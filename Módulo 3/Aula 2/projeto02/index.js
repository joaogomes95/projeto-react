//Este const funciona com o import que usei no python

const express = require('express');
const app = express();

const port = 3003;

const games = [
    'Valorant',
    'League of Legends',
    'GTA 5',
    'Ragnarok',
    'The Sims'
];

// Padrão para setar o endpoint da aplicação  / Home
app.get('/',(req, res) => {
    res.send("Bem vindo ao site Lista de Games");
});

games.forEach(function(item, indice) {
    console.log
})

//Gerando game aleatório
//------------------------------------------------------
function randomgame(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}

function jogo(num){
    return games[num];
}


app.get('/gamesa',(req, res) => {
    res.send(`<h1>${jogo(randomgame(0,games.length))}</h1>`);
});



//------------------------------------------------------------------
app.get('/games',(req, res) => {
    res.send(games);
});


app.get('/games/:id',(req, res) => {
    const id = req.params.id -1;
    const game = games[id];
    res.send(game);
})

app.listen(port, (req, res) => {
    console.info(`App está rodando na porta http://localhost/${port}/`)
});