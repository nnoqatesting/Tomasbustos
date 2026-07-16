# Bustos Cars — Sitio de Concesionaria (Django)

Proyecto Django listo para abrir en VS Code. Incluye:

- App **`autos`** con los modelos `Auto`, `FotoAuto` y `PropuestaVenta`.
- Catálogo con buscador por marca, detalle de vehículo, formulario "Vendé tu auto",
  "Quiénes somos" y "Contacto".
- **Diseño oscuro y minimalista** con tipografía corporativa: `Barlow Condensed`
  para títulos, `Inter` para texto y `IBM Plex Mono` para datos técnicos
  (precio, km, ficha técnica), todo en `static/css/estilos.css`.
- **JavaScript** (`static/js/main.js`): efecto "odómetro" — precios y kilómetros
  cuentan desde 0 hasta su valor real al entrar en pantalla, como el tablero de
  un auto — y contador de caracteres en "Observaciones". Respeta
  `prefers-reduced-motion`.
- **10 autos ficticios** de ejemplo ya cargados en `db.sqlite3` (Volkswagen,
  Fiat, Peugeot, Chevrolet, Renault, Toyota, Ford, Citroën, Nissan) para ver el
  catálogo funcionando apenas levantás el servidor. Podés recargarlos con:
  `python manage.py seed_autos --reset`
- Panel de administración de Django ya configurado (`/admin/`) para cargar autos
  reales (con fotos) y ver las propuestas de venta recibidas.
- **Fotos reales** cargadas para 3 vehículos (Renault Duster Oroch, Peugeot 308,
  Volkswagen Polo) mediante el comando `python manage.py asignar_fotos_demo`.
- **Logo "Bustos Cars"** con tipografía distintiva (Big Shoulders Display) y una
  animación de brillo/expansión de letras al pasar el cursor por encima.
- **Cards del catálogo** con animación de aparición al hacer scroll (fade + subida
  sutil) y una etiqueta "Destacado" para los autos marcados como tal.
- Botón de WhatsApp con un pulso animado sutil para que se note más al scrollear,
  visible en toda la landing principal aunque se scrollee.
- **Contacto** con el teléfono de Tomás, un enlace directo a WhatsApp, y el
  mapa de Google Maps embebido (Quintana y Sobremonte, Virreyes) al lado de
  la información.

## 1. Instalación

```bash
# Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate      # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

## 2. Base de datos y superusuario

El zip ya incluye un `db.sqlite3` con los 10 autos de ejemplo cargados, así que
podés saltar directo al paso 3 para ver el catálogo. Si preferís empezar de cero:

```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_autos      # carga los 10 autos ficticios
```

## 3. Ejecutar el servidor

```bash
python manage.py runserver
```

Abrí `http://127.0.0.1:8000/` para ver el catálogo y `http://127.0.0.1:8000/admin/`
para cargar autos (con fotos) y revisar las propuestas de venta.

## 4. Estructura del proyecto

```
concesionaria/          # Configuración del proyecto (settings, urls raíz)
autos/
  models.py             # Auto, FotoAuto, PropuestaVenta
  forms.py              # PropuestaVentaForm (ModelForm)
  views.py              # CatalogoAutosView, AutoDetailView, vende_tu_auto, etc.
  urls.py                # Rutas de la app
  admin.py               # Configuración del admin
  management/commands/
    seed_autos.py         # Carga los 10 autos ficticios (--reset para recargar)
    asignar_fotos_demo.py # Asigna las 3 fotos reales (Oroch, 308, Polo)
  fixtures_media/          # Fotos reales de origen (oroch.jpg, peugeot_308.jpg, polo.jpg)
  templates/autos/
    base.html            # Header + footer comunes a todo el sitio
    catalogo.html         # Autos Seleccionados + buscador
    detalle_auto.html     # Ficha técnica + desperfectos
    vende_tu_auto.html    # Formulario en 2 columnas
    quienes_somos.html
    contacto.html
static/
  css/estilos.css        # Sistema visual oscuro y minimalista
  js/main.js              # Efecto odómetro + contador de caracteres
media/                    # Acá se guardan las fotos subidas desde el admin
db.sqlite3                # Ya incluye los 10 autos de ejemplo
```

## 5. Recargar los autos de ejemplo

```bash
python manage.py seed_autos --reset
```

Esto borra los autos actuales y vuelve a cargar los 10 de ejemplo. Sin `--reset`
simplemente agrega los que falten sin duplicar los que ya existen.

## 6. Próximos pasos sugeridos

- Reemplazar las imágenes de placeholder (`quienes_somos.html`, `vende_tu_auto.html`)
  por fotos propias de la concesionaria.
- Configurar el envío de email al recibir una propuesta de venta (`views.vende_tu_auto`).
- Agregar `django.contrib.humanize` si querés precios con formato de miles automático.
- En producción: configurar `ALLOWED_HOSTS`, `DEBUG = False`, una base de datos
  como PostgreSQL, y servir `static/`/`media/` con `whitenoise` o un bucket externo.
