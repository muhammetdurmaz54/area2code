# Desenvolvimento

## Instruções do projeto

Desenvolva um banco de dados e relacione tabelas através de chaves estrangeiras ou nomes de colunas iguais. Siga as instruções:
crie uma base de dados; 
crie tabelas nessa base de dados;
em cada tabela, adicione atributos;
insira dados em cada tabela;
utilize os comandos Joins para realizar consultas nas tabelas.

## Resposta
>> OBS: MariaDB
```
CREATE DATABASE BancoDeDados
USE BancoDeDados
CREATE TABLE disciplinas (
id_disciplina INT AUTO_INCREMENT PRIMARY KEY,
nome_disciplina VARCHAR(50) NOT NULL,
nome_professor VARCHAR(50) NOT NULL
)
CREATE TABLE alunos (
id_aluno INT AUTO_INCREMENT PRIMARY KEY,
nome_aluno VARCHAR(50) NOT NULL,
disciplina_id INT,
CONSTRAINT FOREIGN KEY (disciplina_id) REFERENCES disciplinas (id_disciplina)
)
INSERT INTO disciplinas(nome_disciplina, nome_professor) VALUES ('Banco de dados', 'Maria Alves')
INSERT INTO disciplinas (nome_disciplina, nome_professor) VALUES ('Python', 'Pietro Souza')
INSERT INTO disciplinas (nome_disciplina, nome_professor) VALUES ('POO', 'Bia Tavares')
INSERT INTO alunos (nome_aluno, disciplina_id) VALUES ('Cleiton', 2)
INSERT INTO alunos (nome_aluno, disciplina_id) VALUES ('Carol', NULL)
INSERT INTO alunos (nome_aluno, disciplina_id) VALUES ('Ruan', 2)
INSERT INTO alunos (nome_aluno, disciplina_id) VALUES ('Gabi', 1)
INSERT INTO alunos (nome_aluno, disciplina_id) VALUES ('Rian', NULL)
INSERT INTO alunos (nome_aluno, disciplina_id) VALUES ('Mia', 2)
INSERT INTO alunos (nome_aluno, disciplina_id) VALUES ('Malu', 1)
SELECT nome_aluno, nome_disciplina from alunos INNER JOIN disciplinas on disciplinas.id_disciplina = alunos.disciplina_id
SELECT nome_aluno, nome_disciplina from alunos LEFT JOIN disciplinas on disciplinas.id_disciplina = alunos.disciplina_id
SELECT nome_aluno, nome_disciplina from alunos RIGHT JOIN disciplinas on disciplinas.id_disciplina = alunos.disciplina_id
SELECT nome_aluno, nome_disciplina from alunos LEFT JOIN disciplinas on disciplinas.id_disciplina = alunos.disciplina_id
UNION
SELECT nome_aluno, nome_disciplina from alunos RIGHT JOIN disciplinas on disciplinas.id_disciplina = alunos.disciplina_id
```
