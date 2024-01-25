# Desenvolvimento

## Instruções do projeto

Após uma varredura rápida no sistema de banco de dados de uma empresa de vendas, identificamos a necessidade de melhorar a segurança dessas informações. Por isso, será necessário desenvolver um novo banco para armazenar os dados mais importantes, como detalhes dos clientes, valores faturados diariamente e informações sobre os produtos, além de outros. Sendo assim, explique quais são os pilares da segurança de dados que devem ser seguidos para que o novo banco seja bem projetado e funcione corretamente

<hr>

<div align="center">

<b>Controle de Acesso:</b>
Implemente rigorosos controles de acesso para garantir que apenas usuários autorizados tenham permissão para acessar e modificar os dados. Isso inclui a atribuição adequada de privilégios e o uso de autenticação forte.

<b>Criptografia de Dados:</b>
Utilize criptografia para proteger dados sensíveis, tanto em repouso quanto em trânsito. Isso inclui o uso de SSL/TLS para comunicações seguras e a criptografia de dados confidenciais armazenados no banco de dados.

<b>Auditoria e Monitoramento:</b>
Implemente mecanismos de auditoria para monitorar atividades no banco de dados. Registre eventos importantes, como tentativas de acesso não autorizadas, modificações de dados e outras operações críticas. O monitoramento contínuo ajuda a identificar comportamentos suspeitos.

<b>Backup e Recuperação:</b>
Estabeleça procedimentos robustos de backup e recuperação para proteger os dados contra perda acidental, corrupção ou ataques. Regularmente teste os procedimentos de recuperação para garantir que funcionem conforme o esperado.

<b>Padrões de Senhas e Políticas de Senhas:</b>
Implemente políticas de senhas fortes e promova boas práticas de gerenciamento de senhas. Considere o uso de técnicas como hashing e salting para proteger as senhas armazenadas.

<b>Atualizações e Patches:</b>
Mantenha o sistema operacional, o sistema de gerenciamento de banco de dados (SGBD) e outros componentes de software atualizados com as últimas correções de segurança. A aplicação rápida de patches é essencial para corrigir vulnerabilidades conhecidas.

<b>Segregação de Funções:</b>
Adote o princípio da segregação de funções, garantindo que diferentes responsabilidades sejam distribuídas entre os usuários do sistema. Isso reduz o risco de abuso de privilégios.

<b>Princípio do Mínimo Privilégio:</b>
Atribua apenas os privilégios mínimos necessários para que os usuários executem suas funções. Evite conceder privilégios excessivos que não são necessários para suas responsabilidades específicas.

<b>Testes de Segurança:</b>
Realize testes regulares de segurança, incluindo testes de penetração, para identificar possíveis vulnerabilidades e corrigi-las antes que possam ser exploradas por invasores.

<b>Conformidade com Regulamentações:</b>
Garanta que o banco de dados esteja em conformidade com regulamentações de privacidade e segurança de dados aplicáveis, como o GDPR, HIPAA, ou outras normativas locais e setoriais.

</div>