const button = document.getElementById('btnCadastrar');
button.addEventListener('click',handleCadastrar);

function handleCadastrar(event){
    event.preventDefault();
    const formularioCadastro = document.getElementById('formCadastro');
    let message = '';
    let classe = '';

    const mensagensAnteriores = formularioCadastro.querySelectorAll('.error-message');
    
    mensagensAnteriores.forEach(mensagem => mensagem.remove());

    try {        
        if(formularioCadastro.name.value.length < 3){
            message = "O nome precisa ter pelo menos 3 caracteres";
            classe = "name";
            throw new Error(message);
        };

        if(formularioCadastro.user.value.length < 3){
            message = "Usuário inválido (precisa ter pelo menos 3 caracteres)";
            classe = "user";
            throw new Error(message);
        }

        if(formularioCadastro.password.value.length < 3){
            message = "Senha inválida (precisa ter pelo menos 3 caracteres)";
            classe = "password";
            throw new Error(message);
        }

        // a@b.com
        if(! (formularioCadastro.email.value.includes("@") && formularioCadastro.email.value.includes(".")) || formularioCadastro.email.value.length < 7){
            message = "Email inválido!"
            classe = "email";
            throw new Error(message);
        }

        if(Number(formularioCadastro.age.value) < 18){
            message = "Cadastro não permitido para menores de 18 anos";
            classe = "age";
            throw new Error(message);
        }

        if(! formularioCadastro.dateOfBirth.value) {
            message = "Data de nascimento é obrigatória";
            classe = "dateOfBirth";
            throw new Error(message);
        }
        
        const dataNascimento = new Date(formularioCadastro.dateOfBirth.value);
        const dataAtual = new Date();

        if(dataNascimento > dataAtual) {
            message = "Data inválida (não pode ser futura)";
            classe = "dateOfBirth"
            throw new Error(message);
        }

        console.log("Cadastro realizado com sucesso !")

    } catch (error) {
        const pMessageError = document.createElement('p');
        pMessageError.className = 'error-message';
        pMessageError.style.display = "none";
        const divClasse = document.getElementsByClassName(classe);

        if(divClasse.length > 0){
            const divPai = divClasse[0];
            pMessageError.style.display = "block";
            pMessageError.textContent = message;
            divPai.appendChild(pMessageError);
            console.log("último elemento da div -> ",divPai);
        };
        console.log(error.message)
    } finally {
        console.log("Cadastramento encerrado")}
};
