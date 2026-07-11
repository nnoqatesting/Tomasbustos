from django.db import models
from django.urls import reverse


class Auto(models.Model):
    """Vehículo usado publicado en el catálogo del sitio."""

    COMBUSTIBLE_CHOICES = [
        ("nafta", "Nafta"),
        ("gasoil", "Gasoil"),
        ("gnc", "GNC"),
        ("hibrido", "Híbrido"),
        ("electrico", "Eléctrico"),
    ]

    TRANSMISION_CHOICES = [
        ("manual", "Manual"),
        ("automatica", "Automática"),
    ]

    # Datos principales (obligatorios en el listado)
    marca = models.CharField(max_length=60)
    modelo = models.CharField(max_length=80)
    anio = models.PositiveIntegerField(verbose_name="Año")

    # Ficha técnica
    version = models.CharField(max_length=120, blank=True, help_text="Ej: 1.6 5P Feline")
    combustible = models.CharField(max_length=20, choices=COMBUSTIBLE_CHOICES, default="nafta")
    transmision = models.CharField(max_length=20, choices=TRANSMISION_CHOICES, default="manual")
    kilometros = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=40, blank=True)
    puertas = models.PositiveSmallIntegerField(default=4)
    motor = models.CharField(max_length=60, blank=True, help_text="Ej: 1.6L 16v")
    precio = models.DecimalField(max_digits=12, decimal_places=2)

    # Detalles / desperfectos a reparar
    detalles_desperfectos = models.TextField(
        blank=True,
        verbose_name="Detalles / Desperfectos a reparar",
        help_text="Detalles estéticos o mecánicos a informar al comprador.",
    )
    descripcion = models.TextField(blank=True, verbose_name="Descripción general")

    # Multimedia
    foto_principal = models.ImageField(upload_to="autos_fotos/", blank=True, null=True)

    # Meta
    publicado = models.BooleanField(default=True)
    destacado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-destacado", "-creado"]
        verbose_name = "Auto"
        verbose_name_plural = "Autos"

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio})"

    def get_absolute_url(self):
        return reverse("autos:auto_detail", kwargs={"pk": self.pk})


class FotoAuto(models.Model):
    """Fotos adicionales de un auto (opcional, para galería en el detalle)."""

    auto = models.ForeignKey(Auto, related_name="fotos", on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="autos_fotos/galeria/")

    def __str__(self):
        return f"Foto de {self.auto}"


class PropuestaVenta(models.Model):
    """Datos enviados por un usuario a través del formulario 'Vendé tu auto'."""

    SI_NO = [
        ("si", "Sí"),
        ("no", "No"),
    ]

    COMBUSTIBLE_CHOICES = [
        ("nafta", "Nafta"),
        ("gasoil", "Gasoil"),
        ("gnc", "GNC"),
    ]

    nombre_apellido = models.CharField(max_length=150, verbose_name="Nombre y apellido")
    marca = models.CharField(max_length=60, verbose_name="Marca del vehículo")
    modelo = models.CharField(max_length=80, verbose_name="Modelo del vehículo", blank=True)
    anio = models.PositiveIntegerField(verbose_name="Año", blank=True, null=True)
    combustible = models.CharField(max_length=20, choices=COMBUSTIBLE_CHOICES, blank=True)
    kilometros = models.PositiveIntegerField(verbose_name="Kilómetros", blank=True, null=True)
    valor_pretendido = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Valor pretendido")
    tiene_deudas = models.CharField(max_length=3, choices=SI_NO, verbose_name="¿Contiene deudas?")
    tiene_vtv = models.CharField(max_length=3, choices=SI_NO, verbose_name="¿Contiene VTV/RTO?")
    telefono = models.CharField(max_length=30, blank=True)
    email = models.EmailField(verbose_name="Email")
    observaciones = models.TextField(max_length=250, blank=True, verbose_name="Observaciones")

    creado = models.DateTimeField(auto_now_add=True)
    contactado = models.BooleanField(default=False)

    class Meta:
        ordering = ["-creado"]
        verbose_name = "Propuesta de venta"
        verbose_name_plural = "Propuestas de venta"

    def __str__(self):
        return f"{self.nombre_apellido} - {self.marca} {self.modelo}"
