// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
})()


 var total = 0; // variável que retorna o total dos produtos que estão na LocalStorage.
 var i = 0;     // variável que irá percorrer as posições
 var valor = 0; // variável que irá receber o preço do produto convertido em Float.
 
 for(i=1; i<=99; i++) // verifica até 99 produtos registrados na localStorage
 {
	 var prod = localStorage.getItem("produto" + i + ""); // verifica se há recheio nesta posição. 
	 if(prod != null) 
	 {	
		 // exibe os dados da lista dentro da div itens
		 document.getElementById("itens").innerHTML += localStorage.getItem("qtd" + i) + " x ";
		 document.getElementById("itens").innerHTML += localStorage.getItem("produto" + i);
		 document.getElementById("itens").innerHTML += " ";
		 document.getElementById("itens").innerHTML += "R$: " + localStorage.getItem("valor" + i) + "<hr>";
		 
		 // calcula o total dos recheios
		 valor = parseFloat(localStorage.getItem("valor" + i)); // valor convertido com o parseFloat()
		 total = (total + valor); // arredonda para 2 casas decimais com o .toFixed(2)
	 }
 } 
 // exibe o total dos recheios
 document.getElementById("total").innerHTML = total.toFixed(2); 


<button type="button" onclick=" localStorage.clear(); location.reload();"> Limpar carrinho </button>;

