// Atividade 01
// Crie um objeto chamado pessoa que contenha as seguintes propriedades:
//  - nome: Um nome à sua escolha.
//  - idade: Um número que represente a idade.
//  - cidade: O nome de uma cidade.
//  - Converta o objeto pessoa em uma string JSON usando JSON.stringify().
//   - Exiba o resultado no console.

const pessoa = {
    nome: 'Alessandra',
    idade: 51,
    cidade: 'Belo Horizonte'
};

console.log(JSON.stringify(pessoa));