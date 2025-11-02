// localStorage.clear();

const form = document.getElementById('formNotas');
const listaNotas = document.getElementById('listaNotas');

form.botaoAdicionar.addEventListener('click', incluirNota);

function incluirNota(event) {
    event.preventDefault();
    if (!form.tituloNota.value || !form.conteudoNota.value)
        {
            return alert('Campos título e conteúdo são obrigatórios !')
        } else {
            criarNota();
            listarNotas();
        }
};

function criarNota()
    {
        let notas = JSON.parse(localStorage.getItem('notas') || '{}');

        const tituloNota = form.tituloNota.value;
        const conteudoNota = form.conteudoNota.value;

        const notaExiste = tituloUnico(tituloNota, notas);

        if(notaExiste) {
                return alert('Nota já cadastrada !');
            }
        else {
            notas[tituloNota] = conteudoNota;
            localStorage.setItem('notas',JSON.stringify(notas));
        };
        
    };

function tituloUnico(titulo, notas)
{
    console.log(notas);
    return Object.keys(notas).includes(titulo);
};

function listarNotas(){
    let notas = JSON.parse(localStorage.getItem('notas') || '{}');
    listaNotas.innerHTML = "";

    const titulos = Object.keys(notas);

    if (titulos.length > 0) {
        let contador = 1;

        for( let titulo of titulos) {
            const div = document.createElement('div');
            div.setAttribute('id','nota-' + contador);
            div.classList.add('card');
            div.dataset.titulo = titulo;
            contador += 1;
            
            const ul = document.createElement('ul');
            const li = document.createElement('li');
            const tituloNota = document.createElement('h3');
            const conteudoNota = document.createElement('p');

            tituloNota.textContent = titulo;
            conteudoNota.textContent = notas[titulo];
            
            const button = document.createElement('button');
            button.textContent = "Excluir";
            button.classList.add('btnExcluir');
            button.addEventListener('click',excluirNota);

            const linha = document.createElement('hr');
            div.appendChild(tituloNota);
            div.appendChild(button);
            div.appendChild(linha);
            div.appendChild(conteudoNota);
            li.appendChild(div);
            ul.appendChild(li);

            listaNotas.appendChild(div);
        }

    } else {
        const h3 = document.createElement('h3');
        h3.textContent = "Não existem notas cadastradas !"
        listaNotas.appendChild(h3);
    }
};

function excluirNota(event){
    const button = event.target;

    // closest('.card') para buscar o ancestral mais próximo
    const divNota = button.closest('.card');
    const titulo = divNota.dataset.titulo;

    console.log('ID da div: ', divNota.id);
    console.log('Título da nota: ', divNota.dataset.titulo);

    const notas = JSON.parse(localStorage.getItem('notas') || '{}');

    delete notas[titulo];

    localStorage.setItem('notas',JSON.stringify(notas));

    divNota.remove();

    listarNotas()
};

listarNotas();