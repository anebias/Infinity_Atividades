// // FILTER
// fetch('https://fakestoreapi.com/products').then(response =>response.json()).then(data => {
//     const produtosDisponiveis = data.filter(produto => produto.price > 700);
//     console.log(`Qde: ${produtosDisponiveis.length}`,produtosDisponiveis);
// });

// MAP
fetch('https://fakestoreapi.com/products')
    .then(response =>response.json())
    .then(data => {
        const nomesProdutos = data.map(produto => produto.title);
        console.log(nomesProdutos);
});

// PAGINAÇÃO
const page = 2;
const limit = 5; // quantidade por página
fetch(`https://fakestoreapi.com/products?limit=${limit}&page=${page}}`)
    .then(response =>response.json())
    .then(data =>console.log(data));