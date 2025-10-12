
function adicionarParagrafo (){
    let novoParagrafo = document.createElement('p');
    
    let paragrafos = document.getElementById('container');

    let contador = paragrafos.childElementCount + 1;

    novoParagrafo.textContent = "Este é um novo parágrafo ! ( " + contador + " )";

    div.appendChild(novoParagrafo);    
};

function removerParagrafo(){
    let paragrafos = document.getElementById('container');
   
    div.removeChild(paragrafos.lastElementChild);   
};

let div = document.getElementById('container');



