const inputTaskDetalhe = document.getElementById('tarefaIncluir');
        inputTaskDetalhe.addEventListener('keydown', incluirTarefa);

        const inputTaskTitulo = document.getElementById('tituloTarefa');

        inputTaskTitulo.focus();

        const ul = document.querySelector('ul');
        const footer = document.querySelector('footer');

        function incluirTarefa(event) {
            if (event.key === 'Enter') {
                const inputDetalheTask = inputTaskDetalhe.value;
                const inputTituloTask = inputTaskTitulo.value;

                if (inputDetalheTask.length < 3 || inputTituloTask.length < 3) {
                    const message = document.createElement('p');
                    message.textContent = "O título e o detalhe da tarefa precisam ter pelo menos 3 caracteres."

                    const divTarefa = document.getElementById("message");
                    divTarefa.appendChild(message);
                    divTarefa.style.display = 'block';

                    setTimeout(() => {
                        message.remove();
                    }, 1500);

                    inputTaskTitulo.focus();

                    return
                };

                const div = document.createElement('div');
                div.classList.add('ulTask');

                const divDetalheTarefa = document.createElement('div');
                div.classList.add('divDetalheTarefa');

                const checkInput = document.createElement('input');
                checkInput.setAttribute('type', 'checkbox');
                checkInput.classList.add('check-task');
                checkInput.addEventListener('change', alterarStatusTarefa);

                const titulo = document.createElement('h4');
                titulo.textContent = inputTituloTask;

                const detalheTask = document.createElement('p');
                detalheTask.textContent = inputDetalheTask;

                const buttonStatus = document.createElement('button');
                buttonStatus.textContent = 'pendente';
                buttonStatus.classList.add('btnStatus');
                buttonStatus.style.backgroundColor = 'rgb(133, 30, 35)';

                const buttonExcluir = document.createElement('button');
                buttonExcluir.textContent = 'excluir';
                buttonExcluir.setAttribute('class', 'btnExcluir');
                buttonExcluir.addEventListener('click', excluirTarefa);

                divDetalheTarefa.appendChild(titulo);
                divDetalheTarefa.appendChild(detalheTask);

                div.appendChild(checkInput);
                div.appendChild(buttonStatus);
                div.appendChild(divDetalheTarefa);
                div.appendChild(buttonExcluir);

                ul.appendChild(div);

                inputTaskDetalhe.value = '';
                inputTaskTitulo.value = '';
                setTimeout(() => {
                    inputTaskTitulo.focus();
                }, 0);
            };
            totalTarefasCadastradas();
            totalTarefasCadastradasPorTipo();
        };

        function excluirTarefa(event) {
            event.preventDefault();
            const target = event.target;
            const divPai = target.parentNode;
            divPai.remove();
            totalTarefasCadastradas();
            totalTarefasCadastradasPorTipo();
        };

        function alterarStatusTarefa(event) {
            event.preventDefault();
            const target = event.target;
            const divPai = target.parentNode;
            const tarefa = divPai.querySelector('p');
            const tituloTarefa = divPai.querySelector('h4');
            const buttonStatus = divPai.querySelector('button.btnStatus');

            if (target.checked) {
                tarefa.style.textDecoration = 'line-through';
                tituloTarefa.style.textDecoration = 'line-through';
                buttonStatus.textContent = 'concluído';
                buttonStatus.style.backgroundColor = 'rgb(7, 139, 111)';
            } else {
                tarefa.style.textDecoration = 'none';
                tituloTarefa.style.textDecoration = 'none';
                buttonStatus.textContent = 'pendente';
                buttonStatus.style.backgroundColor = 'rgb(133, 30, 35)';
            };

            totalTarefasCadastradas();
        };

        let totalTarefasCadastradas = () => {
            const totalPorStatus = totalTarefasCadastradasPorTipo();

            if (ul.childElementCount === 0) {
                footer.textContent = "Não existem tarefas cadastradas"
            } else {
                footer.textContent = `Total de tarefas cadastradas: ${ul.childElementCount} | ${totalPorStatus.concluidos} Concluídas e ${totalPorStatus.pendentes} Pendentes`
            }
        };

        let totalTarefasCadastradasPorTipo = () => {

            if (ul.childElementCount === 0) { return }

            const ulList = Array.from(ul.childNodes);

            listaConcluidos = [];
            listaPendentes = [];

            ulList.forEach(div => {
                const status = div.querySelector('.btnStatus').textContent;
                if (status === 'concluído') {
                    listaConcluidos.push(div);
                }
                else if (status === 'pendente') {
                    listaPendentes.push(div);
                }
                else { console.log('erro status') };
            });

            return { concluidos: listaConcluidos.length, pendentes: listaPendentes.length }
        };

        totalTarefasCadastradas();