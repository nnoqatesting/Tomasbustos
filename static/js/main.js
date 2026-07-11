/**
 * Bustos Cars — interacciones del sitio.
 *
 * 1) Efecto "odómetro": los precios y kilómetros (marcados con
 *    data-odometro) cuentan desde 0 hasta su valor real la primera
 *    vez que entran en pantalla, como el tablero de un auto.
 * 2) Contador de caracteres para el textarea de "Observaciones".
 */

document.addEventListener("DOMContentLoaded", function () {
  iniciarOdometros();
  iniciarContadorObservaciones();
});

function iniciarOdometros() {
  var elementos = document.querySelectorAll("[data-odometro]");
  if (!elementos.length) return;

  var prefiereMenosMovimiento = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
  ).matches;

  elementos.forEach(function (el) {
    var valorFinal = parseFloat(el.getAttribute("data-odometro"));
    var prefijo = el.getAttribute("data-prefijo") || "";
    var sufijo = el.getAttribute("data-sufijo") || "";

    if (isNaN(valorFinal)) return;

    if (prefiereMenosMovimiento) {
      el.textContent = prefijo + formatearNumero(valorFinal) + sufijo;
      return;
    }

    // Mostrar en 0 hasta que entre en viewport
    el.textContent = prefijo + "0" + sufijo;

    var observador = new IntersectionObserver(
      function (entradas, obs) {
        entradas.forEach(function (entrada) {
          if (entrada.isIntersecting) {
            animarNumero(el, valorFinal, prefijo, sufijo);
            obs.unobserve(el);
          }
        });
      },
      { threshold: 0.4 }
    );

    observador.observe(el);
  });
}

function animarNumero(el, valorFinal, prefijo, sufijo) {
  var duracionMs = 900;
  var inicio = null;

  function paso(timestamp) {
    if (!inicio) inicio = timestamp;
    var progreso = Math.min((timestamp - inicio) / duracionMs, 1);
    // easeOutCubic: arranca rápido, frena suave (como un odómetro real)
    var progresoSuavizado = 1 - Math.pow(1 - progreso, 3);
    var valorActual = Math.floor(valorFinal * progresoSuavizado);

    el.textContent = prefijo + formatearNumero(valorActual) + sufijo;

    if (progreso < 1) {
      requestAnimationFrame(paso);
    } else {
      el.textContent = prefijo + formatearNumero(valorFinal) + sufijo;
    }
  }

  requestAnimationFrame(paso);
}

function formatearNumero(valor) {
  return Math.round(valor).toLocaleString("es-AR");
}

function iniciarContadorObservaciones() {
  var textarea = document.getElementById("id_observaciones");
  var contador = document.getElementById("contador-observaciones");
  if (!textarea || !contador) return;

  var maximo = 250;

  function actualizar() {
    var restantes = maximo - textarea.value.length;
    contador.textContent = restantes + " caracteres restantes";
    contador.classList.toggle("text-danger", restantes < 0);
  }

  textarea.addEventListener("input", actualizar);
  actualizar();
}
