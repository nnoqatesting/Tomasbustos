from django.core.management.base import BaseCommand

from autos.models import Auto

AUTOS_DEMO = [
    dict(
        marca="Volkswagen", modelo="Polo", anio=2023, version="1.6 MSI Track",
        combustible="nafta", transmision="manual", kilometros=18500,
        color="Gris Platino", puertas=5, motor="1.6L 16v", precio=21500000,
        descripcion="Único dueño, service oficial al día, cubiertas nuevas.",
        detalles_desperfectos="Sin detalles a reparar.",
        destacado=True,
    ),
    dict(
        marca="Fiat", modelo="Cronos", anio=2022, version="1.3 Precision CVT",
        combustible="nafta", transmision="automatica", kilometros=56081,
        color="Blanco Banchisa", puertas=4, motor="1.3L 8v", precio=17900000,
        descripcion="Sedán familiar con caja automática CVT, ideal para uso diario.",
        detalles_desperfectos="Rayón leve en paragolpes trasero.",
    ),
    dict(
        marca="Peugeot", modelo="208", anio=2017, version="1.6 5P Feline",
        combustible="nafta", transmision="automatica", kilometros=91150,
        color="Gris Aluminium", puertas=5, motor="1.6L 16v", precio=13800000,
        descripcion="Versión tope de gama con techo panorámico y llantas de aleación.",
        detalles_desperfectos="Falta funda de manija delantera derecha.",
    ),
    dict(
        marca="Chevrolet", modelo="Onix", anio=2021, version="1.2 LT",
        combustible="nafta", transmision="manual", kilometros=48200,
        color="Rojo Absolute", puertas=5, motor="1.2L 8v", precio=15200000,
        descripcion="Hatchback compacto, muy económico, ideal primer auto.",
        detalles_desperfectos="Sin detalles a reparar.",
    ),
    dict(
        marca="Renault", modelo="Duster Oroch", anio=2023, version="1.3 Turbo Iconic CVT",
        combustible="nafta", transmision="automatica", kilometros=22300,
        color="Blanco Glacier", puertas=4, motor="1.3L Turbo", precio=32900000,
        descripcion="Pick up mediana 4x2, equipamiento completo, garantía de fábrica vigente.",
        detalles_desperfectos="Sin detalles a reparar.",
        destacado=True,
    ),
    dict(
        marca="Toyota", modelo="Hilux", anio=2019, version="2.8 SRV 4x4 AT",
        combustible="gasoil", transmision="automatica", kilometros=112400,
        color="Gris Plata", puertas=4, motor="2.8L Turbodiesel", precio=42500000,
        descripcion="Pick up 4x4 con caja automática, cúpula y barras antivuelco.",
        detalles_desperfectos="Requiere cambio de amortiguadores traseros. Detalle de pintura en óptica izquierda.",
    ),
    dict(
        marca="Ford", modelo="Ka", anio=2020, version="1.5 SE",
        combustible="nafta", transmision="manual", kilometros=63700,
        color="Blanco Oxford", puertas=5, motor="1.5L 16v", precio=12300000,
        descripcion="Hatchback ágil para ciudad, bajo consumo.",
        detalles_desperfectos="Sin detalles a reparar.",
    ),
    dict(
        marca="Citroën", modelo="C3 Aircross", anio=2018, version="1.6 Feel",
        combustible="nafta", transmision="manual", kilometros=78900,
        color="Rojo Aden", puertas=5, motor="1.6L 16v", precio=16400000,
        descripcion="SUV compacta, muy buen espacio interior y baúl.",
        detalles_desperfectos="Desgaste en tapizado de asiento del conductor.",
    ),
    dict(
        marca="Nissan", modelo="Versa", anio=2021, version="1.6 Exclusive CVT",
        combustible="nafta", transmision="automatica", kilometros=41200,
        color="Negro Ébano", puertas=4, motor="1.6L 16v", precio=18700000,
        descripcion="Sedán con equipamiento full, cámara de retroceso y control crucero.",
        detalles_desperfectos="Sin detalles a reparar.",
    ),
    dict(
        marca="Chevrolet", modelo="S10", anio=2017, version="2.8 TD DC 4x2 HC",
        combustible="gasoil", transmision="manual", kilometros=136483,
        color="Gris Switchblade", puertas=4, motor="2.8L Turbodiesel", precio=29800000,
        descripcion="Pick up doble cabina, motor confiable, apta para trabajo.",
        detalles_desperfectos="Detalle estético en paragolpes trasero. Necesita cambio de pastillas de freno.",
    ),
]


class Command(BaseCommand):
    help = "Carga (o recarga) autos ficticios de ejemplo para visualizar el catálogo."

    def add_arguments(self, parser):
        parser.add_argument(
            "--reset",
            action="store_true",
            help="Borra todos los autos existentes antes de cargar los de ejemplo.",
        )

    def handle(self, *args, **options):
        if options["reset"]:
            borrados, _ = Auto.objects.all().delete()
            self.stdout.write(self.style.WARNING(f"Se borraron {borrados} autos existentes."))

        creados = 0
        for datos in AUTOS_DEMO:
            _, fue_creado = Auto.objects.get_or_create(
                marca=datos["marca"],
                modelo=datos["modelo"],
                anio=datos["anio"],
                version=datos["version"],
                defaults=datos,
            )
            if fue_creado:
                creados += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Listo: {creados} autos nuevos cargados (de {len(AUTOS_DEMO)} de ejemplo)."
            )
        )
