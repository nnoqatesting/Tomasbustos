from django.urls import path

from . import views

app_name = "autos"

urlpatterns = [
    path("", views.CatalogoAutosView.as_view(), name="catalogo"),
    path("auto/<int:pk>/", views.AutoDetailView.as_view(), name="auto_detail"),
    path("vende-tu-auto/", views.vende_tu_auto, name="vende_tu_auto"),
    path("quienes-somos/", views.quienes_somos, name="quienes_somos"),
    path("contacto/", views.contacto, name="contacto"),
]
