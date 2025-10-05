// Atividade 01
// Crie uma função chamada exibirBoasVindas que, quando chamada, exiba no console a mensagem: "Bem-vindo ao curso de JavaScript!".

// Chame a função duas vezes para verificar que ela funciona corretamente.

// function exibirBoasVindas(){console.log("Bem-vindo ao curso de JavaScript!")};

// exibirBoasVindas();
// exibirBoasVindas();

// Atividade 02
// - Crie uma função chamada saudarUsuario que receba um parâmetro chamado nome.

// - A função deve exibir no console uma mensagem de saudação personalizada, como "Olá, [nome]!".

// - Chame a função três vezes, passando nomes diferentes como argumento.

// function saudarUsuario(nome){console.log(`Olá ${nome}!`)};
// saudarUsuario('Gustavo');
// saudarUsuario('Maria Luiza');
// saudarUsuario('Clarice');

// Atividade 03
// Crie uma função chamada realizarOperacao que receba dois números e uma função de callback como parâmetros.

// Requisitos:
// A função deve executar o callback passando os dois números como argumentos.
// Crie duas funções de callback:
// somar: que recebe dois números e exibe no console a soma deles.
// multiplicar: que recebe dois números e exibe no console o produto deles.
// Teste a função realizarOperacao chamando-a duas vezes, uma vez com o callback somar e outra vez com o callback multiplicar.

// function realizarOperacao(num1,num2,callback){
//     console.log(callback(num1,num2));
// };

// const somar = (num1, num2) => { return num1 + num2 };
// const multiplicar = (num1, num2) => { return num1 * num2 };

// realizarOperacao(1,2,somar);
// realizarOperacao(1,2,multiplicar);
// realizarOperacao(-3,4,somar);
// realizarOperacao(-3,4,multiplicar);

// Atividade 04
// Crie três arrow functions para realizar as seguintes operações  matemáticas:

// soma: Recebe dois números como parâmetros e retorna a soma deles.

// subtracao: Recebe dois números como parâmetros e retorna a diferença entre eles.

// multiplicacao: Recebe dois números como parâmetros e retorna o produto deles.

// Chame cada uma das funções três vezes, passando valores diferentes como argumentos, e exiba o resultado no console.

// const somar = (num1,num2) => { return num1 + num2 };
// const subtrair = (num1,num2) => { return num1 - num2 };
// const multiplicar = (num1,num2) => { return num1 * num2 };

// console.log(somar(6,-9));
// console.log(subtrair(6,-9));
// console.log(multiplicar(6,-9));

// console.log(somar(-2,-4));
// console.log(subtrair(-2,-4));
// console.log(multiplicar(-2,-4));

// console.log(somar(11,3));
// console.log(subtrair(11,3));
// console.log(multiplicar(11,3));

// Atividade 05
// Crie um array chamado numeros com os valores [1, 2, 3, 4, 5]. Usando a função map() e uma arrow function, crie um novo array chamado dobrados que contenha todos os números do array numeros multiplicados por 2.

// let numeros = [1,2,3,4,5];
// let dobrados = numeros.map(num=>2*num);
// console.log(numeros);
// console.log(dobrados);

// Atividade 06
// Crie um array chamado numeros com os valores [1, 2, 3, 4, 5].

// - Usando o método reduce(), calcule a soma de todos os números do array e armazene o resultado em uma variável chamada somaTotal.

// - Usando o método reduce() novamente, calcule o produto de todos os números do array (multiplicação) e armazene o resultado em uma variável chamada produtoTotal.

// - Exiba ambos os resultados no console.

// let numeros = [1,2,3,4,5];
// const soma = numeros.reduce((acc,num)=>{return acc + num},0);
// console.log(soma);

// Atividade 04
// Crie uma classe chamada Carro que tenha as seguintes propriedades e métodos:

// Propriedades:
// marca: uma string que representa a marca do carro.
// modelo: uma string que representa o modelo do carro.
// ano: um número que representa o ano de fabricação do carro.

// Métodos:
// detalhes(): Este método deve exibir no console uma mensagem no formato "Carro: [marca] [modelo], Ano: [ano]".

// Requisitos:
// Crie dois objetos (instâncias) da classe Carro com diferentes valores para as propriedades marca, modelo, e ano.
// Chame o método detalhes() para ambos os objetos e exiba as informações no console.

// class Carro {
//     constructor(marca,modelo,ano){
//         this.marca = marca;
//         this.modelo = modelo;
//         this.ano = ano;
//     };

//     detalhes(){
//         console.log(`Carro: ${this.marca} ${this.modelo}, Ano: ${this.ano}`);
//     };
// };

// let carro1 = new Carro('Fiat','Palio',2017);
// let carro2 = new Carro('Ford','Fiesta',2000);

// carro1.detalhes();
// carro2.detalhes();