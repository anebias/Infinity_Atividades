const button = document.getElementsByTagName('button');
button[0].addEventListener('click',()=>{
    console.log('aqui')
    fetch('https://api.brasilaberto.com/v1/states')
    .then(
        response => response.json()
    )
    .then(
        data => {
            const estados = data.result;
            if(estados){
                
                console.log("Dados recebidos:",estados);
                const divResultados = document.getElementById('resultados');
                estados.forEach(estado => {
                    let item = document.createElement('p');
                    item.textContent = `Estado: ${estado.name} | UF: ${estado.shortName} | Região: ${estado.region}`
                    divResultados.appendChild(item);
                });
            }
        }
    )
    .catch(error =>{
        console.error("message error: ",error);
    })
    .finally(()=>{
        const h2 = document.getElementsByTagName('h2');
        h2[0].textContent = 'Resultados da Consulta';
        }
    )
})