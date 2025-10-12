
function clicado (){
    imagem.setAttribute("src","./img2.jpg");
    link.setAttribute("href","https://chat.deepseek.com/");
    link.textContent = "DeepSeek";
    botao.setAttribute("disabled","");
}

let botao = document.getElementById('meuBotao');

let imagem = document.getElementById('minhaImagem');

let link = document.getElementById('meuLink');
