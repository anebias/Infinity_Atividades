// // FILTER
// fetch('https://fakestoreapi.com/products').then(response =>response.json()).then(data => {
//     const produtosDisponiveis = data.filter(produto => produto.price > 700);
//     console.log(`Qde: ${produtosDisponiveis.length}`,produtosDisponiveis);
// });

// // MAP
// fetch('https://fakestoreapi.com/products')
//     .then(response =>response.json())
//     .then(data => {
//         const nomesProdutos = data.map(produto => produto.title);
//         console.log(nomesProdutos);
// });

// // PAGINAÇÃO
// const page = 2;
// const limit = 5; // quantidade por página
// fetch(`https://fakestoreapi.com/products?limit=${limit}&page=${page}}`)
//     .then(response =>response.json())
//     .then(data =>console.log(data));

// TIMEOUTS E CONEXÕES LENTAS

function fetchComTimeout(url, options = {}, timeout = 5000) {
    return Promise.race([
        fetch(url, options),
        new Promise((_, reject) =>
            setTimeout(() => reject(new Error('Timeout: A requisição excedeu o tempo limite')), timeout)
        )
    ]);
};

fetchComTimeout('https://fakestoreapi.com/products')
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Erro:',error.message));