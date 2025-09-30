// [JSIA-A08]  Explique o que são objetos literais em JavaScript e mostre um exemplo prático de um objeto chamado aluno, que contenha as seguintes propriedades e métodos:

// nome (string)
// notas (array de números)
// calcularMedia() (método que retorna a média das notas)
// Além disso, utilize a desestruturação para acessar o nome do aluno, e o spread operator para adicionar uma nova nota ao array original.

// Resposta: Uma abstração de objetos reais. São estruturas que permitem armazenar "chave" e "valor" entre chaves, iteráveis e que permitem acessar seu valores internos. As chaves são normalmente usadas para designar propriedades do objeto abstraído. 

// Exemplo:
let aluno = {nome:"Maria Joaquina", notas:[10,8.4,9.6,9.3,8.9]};

// Testei com reduce e está dando 46.199999999999996 9.239999999999998. Por que?

// function calcularMedia(){
//     aluno.notas = [...aluno.notas, 10];
//     console.log(aluno);
//     const soma = aluno.notas.reduce((acc,nota)=>acc+nota,0);
//     const media = soma / aluno.notas.length;
//     console.log(soma.toFixed(2).replace('.',','),media.toFixed(2).replace('.',','));

//     let { nome } = aluno;
//     console.log(`O aluno ${nome} obteve média ${media.toFixed(2).replace('.',',')}`);
//     };

// Testei com o for e o resultado apresentado, apesar de não estar preciso, foi o mesmo: 46.199999999999996 9.239999999999998. Por que?

function calcularMedia(){
    let soma = 0;
    aluno.notas = [...aluno.notas, 10];
    console.log(aluno);

    for (nota of aluno.notas) {
        soma += nota;
    }
    const media = soma / aluno.notas.length;
    console.log(soma.toFixed(2).replace('.',','),media.toFixed(2).replace('.',','));
    
    let { nome } = aluno;
    console.log(`O aluno ${nome} obteve média ${media.toFixed(2).replace('.',',')}`);
};

calcularMedia();
