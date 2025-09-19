// Atividade 01
// Crie um arquivo JavaScript e siga os passos abaixo para praticar a declaração e uso de variáveis com var, let e const.

// Declare três variáveis:
// Uma variável nome usando var com seu nome.
// Uma variável idade usando let com sua idade.
// Uma constante cidade usando const com o nome da cidade onde você mora.

// Exiba os valores das variáveis no console usando console.log().
// Altere o valor da variável nome para um novo nome.
// Reatribua o valor da variável idade para um novo número.
// Tente alterar o valor da constante cidade e veja o que acontece.

// Exiba novamente os valores de nome e idade no console.

// var nome = 'Alessandra';
// let idade = 51;
// const cidade = 'Belo Horizonte';

// console.log('Nome:', nome, ", Idade:", idade, ', Cidade:', cidade);

// Atividade 02
// Crie um arquivo JavaScript e siga os passos abaixo para praticar a manipulação de variáveis e a realização de operações básicas.

// Declare quatro variáveis:
// - Use let para declarar duas variáveis, num1 e num2, e atribua a elas dois números à sua escolha.
// - Use const para declarar duas variáveis, nome e cidade, e atribua uma string para cada uma delas (seu nome e a cidade onde você mora).

// Crie novas variáveis para armazenar o resultado das seguintes operações entre num1 e num2:
// - Soma (soma)
// - Subtração (subtracao)
// - Multiplicação (multiplicacao)
// - Divisão (divisao)

// Use console.log() para exibir os resultados das operações e as informações das constantes nome e cidade.

// let num1 = 5;
// let num2 = 7;
// const nome = 'Alessandra';
// const cidade = 'Belo Horizonte';
// let soma = num1 + num2;
// let subtracao = num1 - num2;
// let multiplicacao = num1 * num2;
// let divisao = num1 / num2;

// console.log(`Nome`,nome);
// console.log(`Cidade`,cidade);
// console.log(`O resultado da soma é ${soma}`);
// console.log(`O resultado da subtração é ${subtracao}`);
// console.log(`O resultado da multiplicação é ${multiplicacao}`);
// console.log(`O resultado da divisão é ${divisao}`);

// Atividade 03
// Crie um programa em que utilize uma estrutura condicional para resolver um dos seguinte problema:

// Elegibilidade para Desconto no Cinema:
// - Crie uma condicional que verifica se a idade de uma pessoa permite que ela tenha desconto na entrada do cinema.

// Validando a Abertura da Bilheteria:
// - Implemente uma condicional que verifica se a bilheteria está aberta com base no horário atual.

// Determinando o Status de Exibição do Filme:
// - Escreva uma condicional para verificar se um filme está em exibição ou se a exibição já terminou, considerando o horário atual e o horário de término do filme.

// const idadeMaximaDesconto = 12;
// const horarioAbertura = 10;
// const horarioFechamento = 21;

// let idade = 0;
// let horarioAtual = 0;

// if (idade <= idadeMaximaDesconto){
//     console.log(`Ingresso com desconto`);
// } else {
//     console.log(`Ingresso sem desconto (idade > ${idadeMaximaDesconto})`)};

// if (horarioAtual >= horarioAbertura && horarioAtual <= horarioFechamento) {
//     console.log('Bilheteria aberta');
// } else {
//     console.log('Bilheteria fechada')
// };

// Atividade 04
// Crie um arquivo JavaScript e siga os passos abaixo:

// Peça ao usuário que insira a idade e armazene o valor em uma variável chamada idade. (Você pode usar o prompt() para simular a entrada de dados no navegador).

// Usando a estrutura if-else, faça as seguintes verificações:
// - Se a idade for menor que 18, exiba no console: "Você é menor de idade."
// - Se a idade estiver entre 18 e 65 (inclusive), exiba: "Você é um adulto."
// - Se a idade for maior que 65, exiba: "Você é idoso."

// *** Reposta no arquivo Aula_5.html ***

// Atividade 05
// Crie um programa que receba um número n e gere um triângulo numérico invertido no console usando laços de repetição.

// Objetivo:
// Praticar o uso de laços de repetição aninhados e lógica condicional para gerar padrões complexos no console.

// Por exemplo, se n = 5, o resultado no console deve ser:

// 1 2 3 4 5
// 1 2 3 4
// 1 2 3
// 1 2
// 1

// O triângulo deve começar com n números na primeira linha,diminuindo um número a cada linha até chegar a 1.

// const numero = 5;
// let range = []

// for (let j = numero ; j > 0 ; j --) {
    
//     range = [];

//     for (let i = 1 ; i <= j ; i++) {
//     range.push(i);
//     }

//     console.log(range.join(' '));
// };

// Atividade 06
// Crie um arquivo JavaScript e siga os passos abaixo para praticar o uso de loops.

// - Usando um loop for, exiba no console todos os números de 1 a 10.

// - Usando um loop while, exiba no console todos os números pares de 2 a 20.

// - Usando um loop for, crie uma variável chamada soma que acumule a soma dos números de 1 a 5 e exiba o resultado no final.

// for (let i = 1 ; i <= 10 ; i++){
//     console.log(i)
// }

// let j = 2
// while (j <= 20) {
//     console.log(j);
//     j += 2;
// }

// let soma = 0;

// for (let k = 1 ; k <= 5 ; k++) {
//     soma += k;
// }

// console.log('Soma de 1 a 5 =',soma);

// Atividade 07
// Crie um programa que faça o seguinte:

// Geração de Dados:
// Crie um array chamado numeros contendo 20 números inteiros aleatórios entre 1 e 100.

// Filtre os números pares do array e armazene-os em um novo array chamado pares.
// Transforme o array pares para que cada número seja elevado ao quadrado.
// Calcule a soma de todos os números no array transformado.
// Use os métodos avançados de array (filter, map, reduce, etc.) para realizar as seguintes operações:
// Manipulação de Dados:

// Exiba no console o array original, o array de números
// pares, o array de números ao quadrado e a soma final.

const numeros = [49, 83, 54, 19, 63, 95, 57, 32, 73, 56, 36, 71, 84, 11, 59, 65, 88, 36, 46, 77];

const pares = numeros.filter((numero) => {
    return numero %2 === 0;
});

console.log(pares);

quadrados = pares.map(( numero ) => { return numero * numero })

console.log(quadrados);

let soma = quadrados.reduce((acumulador, valorAtual) => { 
    return acumulador + valorAtual },0);

console.log('soma dos quadrados:', soma);

console.log('range original:', numeros);
console.log('filtro pares:', pares);
console.log('quadrado dos pares',quadrados);
console.log('soma dos quadrados:', soma);
