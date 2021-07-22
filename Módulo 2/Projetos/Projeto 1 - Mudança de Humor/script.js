// function img01 () {
//     document.getElementById("trocarimg").src="feliz.gif";
// }

const btn = document.getElementById("botao");
const img = document.getElementById("trocarimg");

btn.onclick = function () {
    if(btn.value === 'img1'){
        img.src="feliz.gif";
        btn.value = 'img2';
    }
    else if (btn.value === 'img2'){
        img.src="triste.gif";
        btn.value = 'img1'
    }
}


// Adicione um campo de formulário no final com os itens: 
// nome, endereço, e forma de pagamento (escolher entre dinheiro ou cartão)
