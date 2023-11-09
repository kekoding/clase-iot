var conteo = 0;

const cambiarNombre = (nombre) => {
  const header = document.getElementById("bienvenida");
  header.innerText = `Hola ${nombre}`;
};

window.addEventListener("load", (event) => {
  const boton = document.getElementById("mi-boton");
  boton.addEventListener(
    "click",
    (evento) => {
      evento.preventDefault();
      conteo += 1;
      boton.innerText = `Le he picado ${conteo} veces`;
      if (conteo > 20) {
        alert("Ya le picaste muchas veces!");
        conteo = 0;
        boton.classList.add("escondido");
      }
    },
    false
  );
});

//Ejemplo de Fetch

async function datosTemperatura() {
  resultado = await fetch(
    "https://archive-api.open-meteo.com/v1/era5?latitude=52.52&longitude=13.41&start_date=2021-01-01&end_date=2021-12-31&hourly=temperature_2m"
  );
  datos = await resultado.json();

  const datosTemperatura = datos.hourly.temperature_2m;
  let acumulador = 0;
  datosTemperatura.forEach((dato) => {
    acumulador = acumulador + dato;
  });
  let promedio = acumulador / datosTemperatura.length;
  console.log(promedio);
}
