// Tratamento de erros
// // TRY ... CATCH
// A estrutura try...catch é utilizada para envolver um bloco de código que pode gerar erros ou exceções. Se uma exceção ocorrer dentro do bloco try, o fluxo de execução é imediatamente transferido para o bloco catch, onde você pode lidar com a exceção de forma apropriada.

// // let nome = null; (teste que executa com erro)
// // let nome = "gustavo"; (teste que executa com sucesso)
// try {
//     console.log(nome.toUpperCase());
// } catch (error)
// {
//     console.error("Ocorreu um erro: ",error.message);
// };

// FINALLY
// Além do try e catch, o JavaScript oferece o bloco finally. Essa cláusula é opcional e serve para definir um trecho de código que sempre será executado, independentemente de ocorrer ou não uma exceção dentro do bloco try.

function dividir(numerador, denominador) {
    try {
        if(denominador === 0){
            throw new Error("Divisão por zero.");
        }
        return numerador / denominador;
    } catch (error) {
        console.error("error: ", error.message);
    } finally {
        console.log("Operação de divisão finalizada.");
    }
};

// console.log('2 e 0',dividir(2,0));
// console.log('2 e 4',dividir(2,4));
// console.log('-5 e 3',dividir(-5,3));
// console.log('0 e 2',dividir(0,2));
// console.log('null e 2',dividir(null,0));
// console.log('"2" e 2',dividir("2",2));


