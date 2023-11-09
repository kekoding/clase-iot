//const = variable constante, no se puede cambiar
const msg = "El mensaje";
// var = variable global que puede ser cambiada
var msg2 = "El Mensaje 2";
// let = variables locales que pueden ser cambiadas
let msg3 = "El Mensaje 3";

function encenderLed(msg) {
  console.log(`El mensaje es ${msg}`);
  return;
}

var contador = 0;
function incrementarConteo(contador) {
  contador++;
  console.log(`El valor del contador es ${contador}`);
}

("Este es un string");
"Este es otro string"`Este es todavía otro string`;

let arregloNumeros = [1, 2, 3, 4, 5];
arregloNumeros.forEach((numero) => console.log(numero * numero));

/*
for numero in arregloNumeros:
    numero*numero
    print(numero*numero)
*/

arregloNumeros.forEach((numero) => {
  let cuadrado = numero * numero;
  console.log(cuadrado);
});

/*
numero : int = 2

typescript -
*/

let numero1 = "1";
let numero2 = 1;

if (numero1 === numero2) {
} else {
}

persona = { nombre: "Jorge Quintanilla", funcion: "maestro" };
persona["nombre"];
persona.nombre;

// ! - Negación (not)
// && - and
// || - or
// ~ - NOR
