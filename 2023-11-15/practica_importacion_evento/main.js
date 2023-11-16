import { Persona } from "../paquetes/persona.js";
import { EventEmitter } from "../paquetes/eventos.js";

const Mario = new Persona("Mario", "10-10-1995");
console.dir(Mario);

// Con esta subscripción, cada vez que hay un nuevo
// capítulo, se le avisa a todos los subscriptores
const subscripcionesNetflix = new EventEmitter();
const nombreEvento = "Nuevo Episodio - One Piece";

/*
subscriptor: {
    nombre_del_episodio,
    duracion,
    fecha_de_estreno
}
*/

function mandarCorreo(datos) {
  console.log(`Se envío un correo al subscriptor ${datos.subscriptor}`);
  console.dir(datos);
}

let subscriptores = [
  "jorge.quintanilla@correo.com",
  "jaime.guzmen@correo.com",
  "jesshua.galeana@correo.com",
];

subscriptores.forEach((subscriptor) => {
  subscripcionesNetflix.on(nombreEvento, (datos) => {
    datos.subscriptor = subscriptor;
    mandarCorreo(datos);
  });
});

subscripcionesNetflix.emit(nombreEvento, {
  nombre_del_episodio: "Vagando por los mares",
  duracion: 55,
  fecha_de_estreno: "2023-12-24",
});
