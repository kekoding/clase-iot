led_id = [1, 2, 3];

async function getStatus() {
  const status = await fetch("http://localhost:5500/status");
  const data = await status.json();
  console.log(data);
  data.data.forEach((led) => {
    let button = document.getElementById(`led-${led.id}`);
    button.innerText = led.status === true ? "encendido" : "apagado";
  });
}

async function turnOnBoton(e) {
  const boton_id = e.target.id;
  console.log(boton_id);
  const id = e.target.id[e.target.id.length - 1];
  console.log(id);
}

window.addEventListener(
  "load",
  (event) => {
    getStatus();
    const botonUno = document.getElementById("led-1");
    botonUno.addEventListener("click", (event) => turnOnBoton(event), false);
  },
  false
);

/*
const botones = document.querySelectorAll("button");
botones.forEach((boton) => {
  boton.addEventListener(
    "click",
    (event) => {
      console.log(event);
      turnOnBoton(event);
    },
    false
  );
});
*/
