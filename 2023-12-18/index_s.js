//Cargar mi app web en un servidor NGINX | Apache2

const ciudades = {
  monterrey: {
    latitud: 25.6751,
    longitud: -100.3185,
  },
};

class ComponenteTemperatura {
  constructor(id, fecha, elevacion, valoresTemp, ciudad) {
    this.id = id;
    this.fecha = fecha;
    this.elevacion = elevacion;
    this.valoresTemp = valoresTemp;
    this.ciudad = "Monterrey";
  }
  transformarFecha() {
    return new Date(this.fecha).toLocaleDateString("es-MX", {
      dateStyle: "medium",
    });
  }
  tempPromedio() {
    let accum = 0;
    this.valoresTemp.forEach((d) => {
      accum = accum + d;
    });
    return (accum / this.valoresTemp.length).toFixed(2);
  }
  display() {
    return `
    <div class="temp-data">
      <div class='heading'>
        <i data-feather="activity"></i>
        <h2>${this.ciudad}</h2>
      </div>
      <div class='data'>
        <p>Fecha: ${this.transformarFecha()}</p>
        <p>Temperatura promedio - ${this.tempPromedio()}</p>
        <p>Elevacion - ${this.elevacion}</p>
      </div>
    </div>

    `;
  }
}

async function desplegarTemperatura() {
  const res = await fetch(
    "https://archive-api.open-meteo.com/v1/era5?latitude=25.6751&longitude=-100.3185&start_date=2023-12-14&end_date=2023-12-15&hourly=temperature_2m"
  );
  const temp = await res.json();
  const T = new ComponenteTemperatura(
    1,
    temp.hourly.time[temp.hourly.time.length - 1],
    temp.elevation,
    temp.hourly.temperature_2m
  );

  const tempDiv = document.getElementById("datos-temperatura");
  const art = document.createElement("article");
  art.innerHTML = T.display();
  tempDiv.prepend(art);
  feather.replace();
}

desplegarTemperatura();
desplegarTemperatura();
