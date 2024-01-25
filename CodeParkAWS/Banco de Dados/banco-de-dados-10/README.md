# Desenvolvimento

## Instruções do projeto

Uma loja tem um banco de dados que contém todo o controle de vendas de produtos e de cadastro de clientes. Pensando nisso, crie uma função para somar todos os clientes que foram cadastrados na loja durante um dia.

~~~sql
CREATE FUNCTION SomarClientesCadastrados(dataCadastro DATE)
RETURNS INT
BEGIN
    DECLARE totalClientes INT;
    SELECT COUNT(*) INTO totalClientes
    FROM Clientes
    WHERE DATE(dataCadastro) = DATE(dataCadastro);
    RETURN totalClientes;
END;
SELECT SomarClientesCadastrados('2024-01-16') AS TotalClientesCadastrados;
~~~