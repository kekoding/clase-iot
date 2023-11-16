var fs = require("fs");

fs.readFile(
  "../practica_importacion_evento/package.json",
  function (err, data) {
    console.log(data);
  }
);

fs.readFile(
  "../practica_importacion_evento/package.json",
  "utf8",
  (err, data) => {
    console.log(data);
  }
);

fs.writeFile("./prueba.txt", "Hola Mundo!!", (err) => {
  if (err) {
    console.log(err);
  }
});
