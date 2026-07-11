from django.contrib import admin

from .models import Auto, FotoAuto, PropuestaVenta


class FotoAutoInline(admin.TabularInline):
    model = FotoAuto
    extra = 1


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ("marca", "modelo", "anio", "precio", "kilometros", "combustible", "publicado", "destacado")
    list_filter = ("marca", "combustible", "transmision", "publicado", "destacado")
    search_fields = ("marca", "modelo", "version")
    list_editable = ("publicado", "destacado")
    inlines = [FotoAutoInline]
    fieldsets = (
        ("Datos principales", {
            "fields": ("marca", "modelo", "anio", "version", "precio")
        }),
        ("Ficha técnica", {
            "fields": ("combustible", "transmision", "kilometros", "color", "puertas", "motor")
        }),
        ("Detalles y desperfectos", {
            "fields": ("descripcion", "detalles_desperfectos")
        }),
        ("Multimedia", {
            "fields": ("foto_principal",)
        }),
        ("Publicación", {
            "fields": ("publicado", "destacado")
        }),
    )


@admin.register(PropuestaVenta)
class PropuestaVentaAdmin(admin.ModelAdmin):
    list_display = ("nombre_apellido", "marca", "modelo", "anio", "valor_pretendido", "email", "telefono", "contactado", "creado")
    list_filter = ("contactado", "combustible", "tiene_deudas", "tiene_vtv")
    search_fields = ("nombre_apellido", "marca", "modelo", "email", "telefono")
    list_editable = ("contactado",)
    readonly_fields = ("creado",)
