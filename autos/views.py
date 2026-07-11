from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView

from .forms import PropuestaVentaForm
from .models import Auto


class CatalogoAutosView(ListView):
    """Vista 'Autos Seleccionados': catálogo + buscador por marca."""

    model = Auto
    template_name = "autos/catalogo.html"
    context_object_name = "autos"
    paginate_by = 9

    def get_queryset(self):
        queryset = Auto.objects.filter(publicado=True)
        marca_buscada = self.request.GET.get("q", "").strip()
        if marca_buscada:
            queryset = queryset.filter(marca__icontains=marca_buscada)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        return context


class AutoDetailView(DetailView):
    """Vista de detalle de un vehículo (botón 'Información')."""

    model = Auto
    template_name = "autos/detalle_auto.html"
    context_object_name = "auto"

    def get_queryset(self):
        return Auto.objects.filter(publicado=True)


def vende_tu_auto(request):
    """Vista 'Vendé tu auto': formulario de captación de vehículos."""

    if request.method == "POST":
        form = PropuestaVentaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "¡Gracias! Recibimos tus datos. En breve un asesor de Grupo se va a comunicar con vos.",
            )
            return redirect("autos:vende_tu_auto")
    else:
        form = PropuestaVentaForm()

    return render(request, "autos/vende_tu_auto.html", {"form": form})


def quienes_somos(request):
    """Vista 'Quiénes somos'."""
    return render(request, "autos/quienes_somos.html")


def contacto(request):
    """Vista 'Contacto'."""
    return render(request, "autos/contacto.html")
