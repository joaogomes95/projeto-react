const nome = 'Calculadora';

function soma (a, b) {
    return a + b;
};

function sub (a, b) {
    return a - b;
};

function multi (a, b) {
    return a * b;
};

function div (a, b) {
    return a / b;
};


module.exports = {
    soma,
    sub,
    multi,
    div,
    nome,
}

