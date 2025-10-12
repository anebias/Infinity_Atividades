var numeroTarefaCadastrada = 1;

function adicionarTarefa(){

    let ulList = document.getElementById('ulList');

    let input = document.getElementById('inputTarefa')

    let novaTarefa = input.value;

    if(novaTarefa === "") { return }

    let liList = document.createElement('li');
    liList.setAttribute('id',`liList${numeroTarefaCadastrada}`)

    let itemList = document.createElement('a');
    itemList.textContent = novaTarefa;
    itemList.setAttribute('onclick',`concluirTarefa('liList${numeroTarefaCadastrada}')`);

    let buttonExcluir = document.createElement('button');
    buttonExcluir.setAttribute('onclick',`removerTarefa('liList${numeroTarefaCadastrada}')`);
    buttonExcluir.textContent = "Excluir Tarefa " + numeroTarefaCadastrada;
    buttonExcluir.classList.add('buttonExcluir');

    liList.appendChild(itemList);
    liList.appendChild(buttonExcluir);
    ulList.appendChild(liList);

    input.value = "";

    numeroTarefaCadastrada += 1;
};

function removerTarefa(id){
    const li = document.getElementById(id);
    ulList.removeChild(li);
};

function concluirTarefa(id){
    const li = document.getElementById(id);
    li.classList.add('concluido');
};


