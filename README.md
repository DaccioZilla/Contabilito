# Contabilito

# Experimentação de Conceitos de Domain Driven Design (DDD) e Design Patterns em Contabilidade

Em certo sentido, a Contabilidade pode ser considerada como uma linguagem: um modo de mensurar e codificar informação Econômico-Financeira de uma entidade, a fim de que diversas partes interessadas sejam capazes de tomar decisão a partir das informações catalogadas.

Recentemente, tenho lido alguma coisas sobre DDD e Design Patterns que tem me feito refletir sobre como formas parecidas de estruturar trabalho e pensamento poderiam ser utilizados na Contabilidade. Trabalhei que alguns ERP monolíticos, em que transações diversas eram parametrizadas em árvores de configurações complexas que deveriam dar conta de uma enorme variedade de assuntos diferentes, e.g: movimentação de estoque, reflexos nos módulos financeiros, contabilização, etc.

Embora aí exista certa modularidade, tudo é muito acoplado e rígido. Não é difícil imaginar esses grandes monolitos de ERP como Bounded Contexts menores, cada um com uma responsabilidade bem definida, com conhecimento de Domínio isolado, e que se comunicam com outros Contextos no Downstream, estando a Contabilidade bem abaixo no fluxo.

Adicionalmente, um lançamento contábil per si é algo relativamente simples. O lançamento contábil mais simples poderia ser descrito como um registro que contenha:

- Data;
- Descrição na forma de um breve histórico;
- Duas contas;
- Valor

No caso da contabilidade, uma conta é uma marcação qualitativa no evento econômico, que possua certa constância através do tempo para que eventos econômicos sejam comparáveis, e se tenha uma idéia do desenrolar do Desempenho Ecônomico da Entidade e do avanço do Patrimônio. Duas contas são necessárias para o lançamento contábil, pois a boa e consagrada técnica contábil adota uma perpectiva dupla (Débito/Crédito) para cada evento.

Os lançamentos são o átomo da contabilidade, e dão origem a reportes detalhados sob determinada perspectiva (Diário, Razão) e agregados (Balanço, Demonstração de Resultados).

Além disso, é esperado que determinados lançamentos sejam frequentes o bastante para que possam ser implementados como um Padrão. Por exemplo, uma compra de mercadoria para revenda pode ser tratada sempre como um Débito na conta de Estoque, e um Crédito na conta de Fornecedores. O pagamento dessa compra (mesmo A vista) pode tratada como um evento separado, que pode ser tratado sempre como um Débito de Fornecedor e um Crédito de Disponibilidades. Ainda, as contas contábeis e históricos podem ser mantidas o mais simples o possível, mas detalhamento adicional poderia ser obtido upstream, em referência ao evento que enseja a contabilização.

Então, esta é uma experimentação sobre como a Contabilidade, tratada como um Domínio, poderia ser implementada como um componente de um sistema distibuído, que recebe eventos de outros módulos hipotéticos desse sistema e realiza o registro contábil correspondente. Os Eventos que esse módulo recebe, a princípio, são:

- Compra de Mercadoria para Revenda.
- Compra de Ativo Imobilizados.
- Compra de Serviço/Material de Consumo.
- Venda de Mercadoria
- Pagamentos de Compras.
- Recebimentos de Vendas.
- Pagamentos/Recebimentos não relacionados com Compras e Vendas (Aporte de Sócios, Investimentos, Folha de Salários, Empréstimos)

Esses eventos serão tratados de maneira padronizada. Ao longo do tempo, mais padrões podem ser adicionados.

Partimos do princípio que esses eventos são disparados de maneira acordada com os Domínios de Origem, e são abstraídos por uma interfaze bem definida. Nesse momento não no interessa a implementação interna desses domínios, e nem possíveis relações entre eles (e.g, a relação entre o Domínio FInanceiro, que faz pagamentos e recebimentos, com os Domínios de Compras e Vendas).

Outra premissa é que o Plano de Contas deve ser o mais simples o possível. Portanto, haverá apenas uma conta de Estoque, assim como para Cliente, Fornecedor, Disponibilidades, etc. O objetivo da Conta Contábil é fornecer a classificação contábil mais bruta do lançamento. Porém, cada lançamento contábil deverá guardar um objeto com o conteúdo da mensagem disparada pelo domínio no upstream, de modo que seja possível realizar drilldown e realizar análises mais detalhadas de uma conta, e ainda assim a generalização seja possível.

Por último, um disclaimer: não pretendemos dizer aqui que toda contabilização é fácil e tudo que concerne à contabilidade pode ser automatizado. A Contabilidade lida com desafios de mensuração e reavaliação que são espinhosos para dizer o mínimo. Aqui dizemos apenas: há uma parte que é simples o bastante para ser padronizada, sem prejuízos ao reporte e análise. Então, por que não?

O Domínio Contábil deve conter:

- As Contas.
- Um repositório de Contas.
- Um mapa entre os Eventos recebidos e os Lançamentos Contábeis que devem ser executados.
- Um repositório de Lançamentos Contábeis.

Também fará parte do Domínio as Demonstrações Financeiras:
- Balanço Patrimonial
- Demonstração do Resuntado

As Demonstrações Financeiras são responsáveis por organizar as contas em uma estrutura hierárquica que lhe são caractéristicas.

POr enquanto é só...

