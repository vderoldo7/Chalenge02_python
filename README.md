# AIDA - Assistente Virtual de Saúde

## 📌 Sobre o projeto

O projeto **AIDA - Assistente Virtual de Saúde** é um sistema desenvolvido em Python com o objetivo de simular uma assistente digital voltada para a área da saúde.

A proposta do programa é facilitar o acesso do paciente a funcionalidades básicas de atendimento, como cadastro, marcação de consultas, visualização de exames e envio de mensagens ao médico.

O sistema funciona por meio de um menu interativo no terminal, permitindo que o usuário escolha diferentes opções de acordo com sua necessidade.

Este projeto foi desenvolvido como parte de uma atividade acadêmica, com foco em lógica de programação, uso de funções, listas, dicionários, estruturas condicionais, laços de repetição e tratamento de erros.

---

## 👥 Integrantes do grupo

- Álvaro Freitas Miranda — RM: 565364
- Rafael Pascotte Mercadante — RM: 564928
- Vitor Viana Carneiro Deroldo — RM: 565537

---

## 🎯 Objetivo do projeto

O objetivo principal do projeto é criar uma solução simples e funcional que represente uma assistente virtual para pacientes, ajudando pessoas a realizarem tarefas relacionadas ao atendimento médico de forma mais prática.

A AIDA permite que o usuário:

- Cadastre informações de pacientes;
- Marque consultas;
- Liste consultas agendadas;
- Altere informações de consultas;
- Cancele consultas;
- Visualize resultados de exames fictícios;
- Envie mensagens ao médico.

---

## 🧠 Contexto da solução

Muitas pessoas possuem dificuldades para acessar serviços digitais de saúde, principalmente quando precisam marcar consultas, verificar exames ou se comunicar com profissionais médicos.

Pensando nisso, a AIDA foi criada como uma assistente simples e acessível, que organiza essas funcionalidades em um sistema de menu direto e fácil de usar.

Mesmo sendo uma versão inicial executada no terminal, o projeto representa uma base para uma futura plataforma mais completa, podendo evoluir para um sistema com interface gráfica, banco de dados e integração com serviços reais de saúde.

---

## ⚙️ Funcionalidades do sistema

### 1. Área de consultas

Na área de consultas, o usuário pode:

- Marcar uma nova consulta;
- Listar todas as consultas registradas;
- Alterar uma consulta existente;
- Cancelar uma consulta.

As consultas são armazenadas em uma lista de dicionários durante a execução do programa.

---

### 2. Visualização de exames

O sistema permite visualizar um exame fictício de um paciente.

Atualmente, o projeto possui um exemplo de exame do tipo **Hemograma**, contendo informações como:

- Tipo do exame;
- Data do exame;
- Resultado da hemoglobina;
- Resultado dos leucócitos;
- Resultado das plaquetas.

Essa funcionalidade simula a consulta de exames médicos dentro da assistente.

---

### 3. Envio de mensagem ao médico

O usuário pode escrever uma ou mais mensagens ao médico.

As mensagens são armazenadas em uma lista durante a execução do programa e exibidas logo após o envio.

Essa funcionalidade simula uma comunicação simples entre paciente e médico.

---

### 4. Cadastro do paciente

Na área de cadastro, o usuário pode:

- Cadastrar um novo paciente;
- Visualizar os dados cadastrados;
- Alterar informações do cadastro;
- Remover um cadastro.

As informações cadastradas incluem:

- Nome;
- Data de nascimento;
- Idade;
- Sexo;
- CPF;
- Telefone;
- E-mail;
- Endereço.

---

## 🛠️ Tecnologias utilizadas

O projeto foi desenvolvido utilizando:

- Python 3;
- Estruturas condicionais;
- Laços de repetição;
- Funções;
- Listas;
- Dicionários;
- Tratamento de exceções com `try`, `except`;
- Execução via terminal.

---

## 📂 Estrutura do projeto

```text
AIDA/
│
├── main.py
└── README.md
Descrição dos arquivos
main.py: arquivo principal do projeto, contendo todas as funções e o menu de execução do sistema.
README.md: arquivo de documentação do projeto.
▶️ Como executar o projeto

Para executar o projeto, é necessário ter o Python instalado na máquina.

Passo 1: Clone ou baixe o projeto

Caso esteja usando GitHub, clone o repositório:

git clone URL_DO_REPOSITORIO

Ou baixe o arquivo .zip do projeto e extraia em uma pasta.

Passo 2: Acesse a pasta do projeto
cd nome-da-pasta-do-projeto
Passo 3: Execute o arquivo Python
python main.py

Ou, dependendo da instalação do Python:

python3 main.py
🖥️ Como usar o sistema

Ao iniciar o programa, será exibido o menu principal:

| AIDA - Assistente |
Como posso ajudar?

1 - Área de consultas
2 - Ver resultados de exames
3 - Enviar uma mensagem ao médico
4 - Cadastro do paciente
0 - Sair

O usuário deve digitar o número correspondente à opção desejada.

📋 Menus do sistema
Menu principal
1 - Área de consultas
2 - Ver resultados de exames
3 - Enviar uma mensagem ao médico
4 - Cadastro do paciente
0 - Sair
Menu da área de consultas
1 - Marcar nova consulta
2 - Listar consultas
3 - Alterar consulta
4 - Cancelar consulta
0 - Voltar
Menu da área de cadastro
1 - Cadastrar paciente
2 - Informações do cadastro
3 - Alterar informações
4 - Cancelar cadastro
0 - Voltar
🧩 Principais funções do projeto
ver_exame(te, nome_paciente)

Exibe os exames de um paciente específico, buscando as informações dentro de uma lista de exames.

mensagem(m)

Permite que o usuário envie uma ou mais mensagens ao médico, armazenando essas mensagens em uma lista.

registra_consulta(c)

Recebe os dados de uma consulta, como hora, dia e mês, e armazena essas informações em um dicionário.

add_tab(t, c)

Adiciona uma cópia de um dicionário dentro de uma lista, simulando uma tabela de registros.

lista_consulta(t)

Lista todas as consultas cadastradas no sistema.

remove_consulta(t)

Permite cancelar uma consulta cadastrada, removendo-a da lista.

alterar_consulta(t)

Permite alterar os dados de uma consulta existente, como dia, mês e horário.

cria_paciente(p)

Cadastra as informações de um paciente em um dicionário.

listar_paciente(t)

Exibe todos os pacientes cadastrados no sistema.

altera_cadastro(t)

Permite alterar uma informação específica do cadastro do paciente.

remove_cadastro(t)

Remove um cadastro de paciente da lista.

menu()

Função principal do programa. Ela exibe o menu inicial e controla a navegação entre as funcionalidades do sistema.

🗃️ Estruturas de dados utilizadas

O projeto utiliza principalmente listas e dicionários para armazenar os dados temporariamente.

Exemplo de dicionário de paciente
paciente = {
    "Nome": "",
    "Data de nascimento": "",
    "Idade": 0,
    "Sexo": "",
    "CPF": "",
    "Telefone": "",
    "Email": "",
    "Endereço": ""
}
Exemplo de dicionário de consulta
consulta = {
    "Hora": 0.0,
    "Dia": 0,
    "Mês": 0,
    "Ano": 2025
}
Exemplo de dicionário de exame
exame = {
    "id": 1,
    "paciente": "Paciente01",
    "tipo": "Hemograma",
    "data": "12/09/2025",
    "resultado": {
        "Hemoglobina": "14 g/dL",
        "Leucócitos": "7000 /mm³",
        "Plaquetas": "250000 /mm³"
    }
}
⚠️ Tratamento de erros

O sistema possui tratamento de erros utilizando try e except.

Alguns erros tratados no projeto são:

Entrada de letras onde deveriam ser digitados números;
Índices inválidos ao remover consultas ou cadastros;
Chaves inexistentes em dicionários;
Erros inesperados durante a execução.

Isso ajuda a evitar que o programa seja encerrado bruscamente caso o usuário digite alguma informação incorreta.

💾 Armazenamento dos dados

Nesta versão, os dados são armazenados apenas em memória, utilizando listas e dicionários.

Isso significa que, ao encerrar o programa, as informações cadastradas são perdidas.

Em versões futuras, o sistema pode ser integrado a um banco de dados para salvar os dados de forma permanente.

🚀 Possíveis melhorias futuras

Algumas melhorias que podem ser feitas no projeto são:

Adicionar banco de dados para armazenar pacientes, consultas, exames e mensagens;
Criar uma interface gráfica ou versão web;
Implementar login de usuário;
Criar validação de CPF, telefone e e-mail;
Permitir cadastro de vários exames por paciente;
Permitir escolha de especialidade médica;
Adicionar confirmação de consulta;
Criar relatórios de consultas e pacientes;
Melhorar a organização do código em arquivos separados;
Integrar o sistema com uma API externa.
✅ Conclusão

O projeto AIDA - Assistente Virtual de Saúde representa uma solução inicial para facilitar o acesso de pacientes a serviços básicos de saúde.

Por meio de um menu simples no terminal, o sistema permite cadastrar pacientes, marcar consultas, visualizar exames e enviar mensagens ao médico.

Além disso, o projeto reforça conceitos importantes de programação em Python, como funções, listas, dicionários, estruturas de repetição, condicionais e tratamento de exceções.

📄 Licença

Este projeto foi desenvolvido para fins acadêmicos.
