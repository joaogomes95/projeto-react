//Este const funciona com o import que usei no python

const express = require('express');
const app = express();

const port = 3002;

app.use(express.json()); // 

const filmes = [
    {
        id: 1,
        nome: "Capitão América - O primeiro Vingador",
        imagemUrl: "https://play-lh.googleusercontent.com/9LAzip_XWe8eVWEUGCnSJ4xf706RmYtSu5bZRAfvqbs2aW6YVlLbPF7UVTfMpJKQUioKGw",
    },
    {
        id: 2,
        nome: "Capitã Marvel",
        imagemUrl: "https://br.web.img2.acsta.net/pictures/19/02/04/18/35/1468867.jpg",
    },

    {
        id: 3,
        nome: "O incrível Hulk",
        imagemUrl: "https://br.web.img2.acsta.net/c_310_420/pictures/210/485/21048566_20131010182211313.jpg",
    },

    {
        id: 4,
        nome: "Homem de Ferro ",
        imagemUrl: "https://images-na.ssl-images-amazon.com/images/I/81vTHovrz%2BL._AC_SY606_.jpg",
    },

    {
        id: 5,
        nome: "Homem de ferro 2",
        imagemUrl: "https://media.fstatic.com/SFp4c8GT3GTGYok7_526qDSHTns=/290x478/smart/media/movies/covers/2018/09/66432b37ed80464274a58239b695007f95c79155.jpg",
    },
    
    
    
];

//Funções de Validação 

const getFilmesValidos = () => filmes.filter(Boolean);

const getFilmeById = (id) => getFilmesValidos().find((filme) => filme.id == id);
    
const getIndexByFilme = (id) => getFilmesValidos().findIndex((filme) => filme.id === id);

// Padrão para setar o endpoint da aplicação  / Home
app.get('/',(req, res) => {
    res.send("Bem vindo ao site Lista de Filmes");
});

app.get("/filmes", (req, res) => {
    res.send(getFilmesValidos());
  });

app.get('/filmes/:id',(req, res) => {
    const id = req.params.id;
    const filme = getFilmeById(id);

    if(!filme){
        res.send('Filme não encontrado');
    }
    res.send(filme);       
})


//rota de cadastro
// Lista é usado o get, 
//para  criar usamos o post, 
//atualizar -PUT
//e deletar -DELETE

//ainda não sabe da informção que está vindo
app.post('/filmes',(req, res) => {
    const filme = req.body.filme;
    
    if(!filme || !filme.nome ||!filme.imagemUrl){
        res.status(400).send({
            message: "Filme inválido. Tente novamente!"
        });
        return;
    };    

    const ultimoFilme = filmes[filmes.length -1]

    if (filmes.length){
        filme.id = ultimoFilme.id +1;
        filmes.push(filme);
    }else{
        filme.id = 1;
        filmes.push(filme);
    }

    res.send(`filme adicionado com sucesso: ${filme} o id do filme é ${id}`)
});
//------------------------------------------------------
//Atualização usando o put:
app.put('/filmes/:id',(req, res)=>{
    const id = +req.params.id -1; // O -1 se da por conta da lista que sempre começa com número 0
   
    const filmeIndex = getFilmebyIndex(id);

    if (filmeIndex < 0){
        res.status(404).send({
            message: "O filmenão foi encontrado, tente novamente."
        });
        return
    }
    const novoFilme = req.body;

    if(!Object.keys(novoFilme).length){
        res.status(400).send({
            message: "O body está vazio!"
        });
    }

    if (!novoFilme || !novoFilme.nome || !novoFilme.imagemUrl){
        res.send(400).send({
            message:"Filme inválido,tente novamente!"
        });
        return
    }
    
    const filme = getFilmeById(id);
//... sintaxe de espelhamento, nesse caso estamos espelhando o objeto do filme.
    filmes[filmeIndex] = {
        ...filme,
        ...novoFilme,
    }


    res.send(filme[filmeIndex])


// `` funcionam com f' no python.
});

//------------------------------------------------------
//Utilizando o DELETE

app.delete('/filmes/:id',(req, res) =>{
    const id = req.params.id;
    const filmeIndex = getIndexByFilme(id);

    if(filmeIndex < 0){
        res
    }
})


//-------------------------------------------------
app.listen(port, (req, res) => {
    console.info(`App está rodando na porta http://localhost/${port}/`)
});