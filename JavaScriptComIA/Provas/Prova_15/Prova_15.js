// A API (https://jsonplaceholder.typicode.com/) sugerida no
// exercício não tem os recursos de paginação.
// Então, escolhi a API DUMMY que dispões dos recursos para testes.

const urlBase = 'https://dummyjson.com/users';
const TIMEOUT_MS = 8000;
const button = document.querySelector('body header button');
button.addEventListener('click',carregarHTML)

async function fetchComTimeout(url, options = {}, timeout = TIMEOUT_MS) {
            const controller = new AbortController();
            const id = setTimeout(() => controller.abort(), timeout);
            try {
                const response = await fetch(url, { ...options, signal: controller.signal });
                clearTimeout(id);

                if (!response.ok) {
                    const message = `${response.status} - ${response.statusText} \nErro ao carregar os usuários, tente novamente mais tarde.`
                    throw new Error(message);
                }
                return await response.json();
            } catch (err) {
                const divMessage = document.getElementById('containerMessage');
                const pMessage = document.createElement('p');
                pMessage.textContent = `${err.name} - ${err.message}`;
                divMessage.appendChild(pMessage);

                if (err.name === 'AbortError') throw new Error('Tempo de resposta esgotado (timeout)');
                throw err;
            }
        };

function handleGETListUsers(data){
    const listUsers = data.users.map(user =>({
        nome: `${user.firstName} ${user.lastName}`,
        email: user.email
    }));
    console.log(listUsers)
    console.log('users',data.total)
    return listUsers
};

function handleRenderizarHTML(listUsers){
    // Para recarregar a página sem duplicar os registros,
    // precisa remover a OL existente para depois criar 
    // novas tags para renderizar os elementos.
    const olExistente = document.querySelector('ol');
    if(olExistente){
        console.log('estou removendo...')
        olExistente.remove();
        console.log('removido...')
    };

    const divUsers = document.getElementById('containerUsers');
    
    // criando a OL para renderizar a lista
    const ol = document.createElement('ol');

    listUsers.forEach(user => {
        const li = document.createElement('li');
        li.textContent = `${user.nome} | ${user.email}`; 
        ol.appendChild(li);
    });

    divUsers.appendChild(ol);
};
// executar ao carregar
async function carregarHTML(event){
    event.preventDefault();
    const data = await fetchComTimeout(urlBase, options = {}, timeout = TIMEOUT_MS);
    if(!data){
        console.log('data vazio')
        return}
    ;
    handleRenderizarHTML(handleGETListUsers(data));
    console.log('data final:',data)
};

