// Exemplo:
// let pessoa = {nome: "João", idade: 30};
// pessoa.profissao = "Desenvolvedor";
// console.log(pessoa);
// delete pessoa.idade;
// console.log(pessoa);
// pessoa.nome = "Maria";
// pessoa.idade = 31;
// console.log(pessoa);

const { StrictMode } = require("react");

// Atividade 01
// Crie um objeto chamado carro que contenha as seguintes propriedades:

// marca: uma string representando a marca do carro.
// modelo: uma string representando o modelo do carro.
// ano: um número representando o ano de fabricação.

// Após criar o objeto, exiba no console cada uma das propriedades separadamente (marca, modelo, e ano).

// let carro = {marca:"VW", modelo:"Fusca", ano: 1966};

// console.log(carro.marca);
// console.log(carro.modelo);
// console.log(carro.ano);

// Atividade 02
// Crie um objeto chamado pessoa com as propriedades nome, idade, e profissao.

// Em seguida:
// Altere a propriedade profissao para um novo valor.
// Adicione uma nova propriedade chamada cidade ao objeto.
// Exiba no console o objeto completo após as modificações.

// let pessoa = {nome: "Alessandra", idade: 51, profissao: "bancária"};
// pessoa.profissao = "estudante";
// pessoa.cidade = "Belo Horizonte";
// console.log(pessoa);

// DESESTRUTURAÇÃO DE OBJETO:
// atribuir às variáveis o mesmo nome da propriedade (desestruturar).
// Exemplo:
// let pessoa = {nome: "João", idade: 30, profissao: "Desenvolvedor"};

// let {nome , profissao } = pessoa;
// console.log(nome);
// console.log(profissao);

// let { idade } = pessoa;
// console.log(idade);

// REST OPERADOR COM FUNÇÕES
// Permite que você agrupe múltiplos argumentos ou elementos em um único array.
// Ele é usado principalmente em funções para coletar os argumentos restantes em
// um array, ou em objetos e arrays para agrupar elementos restantes.

// Exemplo:
// function somar(...numeros){
//     return numeros.reduce((acc,num)=>acc + num,0);
// };

// console.log(somar(1,25,575,14));

// Atividade 03
// Crie um objeto chamado livro que contenha as seguintes propriedades:

// titulo: uma string representando o título do livro.
// autor: uma string com o nome do autor.
// ano: um número representando o ano de publicação.
// editora: uma string com o nome da editora.

// Utilize a desestruturação para extrair as propriedades titulo e autor do objeto livro. Em seguida, exiba essas propriedades no console.
   
// let livro = {titulo: "O Pequeno Príncipe", autor: "Antoine de Saint-Exupéry", ano: 1943, editora:"FTD"};

// let { titulo, autor } = livro;
// console.log(titulo);
// console.log(autor);

// SPREAD OPERATOR
// O spread operator (...) é uma funcionalidade do JavaScript que permite "espalhar" os elementos de um array ou as propriedades de um objeto em outro array ou objeto.

// Exemplo:
// const arr1= [1,2,3];
// const arr2 = [...arr1,4,5];

// const obj1 = {a:1, b:2};
// const obj2 = {...obj1, c:3};

// console.log(arr2);
// console.log(obj2);

// Atividade 04
// Crie um array chamado livros, onde cada elemento do array é um objeto representando um livro, com as seguintes propriedades:

// titulo: string com o título do livro.
// autor: string com o nome do autor.

// Após criar o array:
// - Exiba no console todos os títulos dos livros.
// - Adicione um novo objeto representando outro livro ao array.
// - Exiba no console a lista completa de livros após a adição.

// let livros = [{titulo: "O Pequeno Príncipe", autor: "Antoine de Saint-Exupéry"},{titulo:"Chapeuzinho Vermelho",autor:"Charles Perrault"},{titulo:"O Gato de Botas",autor:"Charles Perrault"},{livro:"Branca de Neve", autor:"Jacob e Wilhelm Grimm"}];

// for (livro of livros){
//     let { autor } = livro;
//     console.log(autor); 
// }

// livros.push({titulo:"Os Três Porquinhos",autor:"Joseph Jacobs"});

// console.log(livros);

// Atividade 05
// Crie dois objetos chamados representando dois carros com as seguintes propriedades:

// marca: string com a marca do carro.
// modelo: string com o modelo do carro.
// ano: número representando o ano de fabricação.

// Em seguida:
// - Crie um novo objeto que combine as propriedades dos dois objetos usando o spread operator.
// - Exiba o novo objeto no console.

// let carro1 = {marca:"Ford",modelo:"Fiesta",ano:2025};

// let carro2 = {marca:"Fiat", modelo: "Strada", ano: 2024};

// let carros = {carro1: {...carro1}, carro2: {...carro2}};
// console.log(carros);

