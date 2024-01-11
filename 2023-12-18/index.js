class ComponenteTemperatura {
  constructor(fecha, arrayTemperaturas, elevacion, ciudad) {
    this.fecha = fecha;
    this.arrayTemperaturas = arrayTemperaturas;
    this.elevacion = elevacion;
    this.ciudad = ciudad;
  }
  getPromedio() {
    let accum = 0;
    this.arrayTemperaturas.forEach((temp) => {
      accum = accum + temp;
    });
    return (accum / this.arrayTemperaturas.length).toFixed(1);
  }
  getFecha() {
    const fecha = new Date(this.fecha);
    const strFecha = fecha.toLocaleDateString("es-MX", {
      dateStyle: "medium",
    });
    return strFecha;
  }
  html() {
    return `
    <div class=datos-temperatura>
        <div class="dtemp-header">
            <i data-feather="activity"></i>
            <h2>${this.ciudad}</h2>
        </div>
        <div class="inf-general">
            <p>T Promedio - ${this.getPromedio()}</p>
            <p>Elevación - ${this.elevacion}</p>
            <p>${this.getFecha()}</p>
        </div>
    </div>
    `;
  }
}

async function getTemperatura(ciudad) {
  const res = await fetch(
    "https://archive-api.open-meteo.com/v1/era5?latitude=25.6751&longitude=-100.3185&start_date=2023-12-13&end_date=2023-12-14&hourly=temperature_2m"
  );
  const datos = await res.json();
  const T = new ComponenteTemperatura(
    datos.hourly.time[0],
    datos.hourly.temperature_2m,
    datos.elevation,
    ciudad
  );

  const divUbicacion = document.getElementById("temperaturas");
  const divNuevo = document.createElement("div");
  divNuevo.innerHTML = T.html();
  divUbicacion.appendChild(divNuevo);
  feather.replace();
}

getTemperatura("Cd. México");
getTemperatura("Monterrey");
getTemperatura("Guadalajara");
