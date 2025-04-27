# PainelTI - Documentação

## Visão Geral

O **PainelTI** é um sistema de gerenciamento de chamados e patrimônio voltado para a gestão de TI. Ele inclui funcionalidades como:

- Gerenciamento de chamados.
- Inventário de patrimônio (computadores, nobreaks, thin clients).
- Cadastro de impressoras e outros dispositivos.
- Relatórios detalhados sobre as atividades da equipe de TI.

---

## Estrutura do Projeto

O sistema foi desenvolvido utilizando **Django**, com as seguintes características principais:

- **Banco de Dados**: SQLite.
- **Python**: Ambiente virtual `venv`.
- **Front-end**: HTML e CSS customizados, utilizando as fontes `EB Garamond` e `Kanit`.
- **Apps Principais**:
  - **Dashboard**: Relatórios e configurações gerais.
  - **Chamados**: Gerenciamento de chamados.
  - **Utilitários**: Cadastro de dispositivos como impressoras e thin clients.
  - **Ping**: Monitoramento de redes.

---

## Funcionalidades

### Chamados

- **Cadastro**: Criação de chamados com informações como título, departamento, local, descrição e contato.
- **Fechamento**: Formulário adicional no encerramento do chamado, com campos obrigatórios como número de patrimônio, descrição técnica e solução.
- **Status**: Gerenciamento do status (Aberto, Em Andamento, Encerrado).
- **Relatórios**: Geração de relatórios filtrados por data, técnico responsável e status.
- **Grupos de Usuários**: Controle de permissões para operadores, técnicos e administradores.

### Patrimônios

- **Cadastro**: Itens como computadores, nobreaks e thin clients, com informações detalhadas (número de patrimônio, marca, tipo, local, setor, entre outros).
- **Especificações de Computadores**: Informações adicionais como IP, memória RAM, HD, processador e placa de vídeo.
- **Thin Clients**: Cadastro com informações como usuário, senha, número do monitor e local.

### Impressoras

- **Cadastro e Edição**: Registro de impressoras com IP, número do equipamento, modelo e local.

### Inventário de TI

- **Automatização**: Envio de informações de hardware como nome, IP, memória, HD, processador e placa de vídeo para o servidor.

---

## Arquitetura do Sistema

O sistema está estruturado em diferentes aplicativos dentro do projeto Django:

- **Dashboard**: Gerenciamento de configurações e geração de relatórios.
- **Chamados**: Funcionalidades relacionadas a chamados.
- **Utilitários**: Cadastro e gerenciamento de dispositivos.
- **Ping**: Monitoramento de redes.

### Modelos de Dados

#### Chamado

- **titulo**: Título do chamado.
- **departamento**: Departamento relacionado.
- **local**: Local do chamado.
- **contato**: Informações de contato.
- **descricao**: Descrição detalhada.
- **status**: Status (Aberto, Em Andamento, Encerrado).
- **data_criacao**: Data de criação.
- **data_atualizacao**: Última atualização.

#### Patrimônio

- **numero_patrimonio**: Número único de patrimônio.
- **marca**: Marca do item.
- **tipo**: Tipo do item (computador, nobreak, etc.).
- **local**: Local onde o patrimônio está alocado.
- **departamento**: Departamento ao qual pertence.
- **obs**: Observações gerais.
- **Computadores**:
  - **ip**: IP do computador.
  - **memoria_ram**: Quantidade de memória RAM.
  - **hd**: Capacidade do HD.
  - **processador**: Modelo do processador.
  - **placa_video**: Informações da placa de vídeo.

#### Impressora

- **numero_equipamento**: Número do equipamento.
- **modelo**: Modelo da impressora.
- **local**: Local onde está instalada.

#### Thin Client

- **numero_patrimonio**: Número de patrimônio relacionado.
- **usuario**: Nome do usuário.
- **senha**: Senha de acesso.
- **numero_monitor**: Número do monitor associado.
- **local**: Local do equipamento.

---

## Como Usar

### Passo 1: Clonar o Repositório

Clone o repositório do projeto para sua máquina local:

```bash
git clone <url-do-repositorio>
