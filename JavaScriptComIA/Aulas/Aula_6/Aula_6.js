// Atividade 01
// - Defina a função exibirMensagem.
// - Dentro da função, utilize console.log para exibir uma mensagem fixa, como "Bem-vindo ao JavaScript!".
// - Chame a função e observe o resultado no console.

// function exibirMensagem (){
//     console.log("Bem-vindo ao JavaScript!")
// };

// exibirMensagem()

// Atividade 02
// Crie uma função chamada calcularDesconto que receba dois parâmetros: preco e desconto. A função deve calcular o preço final do produto após aplicar o desconto e retornar esse valor.Chame a função com diferentes valores e exiba o resultado no console.

// function calcularDesconto (preco, desconto){
//     console.log(preco * (1 - desconto / 100 ));
// };

// calcularDesconto(100,20);


// REST OPERATOR

// O rest operator (...) permite que você agrupe vários argumentos em um único array. Isso é útil para funções que recebem um número variável de argumentos.

// Exemplo:
// function listarFilmes(filmePrincipal,...outrosFilmes){
//     console.log(`Filme principal: ${filmePrincipal}`);
//     console.log(`Outros filmes: ${outrosFilmes.join(', ')}`);
// };

// listarFilmes('E o vento levou','Toy Story', 'Shrek', 'Minions');

// Atividade 03
// Crie uma função chamada calcularSoma que utilize o rest operator para aceitar um número indefinido de parâmetros e calcular a soma de todos eles. Chame a função com diferentes quantidades de números e exiba o resultado no console.

// function calcularSoma(num1, ...outrosNumeros){
//     let soma = num1;
//     for (numero of outrosNumeros){
//         soma += numero;
//     }
//     return soma
// };

// console.log(calcularSoma(1,2,3,4,5));

// Atividade 04
// Crie uma função chamada saudacao que receba um parâmetro nome e retorne uma string de saudação no formato "Olá, [nome]!". Em seguida:
// - Chame a função saudacao passando diferentes nomes.
// - Exiba o resultado no console.

// function saudacao(nome){
//     return console.log(`Olá ${nome}!`);
// };

// saudacao('Alessandra');
// saudacao('Gustavo');

// Atividade 05
// Crie três funções anônimas e atribua-as a variáveis para realizar as seguintes operações matemáticas:

// Soma: A função deve receber dois números e retornar a soma deles.
// Subtração: A função deve receber dois números e retornar a subtração do primeiro pelo segundo.
// Multiplicação: A função deve receber dois números e retornar o produto deles.

// Em seguida:
// Chame cada função anônima passando diferentes valores e exiba o resultado no console.

// let soma = function (num1,num2){return num1 + num2};
// console.log(soma(2,3));
// console.log(soma(8,-3));

// let subtracao = function(num1, num2){return num1 - num2};
// console.log(subtracao(2,3));
// console.log(subtracao(8,-3));

// let multiplicacao = function(num1, num2){return num1 * num2};
// console.log(multiplicacao(2,3));
// console.log(multiplicacao(8,-3));

// Atividade 06
// Crie uma função chamada processarArray que receba um array de números e uma função de callback.

// A função processarArray deve aplicar o callback a cada elemento do array e retornar um novo array com os resultados.

// Crie duas funções de callback:
// dobrarNumero: Recebe um número e retorna o dobro dele.
// raizQuadrada: Recebe um número e retorna sua raiz quadrada.

// Use a função processarArray com o callback dobrarNumero para dobrar os valores de um array de números.

// Use processarArray com o callback raizQuadrada para calcular a raiz quadrada dos números.

// Exiba no console os arrays resultantes de cada operação.

// let dobrarNumero = numero => numero*2;
// let raizQuadrada = (numero) => Math.sqrt(numero);

// function processarArray(array,callback){
//     let novoArray = [];
//     for (elemento of array) {
//         novoArray.push(callback(elemento))
//     };
//     return novoArray;
// };

// console.log(processarArray([1,2,3],dobrarNumero));
// console.log(processarArray([100,25,36],raizQuadrada));

// Atividade 06
// Crie uma função arrow chamada filtrarPares que receba um array de números como parâmetro e retorne um novo array contendo apenas os números pares.

// Em seguida, crie outra função arrow chamada calcularMedia que receba um array de números e retorne a média desses números.

// Faça o seguinte:
// - Chame a função filtrarPares passando um array de números.
// - Use o resultado de filtrarPares como argumento para a função calcularMedia.
// - Exiba no console o array filtrado e a média dos números pares.

// function filtrarPares(array){
//     let arrayFiltrado = [];
//     for (elemento of array){
//         if (elemento % 2 === 0){arrayFiltrado.push(elemento)};
//     }
//     return arrayFiltrado;
// };

// function calcularMedia(array){
//     let soma = 0;
//     for(elemento of array){
//         soma += elemento;    
//     }
//     let media = soma / array.length;
//     return media;
// };

// calcularMedia( filtrarPares([5,10,15]) );

// console.log(filtrarPares([5,10,15]));
// console.log(calcularMedia( filtrarPares([5,10,15]) ));