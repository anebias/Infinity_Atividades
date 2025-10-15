funcoes1.js

// Funções (Revisão)
// Uma função é uma ação onde nós definimos entrada, processamento e saída

// Assinatura da Função
// function <nomeFunção>(<parametros>...) {
//      <codigo da funcao>
// }

/**
 * Mostra uma saudação no console para uma pessoa
 * @param {string} nome - Nome da pessoa
 * @param {string} sobrenome - Sobrenome da pessoa (Opcional)
 * @returns {void}
 */
function mostrarSaudacao(nome, sobrenome = '') {
    console.log(`Olá ${nome} ${sobrenome}`)
}

mostrarSaudacao('Alessandra')
mostrarSaudacao('Usuário', 'Infinity')

--------------------------------------------------------------------------------------------------------------------
funcoes2.js
// Retornos de Função

// Ao retornar um valor em uma função, esse valor vai substituir o local da chamada da função.
function calcularImc(peso, altura) {
    const imc = peso / (altura * altura)
    return imc
}

// Armazenando o retorno da função em uma variavel
const variavel = calcularImc(75, 1.71)
console.log(variavel)

// Passando o retorno da função como parametro para outra função
console.log(calcularImc(85, 1.67))

--------------------------------------------------------------------------------------------------------------------

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1> Cadastre seu Carro </h1>
    <input type="text" id="marca" placeholder="Marca do carro"> <br>
    <input type="text" id="modelo" placeholder="Modelo do carro"> <br>
    <button onclick="handleCadastrarCarro()"> Cadastrar </button>

    <div id="resultado"></div>

    <script>
        function handleCadastrarCarro() {
            const carro = {
                marca: document.getElementById('marca').value,
                modelo: document.getElementById('modelo').value
            }

            const resultado = document.getElementById('resultado')
            resultado.innerText = `Carro ${carro.marca} ${carro.modelo} cadastrado com sucesso.`
        }
        
        // function handleCadastrarCarro() {
        //     const inputMarca = document.getElementById('marca')
        //     const marca = inputMarca.value
            
        //     const inputModelo = document.getElementById('modelo')
        //     const modelo = inputModelo.value
            
        //     console.log(`Marca: ${marca}`)
        //     console.log(`Modelo: ${modelo}`)
        // }
    </script>
</body>
</html>