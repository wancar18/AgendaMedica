# Guia de Instalação e Execução do Sistema de Agendamento Médico

Este guia fornece instruções passo a passo para configurar e executar o Sistema de Agendamento Médico em uma nova máquina.

## Pré-requisitos

- Python 3.8 ou superior
- MySQL 5.7 ou superior
- Git (para clonar o repositório)

## Passo 1: Clonar o Repositório

```bash
# Clone o repositório do GitHub
git clone https://github.com/seu-usuario/agendador-medico.git

# Entre no diretório do projeto
cd agendador-medico
```

## Passo 2: Configurar o Ambiente Virtual (Recomendado)

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
```

## Passo 3: Instalar as Dependências

```bash
# Instalar todas as dependências necessárias
pip install -r requirements.txt
```

## Passo 4: Configurar o Banco de Dados

1. Inicie o serviço MySQL:
```bash
# No Windows (como administrador):
net start mysql

# No Linux:
sudo systemctl start mysql
```

2. Crie um banco de dados MySQL:

```sql
# Acesse o MySQL
mysql -u root -p

# No prompt do MySQL, execute:
CREATE DATABASE agendador_medico;
```

3. Configure as credenciais do banco de dados no arquivo `agendador_medico/config/config.py`:

```python
# Configurações do banco de dados
DB_CONFIG = {
    'host': 'localhost',
    'user': 'seu_usuario',
    'password': 'sua_senha',
    'database': 'agendador_medico'
}
```

4. Execute o script SQL para criar as tabelas necessárias:

```sql
USE agendador_medico;

-- Tabela de médicos
CREATE TABLE IF NOT EXISTS medicos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    CRM VARCHAR(20) NOT NULL,
    especialidade VARCHAR(100) NOT NULL,
    dias_atendimento TEXT,
    horarios_atendimento TEXT
);

-- Tabela de agendamentos
CREATE TABLE IF NOT EXISTS agendamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_paciente VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    especialidade VARCHAR(100) NOT NULL,
    medico_id INT NOT NULL,
    dia VARCHAR(20) NOT NULL,
    hora VARCHAR(10) NOT NULL,
    FOREIGN KEY (medico_id) REFERENCES medicos(id)
);
```

## Passo 5: Popular o Banco de Dados com Dados de Exemplo

Execute os seguintes comandos SQL para inserir 5 médicos e 5 agendamentos de exemplo:

```sql
USE agendador_medico;

-- Inserir médicos de exemplo
INSERT INTO medicos (nome, CRM, especialidade, dias_atendimento, horarios_atendimento) VALUES 
('Dr. Carlos Silva', '12345-SP', 'Cardiologia', 'Segunda-feira,Quarta-feira,Sexta-feira', '08:00,09:00,10:00,11:00,14:00,15:00,16:00'),
('Dra. Ana Oliveira', '23456-SP', 'Pediatria', 'Segunda-feira,Terça-feira,Quinta-feira', '08:30,09:30,10:30,14:30,15:30,16:30'),
('Dr. Roberto Santos', '34567-SP', 'Ortopedia', 'Terça-feira,Quinta-feira,Sábado', '07:00,08:00,09:00,10:00,11:00'),
('Dra. Juliana Costa', '45678-SP', 'Dermatologia', 'Segunda-feira,Quarta-feira,Sexta-feira', '13:00,14:00,15:00,16:00,17:00'),
('Dr. Marcelo Lima', '56789-SP', 'Clínica Geral', 'Segunda-feira,Terça-feira,Quarta-feira,Quinta-feira,Sexta-feira', '08:00,09:00,10:00,11:00,14:00,15:00,16:00,17:00');

-- Inserir agendamentos de exemplo
INSERT INTO agendamentos (nome_paciente, cpf, especialidade, medico_id, dia, hora) VALUES 
('João Pereira', '12345678901', 'Cardiologia', 1, 'Segunda-feira', '09:00'),
('Maria Souza', '23456789012', 'Pediatria', 2, 'Terça-feira', '09:30'),
('Pedro Almeida', '34567890123', 'Ortopedia', 3, 'Quinta-feira', '10:00'),
('Fernanda Gomes', '45678901234', 'Dermatologia', 4, 'Quarta-feira', '14:00'),
('Ricardo Martins', '56789012345', 'Clínica Geral', 5, 'Sexta-feira', '15:00');
```

Você também pode salvar esses comandos em um arquivo `dados_exemplo.sql` e executá-lo diretamente:

```bash
# No terminal, execute:
mysql -u seu_usuario -p agendador_medico < dados_exemplo.sql
```

## Passo 6: Executar o Sistema

```bash
# Executar a aplicação
python agendador_medico/app.py
```

O sistema estará disponível em: http://localhost:5000

## Passo 7: Acessar o Sistema

1. Abra seu navegador e acesse: http://localhost:5000
2. Faça login com as credenciais padrão:
   - Usuário: `admin`
   - Senha: `123`

## Estrutura do Projeto

O sistema segue a arquitetura MVC (Model-View-Controller):

- `models/`: Gerenciamento de dados e regras de negócio
- `views/`: Templates e interface do usuário
- `controllers/`: Rotas e lógica de controle
- `utils/`: Funções utilitárias
- `config/`: Configurações do sistema

## Dados de Exemplo Inseridos

### Médicos Cadastrados:
1. **Dr. Carlos Silva** - Cardiologia
   - Dias: Segunda, Quarta, Sexta
   - Horários: 08:00 às 11:00 e 14:00 às 16:00

2. **Dra. Ana Oliveira** - Pediatria
   - Dias: Segunda, Terça, Quinta
   - Horários: 08:30 às 10:30 e 14:30 às 16:30

3. **Dr. Roberto Santos** - Ortopedia
   - Dias: Terça, Quinta, Sábado
   - Horários: 07:00 às 11:00

4. **Dra. Juliana Costa** - Dermatologia
   - Dias: Segunda, Quarta, Sexta
   - Horários: 13:00 às 17:00

5. **Dr. Marcelo Lima** - Clínica Geral
   - Dias: Segunda a Sexta
   - Horários: 08:00 às 11:00 e 14:00 às 17:00

### Agendamentos Cadastrados:
1. João Pereira - Cardiologia com Dr. Carlos Silva
   - Segunda-feira às 09:00

2. Maria Souza - Pediatria com Dra. Ana Oliveira
   - Terça-feira às 09:30

3. Pedro Almeida - Ortopedia com Dr. Roberto Santos
   - Quinta-feira às 10:00

4. Fernanda Gomes - Dermatologia com Dra. Juliana Costa
   - Quarta-feira às 14:00

5. Ricardo Martins - Clínica Geral com Dr. Marcelo Lima
   - Sexta-feira às 15:00

## Solução de Problemas

### Erro de Conexão com o Banco de Dados

Verifique se:
- O serviço MySQL está em execução
- As credenciais no arquivo `config.py` estão corretas
- O banco de dados `agendador_medico` foi criado

### Erro de Importação de Módulos

Se ocorrerem erros de importação, verifique se você está executando o sistema a partir do diretório raiz do projeto.

### Outros Erros

Para a maioria dos erros, verifique o console onde o servidor está sendo executado para obter mensagens de erro detalhadas.

## Personalização

### Alterando as Credenciais de Administrador

Edite o arquivo `agendador_medico/config/config.py` e altere as seguintes variáveis:

```python
USUARIO_ADMIN = 'seu_novo_usuario'
SENHA_ADMIN = 'sua_nova_senha'
```

### Alterando a Porta do Servidor

Para alterar a porta padrão (5000), edite o arquivo `agendador_medico/app.py`:

```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)  # Altere 8080 para a porta desejada
```
