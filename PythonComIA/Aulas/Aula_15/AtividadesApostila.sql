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


*** ESCRITA PARA PLAYGROUND ***
-- vai criar e apagar e abaixo recriar
CREATE TABLE matriculas(
id_matricula INT AUTO_INCREMENT PRIMARY KEY,
id_aluno INT,
id_curso INT,
data_matricula DATE NOT NULL,
FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno),
FOREIGN KEY (id_curso) REFERENCES cursos (id_curso)
);

TRUNCATE TABLE matriculas;

CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(255) NOT NULL,
    telefone VARCHAR(15) NOT NULL,
    email VARCHAR(100) UNIQUE
);

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

CREATE TABLE pedidos (
id_pedido INT PRIMARY KEY AUTO_INCREMENT,
id_cliente INT,
data_pedido DATE,
FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente)
);


CREATE TABLE produtos(
id_produto INT PRIMARY KEY AUTO_INCREMENT,
nome_produto VARCHAR(100) NOT NULL,
preco FLOAT NOT NULL,
CHECK (preco > 0)
);

INSERT INTO clientes (nome, endereco, telefone, email) VALUES ('João Pereira', 'Rua das Flores, 123', '31987654321', 'joao.pereira@example.com');
INSERT INTO clientes (nome, endereco, telefone, email) VALUES ('Maria Santos', 'Avenida Brasil, 456', '31987654322', 'maria.santos@example.com');
INSERT INTO clientes (nome, endereco, telefone, email) VALUES ('Carlos Almeida', 'Praça da Liberdade, 789', '31987654323', 'carlos.almeida@example.com');
INSERT INTO clientes (nome, endereco, telefone, email) VALUES ('Fernanda Costa', 'Rua do Sol, 101', '31987654324', 'fernanda.costa@example.com');
INSERT INTO clientes (nome, endereco, telefone, email) VALUES ('Lucas Fernandes', 'Avenida Amazonas, 202', '31987654325', 'lucas.fernandes@example.com');

INSERT INTO alunos (nome, idade) VALUES ('Ana Silva', 20);
INSERT INTO alunos (nome, idade) VALUES ('Bruno Souza', 22);
INSERT INTO alunos (nome, idade) VALUES ('Carla Mendes', 19);
INSERT INTO alunos (nome, idade) VALUES ('Daniel Oliveira', 21);
INSERT INTO alunos (nome, idade) VALUES ('Eduarda Lima', 23);

INSERT INTO cursos (nome_curso, carga_horaria) VALUES ('Matemática', 40);
INSERT INTO cursos (nome_curso, carga_horaria) VALUES ('Física', 45);
INSERT INTO cursos (nome_curso, carga_horaria) VALUES ('Química', 35);
INSERT INTO cursos (nome_curso, carga_horaria) VALUES ('Biologia', 50);
INSERT INTO cursos (nome_curso, carga_horaria) VALUES ('História', 30);

INSERT INTO matriculas (id_aluno, id_curso, data_matricula) VALUES (1, 1, '2025-04-01');
INSERT INTO matriculas (id_aluno, id_curso, data_matricula) VALUES (2, 2, '2025-04-02');
INSERT INTO matriculas (id_aluno, id_curso, data_matricula) VALUES (3, 3, '2025-04-03');
INSERT INTO matriculas (id_aluno, id_curso, data_matricula) VALUES (4, 4, '2025-04-04');
INSERT INTO matriculas (id_aluno, id_curso, data_matricula) VALUES (5, 5, '2025-04-05');

INSERT INTO pedidos (id_cliente, data_pedido) VALUES (1, '2025-04-01');
INSERT INTO pedidos (id_cliente, data_pedido) VALUES (2, '2025-04-02');
INSERT INTO pedidos (id_cliente, data_pedido) VALUES (3, '2025-04-03');
INSERT INTO pedidos (id_cliente, data_pedido) VALUES (4, '2025-04-04');
INSERT INTO pedidos (id_cliente, data_pedido) VALUES (5, '2025-04-05');

INSERT INTO produtos (nome_produto, preco) VALUES ('Notebook', 3500.00);
INSERT INTO produtos (nome_produto, preco) VALUES ('Smartphone', 2500.00);
INSERT INTO produtos (nome_produto, preco) VALUES ('Tablet', 1500.00);
INSERT INTO produtos (nome_produto, preco) VALUES ('Monitor', 800.00);
INSERT INTO produtos (nome_produto, preco) VALUES ('Teclado', 150.00);

