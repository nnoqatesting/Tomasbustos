from pathlib import Path

from django.core.files import File
from django.core.management.base import BaseCommand

from autos.models import Auto

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # .../autos/
CARPETA_FOTOS = BASE_DIR / "fixtures_media"

# Relación marca/modelo -> archivo de foto real
FOTOS_POR_AUTO = {
    ("Renault", "Duster Oroch"): "oroch.jpg",
    ("Peugeot", "308"): "peugeot_308.jpg",
    ("Volkswagen", "Polo"): "polo.jpg",
}


class Command(BaseCommand):
    help = "Asigna las fotos reales de ejemplo (Oroch, Peugeot 308, Polo) a los autos ya cargados."

    def add_arguments(self, parser):
        parser.add_argument(
            "--forzar",
            action="store_true",
            help="Reemplaza la foto aunque el auto ya tenga una asignada.",
        )

    def handle(self, *args, **options):
        asignadas = 0
        for (marca, modelo), archivo in FOTOS_POR_AUTO.items():
            ruta = CARPETA_FOTOS / archivo
            if not ruta.exists():
                self.stdout.write(self.style.WARNING(f"No encontré el archivo {ruta}"))
                continue

            auto = Auto.objects.filter(marca=marca, modelo=modelo).first()
            if not auto:
                self.stdout.write(self.style.WARNING(f"No hay ningún auto {marca} {modelo} cargado."))
                continue

            if auto.foto_principal and not options["forzar"]:
                self.stdout.write(f"{marca} {modelo} ya tiene foto (usá --forzar para reemplazarla).")
                continue

            with open(ruta, "rb") as f:
                auto.foto_principal.save(archivo, File(f), save=True)

            asignadas += 1
            self.stdout.write(self.style.SUCCESS(f"Foto asignada a {marca} {modelo}."))

        self.stdout.write(self.style.SUCCESS(f"Listo: {asignadas} fotos asignadas."))
