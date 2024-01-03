# Desenvolvimento

## Instruções do projeto

De acordo com os conceitos estudados, exiba os resultados das consultas das operações select, project, união, intersecção e diferença. Siga as instruções com base na tabela apresentada em anexo.

- Mostre as informações apenas dos alunos aprovados. A aprovação é acima de 7,0;
- Exiba as informações dos alunos do primeiro ano com nota maior ou igual a 8,0;
- Exiba apenas os nomes e as notas dos alunos;
- Crie uma tabela PROFESSOR que apresente apenas o primeiro e o último nome do professor;
- Crie uma tabela ALUNO com o primeiro e o último nome de cada;
- Mostre o resultado da união entre a tabela ALUNO(PNome, UNome) e a tabela PROFESSOR;
- Exiba o resultado da intersecção entre a tabela ALUNO(PNome, UNome) e a tabela PROFESSOR;
- Exiba o resultado da diferença entre a tabela ALUNO(PNome, UNome) e a tabela PROFESSOR. 

![tabela-de-dados](Imagem01_Atividade04_BancoDeDadosI.png)

1. Mostre as informações apenas dos alunos aprovados. A aprovação é acima de 7,0;

|P.NOME|U.NOME|MATRÍCULA|SÉRIE|DISCIPLINA|NOTA
|---|---|---|---|---|---
|Luiz|Silva|6215|1º ano|Português|8,0
|André|Carvalho|4521|3º ano|Matemática|9,5
|Alan|Vilela|3285|1º ano|História|9,5
|Figueiredo|Santos|4598|2º ano|Geografia|9,0

2. Exiba as informações dos alunos do primeiro ano com nota maior ou igual a 8,0;

|P.NOME|U.NOME|MATRÍCULA|SÉRIE|DISCIPLINA|NOTA
|---|---|---|---|---|---
|Luiz|Silva|6215|1º ano|Português|8,0
|Alan|Vilela|3285|1º ano|História|9,5

3. Exiba apenas os nomes e as notas dos alunos;

|P.NOME|NOTA
|---|---
|Vitória|7,0
|Luiz|8,0
|André|9,5
|Alan|9,5
|Figueiredo|9,0

4. Crie uma tabela PROFESSOR que apresente apenas o primeiro e o último nome do professor;

|PROFESSOR||
|---|---
|P.NOME|U.NOME
|Alvaro|Neto
|Alan|Vilela

5. Crie uma tabela ALUNO com o primeiro e o último nome de cada;

|ALUNO||
|---|---
|P.NOME|U.NOME
|Vitória|Claudino
|Luiz|Silva
|André|Carvalho
|Alan|Vilela
|Figueiredo|Santos


6. Mostre o resultado da união entre a tabela ALUNO(PNome, UNome) e a tabela PROFESSOR;

|PROFESSOR U ALUNO||
|---|---
|P.NOME|U.NOME
|Alvaro|Neto
|Vitória|Claudino
|Alan|Vilela
|Luiz|Silva
|André|Carvalho
|Alan|Vilela
|Figueiredo|Santos

7. Exiba o resultado da intersecção entre a tabela ALUNO(PNome, UNome) e a tabela PROFESSOR;

|PROFESSOR ∩  ALUNO||
|---|---
|P.NOME|U.NOME
|Alan|Vilela

8. Exiba o resultado da diferença entre a tabela ALUNO(PNome, UNome) e a tabela PROFESSOR;

|PROFESSOR ≠ ALUNO||
|---|---
|P.NOME|U.NOME
|Alvaro|Neto
|Vitória|Claudino
|Luiz|Silva
|André|Carvalho
|Figueiredo|Santos