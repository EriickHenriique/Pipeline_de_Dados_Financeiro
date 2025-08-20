📌 Descrição

O API_Financeiro é um projeto em Python que coleta cotações diárias do Bitcoin, Ouro, Prata e Petróleo, integrando os dados em um banco de dados para análise e consulta posterior.

🚀 Problema Resolvido

O projeto automatiza a coleta de informações financeiras, permitindo centralizar dados de commodities e criptomoedas em uma única base estruturada. Isso elimina a necessidade de consultas manuais em diferentes fontes.

🛠️ Tecnologias Utilizadas

Linguagem: Python

Bibliotecas:

pandas → Manipulação e análise de dados

requests → Consumo de APIs (Coinbase)

time → Controle de execução e intervalos

yfinance → Coleta de dados de commodities

sqlalchemy → Integração com banco de dados

⚙️ Funcionamento

O projeto coleta os preços do Bitcoin via API da Coinbase.

Obtém os preços do Ouro, Prata e Petróleo via yfinance.

Concatena as informações coletadas.

Armazena os dados em um banco de dados para uso posterior.

📂 Estrutura do Projeto

Get_Bitcoin.py → Extrai informações do Bitcoin via API da Coinbase.

Get_Commodities.py → Obtém dados do Ouro, Prata e Petróleo usando yfinance.

GetPrices_loop_db.py → Concatena Bitcoin + Commodities e insere os dados no banco de dados.

GetPrices.py → Realiza a concatenação simples entre Bitcoin e Commodities.

🤝 Contribuição

O projeto foi inspirado em conteúdos do Luciano Vasconcelos (Jornada de Dados).
