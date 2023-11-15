const calculos = {
  sumar: function (a, b) {
    return a + b;
  },
  multiplicar: function (a, b) {
    return a * b;
  },
};
calculos.cuadrado = function (a) {
  return a * a;
};

module.exports = calculos;
