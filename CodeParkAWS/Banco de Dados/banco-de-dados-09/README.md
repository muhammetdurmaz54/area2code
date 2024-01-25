# Desenvolvimento

## Instruções do projeto

Uma empresa de vendas tem um banco de dados com informações sobre os seus produtos. Ela precisa criar um relatório que faça um levantamento diário da quantidade de produtos comprados por dia. Para ajudar a empresa, crie um procedure para agilizar esse processo.

~~~sql
CREATE PROCEDURE LevantamentoDiarioProdutos()
BEGIN
    CREATE TEMPORARY TABLE TempLevantamentoDiario (
        Data DATE,
        TotalProdutosComprados INT
    );
    INSERT INTO TempLevantamentoDiario (Data, TotalProdutosComprados)
    SELECT Data, SUM(Quantidade) AS TotalProdutosComprados
    FROM Vendas
    GROUP BY Data;
    SELECT * FROM TempLevantamentoDiario;
    DROP TEMPORARY TABLE IF EXISTS TempLevantamentoDiario;
END
~~~