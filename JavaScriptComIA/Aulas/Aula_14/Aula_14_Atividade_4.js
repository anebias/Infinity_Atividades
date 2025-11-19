// Atividade 04
// Usando JavaScript e Fetch API, crie uma função chamada criarPost.
//  - A função deve fazer uma requisição POST para a seguinte URL da API pública: https://jsonplaceholder.typicode.com/posts.
//  - Envie um objeto JSON com as seguintes propriedades: title, body, e userId.
//  - Converta a resposta para JSON e exiba no console o objeto retornado pela API.

const { response } = require("express");

async function criarPost(post) {
    try {
        const postString = JSON.stringify(post);
    const response = await fetch('https://jsonplaceholder.typicode.com/posts',{
        method: "POST",
        body: postString
    });

    const resultadoObject = await response.json();

    console.log("post criado: ",resultadoObject);

    } catch (error) {
        console.error("message error: ", error)
    };
};

const post = {
    title: "título do post",
    body: "corpo do post",
    userId: 12345
};

// criarPost(post);

// OUTRA FORMA PARA RESOLVER (NÃO MODERNA):
fetch('https://jsonplaceholder.typicode.com/posts',{
        method: "POST",
        body: JSON.stringify({
    title: "título do post",
    body: "corpo do post",
    userId: 12345
})
    }).then(response => response.json())
    .then(data=>{
        console.log('criado',data)
    }).catch(error =>{console.error(error)}).finally(console.log('finalizado'));