// Variáveis simples
// let idade = 25 // Número
// let nome = "João" // String
// let ativo = true // Booleano
// let saldo = null // Null
// let indefinido = undefined // Indefinido

// // Variáveis compostas
// let frutas = ["maça","banana","laranja"] // Array
// let pessoa = {nome: "Carlos", idade: 40} // Objeto

// // Propriedade lenght
// const array = [1,2,3,4,5]
// console.log(array.length)

// // Acessando elementos de um array
// let animais = ['cachorro','gato','papagaio','tartaruga']
// console.log('posição 1: ',animais[0])
// console.log('posição 2: ',animais[1])
// console.log('posição 3: ',animais[2])
// console.log('posição 4: ',animais[3])

// Atividade 01
// Primeiro, crie um array chamado cores contendo os seguintes elementos: Vermelho, Verde, Azul, Amarelo. Em seguida, acesse e exiba no console o elemento na posição 3.
// Objetivo: Praticar o uso de índices para acessar elementos específicos em um array.

// let cores = ["Vermelho", "Verde","Azul","Amarelo"]
// console.log(cores[2])

// Métodos
// push: adiciona um ou mais elementos e retorna o novo comprimento do array
// pop: remove o último elemento e o retorna
// shift: remove o primeiro elemento e o retorna
// unshift: adiciona um ou mais elementos no início e retorna o novo comprimento do array
// splice: Altera o conteúdo de um array, adicionando, removendo ou substituindo elementos. Parâmetros: Índice de Início: Posição onde a alteração começa. Número de Elementos a Remover: Quantos elementos remover. Se 0, nada é removido. Elementos a Adicionar (opcional): Elementos para adicionar no local.
// slice: Retorna uma cópia superficial de uma parte de um array, selecionada desde o início até o fim (fim não incluído). O array original não é modificado. Parâmetros: Índice de Início: Posição onde a cópia começa (inclusivo). Índice de Fim (opcional): Posição onde a cópia termina (exclusivo). Se não for informado, o array é copiado até o final.
// concat: Usado para mesclar dois ou mais arrays. Este método não altera os arrays existentes, mas retorna um novo array.
// reverse: Inverte a ordem dos elementos de um array no local. O primeiro elemento se torna o último, e o último elemento se torna o primeiro.
// join: Une todos os elementos de um array em uma string e retorna esta string. É possível especificar um separador.
// sort: Ordena os elementos de um array no local e retorna o mesmo. A ordem padrão é crescente e alfabética. Para números, a ordenação converte os valores em strings, o que pode gerar resultados inesperados. Para números corretos, use uma função de comparação.
// includes: Verifica se um array contém um determinado valor de forma rápida e simples.

// Exemplos
// let frutas = ['maça','banana']
// console.log(frutas.push('laranja'))
// console.log(frutas)
// console.log(frutas.pop())
// console.log(frutas)

// console.log(frutas.shift())
// console.log(frutas)
// console.log(frutas.unshift('maça'))
// console.log(frutas)

// console.log(frutas.splice(1,0,'morango','uva'))
// console.log(frutas)

// console.log(frutas.slice(1,3))
// console.log(frutas)

// let novasFrutas = ['pera','abacaxi']
// console.log(frutas.concat(novasFrutas))
// console.log(frutas)

// console.log(frutas.reverse())

// console.log(frutas.join('; '))

// console.log(frutas.sort())

// console.log('frutas: ', frutas)
// console.log(frutas.includes('pera'))
// console.log(frutas.includes('banana'))

// Atividade 02
// Crie um array chamado animais contendo os seguintes elementos: Cachorro, Gato, Papagaio. Em seguida: 
// 1 - Adicione o elemento Tartaruga ao final do array.
// 2 - Remova o primeiro elemento e adicione o elemento Coelho no início.
// 3 - Depois, substitua o elemento na posição 2 por Hamster.
// 4 - Exiba o comprimento atual do array.
// 5 - Acesse e exiba no console o elemento na posição 1.
// 6 - Finalmente, exiba o array final no console.

// let animais = ['Cachorro','Gato','Papagaio']
// animais.push('Tartaruga')
// animais.splice(0,1,'Coelho')
// animais.splice(1,1,'Hamster')
// console.log(animais.length)
// console.log(animais[0])
// console.log(animais)

// Atividade 03
// Crie um array chamado cores contendo as seguintes cores, Vermelho, Verde, Azul. 
// 1 - Adicione as cores Amarelo e Roxo ao final do array.
// 2 - Em seguida, remova a última cor. 
// 3 - Use o método splice para remover "Verde" e adicionar "Laranja" e "Marrom" em seu lugar. 
// 4 - Crie um novo array chamado novasCores contendo as primeiras duas cores do array cores.
// 5 - Use o método join para criar uma string com todas as cores do array cores, separadas por uma vírgula.
// 6 - Inverta a ordem dos elementos no array cores.
// 7 -Exiba os arrays cores e novasCores, e a string resultante no console.

