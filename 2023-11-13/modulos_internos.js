const url_paquete = require("url");
const queryString = require("querystring");

const url =
  "https://archive-api.open-meteo.com/v1/era5?latitude=52.52&longitude=13.41&start_date=2021-01-01&end_date=2021-12-31&hourly=temperature_2m";

const parametros = queryString.parse(url);
const miUrl = queryString.stringify(url_paquete.format(parametros));

console.log(miUrl);
