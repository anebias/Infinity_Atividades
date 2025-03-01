const fs = require('fs');

const conteudo = "Este é o novo conteúdo";

fs.writeFile('novoArquivo.txt', conteudo, (err) => {
if (err){console.error('Erro ao escrever no arquivo: ',err);
    return;
}{console.log('Arquivo escrito com sucesso')};

})