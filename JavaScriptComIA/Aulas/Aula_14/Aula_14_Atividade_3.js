// Atividade 03
//  - Usando JavaScript e Fetch API, crie uma função chamada buscarUsuarios.
//  - A função deve fazer uma requisição GET para a seguinte URL da API pública: https://jsonplaceholder.typicode.com/users.
//  - Converta a resposta para JSON e exiba no console os nomes dos usuários retornados.

async function buscarUsuarios(){
    try {
        const retorno =  await fetch('https://jsonplaceholder.typicode.com/users');
        const retornoObject = await retorno.json();
        console.log(retornoObject);
    } catch (error) {
        console.error(error);
    }
};

buscarUsuarios();
