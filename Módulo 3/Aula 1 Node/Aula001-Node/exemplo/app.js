// JavaScript não é fortemente tipado, então geralmente não será necessário mostrar o tipo do campo.

// Formas de declarar variavel.
// var, let , const

// Var = Variavel de escopo global. Não é muito utilizado por conta da sua atribuição global 
//Mais utilizados: 
//let = Variavel de escopo local.
//const = é uma constante que não pode ser alterada depois de declarada. Para alterar é necessário mudar direto na constante.


const calculadora = require('./calculadora');

console.log(calculadora.soma(1,2))
console.log(calculadora.sub(1,2))
console.log(calculadora.multi(5,2))
console.log(calculadora.div(5,2))