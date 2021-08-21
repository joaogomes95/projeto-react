const http = require('http');

http.createServer(function(req, res) {
    res.end('<h1>Ola mundo<h1>');
}).listen(3000);


console.log('Meu servidor está rodando')