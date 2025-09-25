

// Atividade 01
// Crie um script que contenha um array com alguns números e utilize o método forEach() para percorrê-lo. Para cada número no array, verifique se ele é positivo, negativo ou zero, e exiba uma mensagem no console indicando o resultado.

// let array = [2,-6,3,-5,-9,25,0,98,-4];

// array.forEach((number, index)=>{
//     if(number > 0){
//         console.log(`O número que está no índice ${index} é positivo`);
//     }
//     else if(number < 0 ){
//         console.log(`O número que está no índice ${index} é negativo`);
//     }
//     else {console.log(`O número que está no índice ${index} é zero`);}    
// });

// Atividade 02
// Crie um script que utilize o método map() para transformar um array de números. A transformação deve consistir em calcular o quadrado de cada número do array original. O script deve então armazenar os resultados em um novo array e exibi-lo no console.

// let array = [2,-6,3,-5,-9,25,0,98,-4];

// let quadradoArray = array.map((numero)=>{return numero**2});
// console.log(quadradoArray);

// Atividade 03
// Crie um script que utilize o método filter() para filtrar um array de números, mantendo apenas os números pares. O script deve armazenar os números pares em um novo array e exibi-lo no console.

// let array = [2,-6,3,-5,-9,25,0,98,-4];

// let arrayFiltrado = array.filter((number)=>{return number % 2 === 0});
// console.log(arrayFiltrado);

// Atividade 04
// Crie um script que utilize o método reduce() para somar todos os números de um array. O script deve calcular a soma total e exibir o resultado no console.

// let array = [2,-6,3,-5,-9,25,0,98,-4];

// let soma = array.reduce((acumulador, valorAtual)=>{return acumulador + valorAtual},0);
// console.log(soma);

// Atividade 05
// Crie um script que utilize o método some() para verificar se um array contém algum número negativo. O script deve exibir no console uma mensagem indicando se há ou não números negativos no array.

// let array = [2,-6,3,-5,-9,25,0,98,-4];
// const temNegativo = array.some(number=>number<0?true:false);
// console.log(temNegativo);

// Atividade 06
// Crie um script que utilize o método find() para localizar o primeiro número ímpar em um array de números. O script deve exibir no console o número encontrado ou uma mensagem indicando que não há números ímpares no array.

// let array = [2,-6,3,-5,-9,25,0,98,-4];

// const primeiroImpar = array.find(numero=>numero%2===1?numero:false);
// console.log(primeiroImpar);

// Atividade 07
// Crie um script que utilize o método every() para verificar se todos os números em um array são positivos. O script deve exibir no console uma mensagem indicando se todos os números são positivos ou se há algum número negativo ou zero no array.

// let array = [2,-6,3,-5,-9,25,0,98,-4];
// const todosPositivos = array.every(numero=>numero>0?true:false);
// console.log(todosPositivos);

// let array2 = [2,6,3,5,9,25,0,98,4];
// const todosPositivos2 = array2.every(numero=>numero>0?true:false);
// console.log(todosPositivos2);

// let array3 = [2,6,3,5,9,25,10,98,4];
// const todosPositivos3 = array3.every(numero=>numero>0?true:false);
// console.log(todosPositivos3);


