async function traerTemperatura() {
  let response = await fetch(
    "https://api.openweathermap.org/data/2.5/weather?id=3827406&APPID=2f794563a387e10887f16fd4b7a69ebf"
  );
  const tempObj = await response.json();
  return tempObj;
}

async function desplegarTemperatura() {
  const temperatura = await traerTemperatura();
  console.log(temperatura);
  const div = document.getElementById("temperatura");

  const articulo = document.createElement("article");
  articulo.innerHTML = `<p>${temperatura.main.humidity}%</p><p>${(
    temperatura.main.temp - 272.15
  ).toFixed(2)} Celsius</p>`;

  div.appendChild(articulo);
}

desplegarTemperatura();
