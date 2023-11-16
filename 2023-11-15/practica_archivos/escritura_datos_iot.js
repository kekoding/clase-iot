const fs = require("fs");

const datosTemperatura = [
  { fecha: "2023-11-15T18:19:00.00", temperatura: 20 },
  { fecha: "2023-11-15T18:19:02.00", temperatura: 18 },
];

fs.writeFile(
  "./datos_temperatura.json",
  JSON.stringify(datosTemperatura),
  (err) => {
    if (err) {
      console.log(err);
    }
  }
);

fs.readFile("./datos_temperatura.json", "utf8", (err, temperatura) => {
  if (err) {
    console.log(err);
  }
  const datos = JSON.parse(temperatura);
  console.dir(datos);
  let accumulador = 0;
  datos.forEach((dato) => {
    accumulador = accumulador + dato.temperatura;
  });
  console.log(`Promedio = ${accumulador / datos.length}`);
  /*
  let acumulador = 0;
  datos.forEach((temperatura) => {
    acumulador += temperatura;
  }); */
});
