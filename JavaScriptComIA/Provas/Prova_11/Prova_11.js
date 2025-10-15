const formCadastro = document.getElementById('formulario');
formCadastro.addEventListener('submit',handleEnviarFormulario);

const olContainer = document.getElementById('olContainer');

const contador = olContainer.childElementCount;

const buttonReset = document.getElementById('reset');
buttonReset.addEventListener('click',()=>{
    olContainer.innerHTML = "";
});

function handleEnviarFormulario(event){
    console.log(contador);
    event.preventDefault();
    console.log("prevenido");

    if (formCadastro.nome.value === ''
        || formCadastro.senha.value === ''
        || formCadastro.telefone.value === ''
        || formCadastro.nascimento.value === ''
        || formCadastro.email.value === ''
    ){return console.log('Algum campo vazio. Preencha todos os campos para enviar o formulário.')}

    const cadastro = {
        nome: formCadastro.nome.value,
        senha: formCadastro.senha.value,
        telefone: formCadastro.telefone.value,
        nascimento: formCadastro.nascimento.value,
        email: formCadastro.email.value,
    }

    const liList = document.createElement('li');

    liList.textContent = `Nome: ${cadastro.nome} | Telefone: ${cadastro.telefone} | Nascimento: ${cadastro.nascimento} | E-mail: ${cadastro.email}`

    olContainer.appendChild(liList);
};