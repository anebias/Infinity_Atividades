// Atividade 02
// Crie um array chamado produtos, onde cada item seja um objeto com as
// seguintes propriedades:
//  - nome: O nome do produto.
//  - preco: O preço do produto.
//  - Converta o array produtos em uma string JSON usando JSON.stringify().
//  - Exiba o resultado no console.

const produtos = [{nome:'cafe', preco:29.99},{nome:'açucar', preco:15.98},{nome:'canela', preco:4.97}];

console.log(JSON.stringify(produtos));