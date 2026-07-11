from django import forms

from .models import PropuestaVenta


class PropuestaVentaForm(forms.ModelForm):
    """Formulario de la vista 'Vendé tu auto'."""

    class Meta:
        model = PropuestaVenta
        fields = [
            "nombre_apellido",
            "marca",
            "modelo",
            "anio",
            "combustible",
            "kilometros",
            "valor_pretendido",
            "tiene_deudas",
            "tiene_vtv",
            "telefono",
            "email",
            "observaciones",
        ]
        widgets = {
            "nombre_apellido": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "Ej: Juan Pérez"
            }),
            "marca": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "Ej: Volkswagen"
            }),
            "modelo": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "Ej: Polo"
            }),
            "anio": forms.NumberInput(attrs={
                "class": "form-control", "placeholder": "Ej: 2019", "min": 1950, "max": 2100
            }),
            "combustible": forms.Select(attrs={"class": "form-select"}),
            "kilometros": forms.NumberInput(attrs={
                "class": "form-control", "placeholder": "Ej: 65000", "min": 0
            }),
            "valor_pretendido": forms.NumberInput(attrs={
                "class": "form-control", "placeholder": "Valor en $ que esperás obtener"
            }),
            "tiene_deudas": forms.Select(attrs={"class": "form-select"}),
            "tiene_vtv": forms.Select(attrs={"class": "form-select"}),
            "telefono": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "Ej: 11 2345 6789"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control", "placeholder": "tuemail@ejemplo.com"
            }),
            "observaciones": forms.Textarea(attrs={
                "class": "form-control", "rows": 4, "maxlength": 250,
                "placeholder": "Contanos algo más sobre el estado del vehículo (máx. 250 caracteres)"
            }),
        }
        labels = {
            "nombre_apellido": "Nombre y apellido *",
            "valor_pretendido": "Valor pretendido *",
            "email": "Email *",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Sólo estos tres son obligatorios según el requerimiento
        opcionales = [
            "modelo", "anio", "combustible", "kilometros",
            "telefono", "observaciones", "tiene_deudas", "tiene_vtv",
        ]
        for campo in opcionales:
            self.fields[campo].required = False
        self.fields["nombre_apellido"].required = True
        self.fields["marca"].required = True
        self.fields["valor_pretendido"].required = True
        self.fields["email"].required = True
