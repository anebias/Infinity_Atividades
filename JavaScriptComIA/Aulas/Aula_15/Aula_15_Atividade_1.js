// <!-- Atividade 1
// Você recebeu um array de objetos que representa produtos, cada um com as propriedades nome e preco. Sua tarefa é criar um código que utilize o método map para aplicar um desconto de 10% no preço de cada produto, gerando um novo array com os preços ajustados. No final, exiba tanto o array original quanto o novo array com os preços atualizados. 

// const produtos = [
// { nome: "Camisa", preco: 50 },
// { nome: "Calça", preco: 80 },
// { nome: "Sapato", preco: 120 }
// ]; -->

const produtos = [
{ nome: "Camisa", preco: 50 },
{ nome: "Calça", preco: 80 },
{ nome: "Sapato", preco: 120 }
];

const produtosDesconto = produtos.map((produto)=>({
    nome: produto.nome,
    preco: produto.preco*0.9
}));

console.log("Original:",produtos);
console.log("Com desconto:",produtosDesconto);

