// Ex01. Crie um objeto "Carro" que deve conter as propriedades "marca", "modelo", "ano" e "cor"

// a) Mostre no console a marca e o modelo do carro
// b) Mostre no console a cor do carro
// c) Altere o valor da cor do carro (e mostre novamente)
// d) Adicione uma nova propriedade chamada "km" que terá a kilometragem do carro

let carro = {
    marca: "Honda",
    modelo: "HRV",
    ano: 2025,
    cor: "grafite"
}

console.log(carro)
console.log(carro['marca'], carro.modelo)

carro['cor'] = 'branco'

console.log(carro.cor)

carro.km = 0

console.log(carro)