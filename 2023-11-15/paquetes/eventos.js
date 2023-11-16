export class EventEmitter {
  constructor() {
    this.eventos = {};
    // {nombre_de_evento:[lista_de_escuchas]}
  }
  // subscripcion de listener a evento
  on(nombreEvento, listener) {
    if (!this.eventos[nombreEvento]) {
      this.eventos[nombreEvento] = [];
    }
    this.eventos[nombreEvento].push(listener);
  }
  emit(nombreEvento, ...args) {
    if (this.eventos[nombreEvento]) {
      this.eventos[nombreEvento].forEach((listener) => {
        listener(...args);
      });
    }
  }
}
