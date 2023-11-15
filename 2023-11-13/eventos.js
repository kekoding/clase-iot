/*
*args = dada una lista... o un arreglo de parámetros... expándelos
**kwargs = dado un diccionario... expande el diccionario en llaves y valores


persona = {
  "nombre":"Fernando",
  "edad":20
}

imprimir_persona(**persona) ---- edad=20, nombre="Fernando"


def imprimir_persona(edad:int=30, nombre:str="Jorge"):
      return f'El nombre de la persona es {nombre} y tiene {edad} años'
*/

// Patrón de Programación de Eventos
class EventEmitter {
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
