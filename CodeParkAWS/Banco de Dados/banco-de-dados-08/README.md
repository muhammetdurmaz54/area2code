# Desenvolvimento

## Instruções do projeto

Crie um banco de dados, adicione tabelas e determine quais são os atributos de cada uma. Em seguida, execute um trigger que se relacione com algum comando, como insert, select, delete ou update.

## Resposta

```
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
CREATE TABLE aviso (
id_aviso INT AUTO_INCREMENT PRIMARY KEY,
mensagem VARCHAR(100)
)
CREATE TRIGGER inserir_dados
AFTER INSERT
ON alunos FOR EACH ROW
BEGIN
IF NEW.disciplina_id IS NULL THEN
INSERT INTO aviso(id_aviso, mensagem)
VALUES
(NEW.id,CONCAT(Oi ,NEW.nome_aluno, você não possui disciplina ainda))
END IF
END
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

```