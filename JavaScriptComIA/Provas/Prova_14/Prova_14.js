
const button = document.getElementsByTagName('button');
button[0].addEventListener('click',()=>{
const h2 = document.getElementsByTagName('h2');
const divResultados = document.getElementById('resultados');
    
let message = '';

fetch('https://api.brasilaberto.com/v1/statess')
.then(response => {
    if (response.status === 404){
        message = "URL inválida"
        throw new Error(message);
    };
    return response;
})
.then(
    response => response.json()
)
.then(
    data => {
        const estados = data.result;

        if(!estados){
            message = "Base de dados vazia"
            throw new Error(message);                
        }

        if(estados){
            console.log("Dados recebidos:",estados);
            estados.forEach(estado => {
                let item = document.createElement('p');
                item.textContent = `Estado: ${estado.name} | UF: ${estado.shortName} | Região: ${estado.region}`
                divResultados.appendChild(item);
            });
        }
    }
)
.catch(error =>{
    const h3MessageError = document.createElement('h3');
    h3MessageError.textContent = `Mensagem de erro: ${error.message}`
    divResultados.appendChild(h3MessageError);
})
.finally(()=>{
    h2[0].textContent = 'Resultados da Consulta';
    }
)
})