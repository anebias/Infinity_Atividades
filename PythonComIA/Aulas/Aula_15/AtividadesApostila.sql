'''ATIVIDADE PRÁTICA 1
Crie um banco de dados chamado "escola" e as seguintes tabelas:
Tabela "alunos" com colunas: id_aluno, nome, idade.
Tabela "cursos" com colunas: id_curso, nome_curso, carga_horaria. 
Tabela "matriculas" com colunas: id_matricula , id_aluno id_curso, data_matricula.'''

CREATE DATABASE escola;
CREATE TABLE alunos(
id_aluno INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
idade INT NOT NULL
);

CREATE TABLE cursos(
id_curso INT AUTO_INCREMENT PRIMARY KEY,
nome_curso VARCHAR(100) NOT NULL,
carga_horaria INT NOT NULL
);

CREATE TABLE matriculas(
id_matricula INT AUTO_INCREMENT PRIMARY KEY,
id_aluno INT,
id_curso INT,
data_matricula DATE NOT NULL,
FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno),
FOREIGN KEY (id_curso) REFERENCES cursos (id_curso)
);

'''ATIVIDADE PRÁTICA 2
Usando o comando TRUNCATE TABLE, exclua todos os dados da tabela "matriculas"
sem excluir a estrutura da tabela.'''

TRUNCATE TABLE matriculas;

'''ATIVIDADE PRÁTICA 3
Usando o comando DROP DATABASE, exclua o banco de dados "escola". Certifique-se de que você tenha feito um backup dos dados, pois essa ação apagará todo o banco de dados.'''

DROP DATABASE escola;

'''DESAFIO PRÁTICO
Sistema de uma escola Crie um banco de dados para um sistema de uma escola, esse banco de dados ficará responsável por persistir os dados sobre alunos, professores, turmas e disciplinas. Para os alunos é importante que contenha um número de matrícula, o nome, a idade, e o endereço.'''


'''DESAFIO PRÁTICO
Sistema de uma escola Para os professores, deverá conter um número de matrícula, nome,
especialidade e endereço. Para a turma deverá conter um identificador, horário de início e dia de semana. Para disciplina é importante que contenha um identificador, nome e quantidade de aulas.'''