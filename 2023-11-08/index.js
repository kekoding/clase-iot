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
