const button = document.getElementsByTagName('button');
button[0].addEventListener('click',()=>{
const h2 = document.getElementsByTagName('h2');
const divResultados = document.getElementById('resultados');
    
let message = '';

divResultados.innerHTML = '';

fetch('https://api.brasilaberto.com/v1/states')
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

        if(!data || data.length ===0){
            message = "Base de dados vazia"
            throw new Error(message);                
        }

        divResultados.innerHTML = '';

        if(estados){
            const ufs = estados.reduce((acc,item)=>{
                if(!acc.includes(item.region)){
                    acc.push(item.region)
                }
                return acc
            },[]);

            ufs.forEach((uf)=>{
                let box = document.createElement('div');
                let titulo = document.createElement('h4');
                titulo.textContent = `Região ${uf}`;
                box.className = 'boxRegiao';
                box.classList.add(uf)
                divResultados.appendChild(box);
                box.appendChild(titulo);                
            });

            estados.forEach(estado => {
                    let item = document.createElement('p');
                    let boxRegiao = document.querySelector(`.${estado.region}`);
                    console.log("box",boxRegiao);

                    item.textContent = `Estado: ${estado.name} | UF: ${estado.shortName}`
                    boxRegiao.appendChild(item);
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