"""
Módulo de templates para o sistema de agendamento médico.
Contém todos os templates HTML utilizados no sistema.
"""

# Template de login
login_template = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Agendador Médico - Login</title>
<style>
  body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea, #764ba2);
    height: 100vh;
    margin: 0;
    display: flex;
    justify-content:center;
    align-items:center;
    color: #fff;
  }
  .login-container {
    background: #3a3f59;
    padding: 2rem 3rem;
    border-radius: 12px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    width: 320px;
  }
  h2 {
    text-align: center;
    margin-bottom: 1.5rem;
    font-weight: 700;
  }
  input[type="text"],
  input[type="password"] {
    width: 100%;
    padding: 0.6rem;
    margin-bottom: 1rem;
    border-radius: 6px;
    border: none;
    font-size: 1rem;
  }
  button {
    width: 100%;
    padding: 0.7rem;
    border: none;
    border-radius: 6px;
    background-color: #6a82fb;
    color: white;
    font-size: 1.1rem;
    font-weight: 700;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  button:hover {
    background-color: #4e64da;
  }
  .error {
    background: #ff4f4f;
    padding: 0.5rem;
    border-radius: 6px;
    margin-bottom: 1rem;
    text-align: center;
    font-weight: 600;
  }
</style>
</head>
<body>
  <div class="login-container">
    <h2>Login</h2>
    {% if erro %}
    <div class="error">{{ erro }}</div>
    {% endif %}
    <form method="post" action="{{ url_for('auth.login') }}">
      <input type="text" name="usuario" placeholder="Usuário" required />
      <input type="password" name="senha" placeholder="Senha" required />
      <button type="submit">Entrar</button>
    </form>
  </div>
</body>
</html>
"""

# Template de menu principal
menu_template = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8" />
<title>Menu - Agendador Médico</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<style>
  body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea, #764ba2);
    margin: 0;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
  }
  .menu-container {
    background: #3a3f59;
    padding: 2rem 3rem;
    border-radius: 16px;
    width: 320px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    text-align: center;
  }
  h2 {
    margin-bottom: 2rem;
    font-weight: 700;
  }
  button {
    display: block;
    width: 100%;
    padding: 1rem 0;
    margin: 0.8rem 0;
    font-size: 1.2rem;
    border: none;
    border-radius: 12px;
    background-color: #6a82fb;
    cursor: pointer;
    font-weight: 700;
    transition: background-color 0.3s ease;
  }
  button:hover {
    background-color: #4e64da;
  }
  .logout {
    margin-top: 1.5rem;
    background-color: #ff4f4f;
  }
  .logout:hover {
    background-color: #d13f3f;
  }
</style>
</head>
<body>
  <div class="menu-container">
    <h2>Menu</h2>
    <form action="{{ url_for('admin.parametros') }}" method="get" style="margin-bottom: 1rem;">
      <button type="submit">Parâmetros</button>
    </form>
    <form action="{{ url_for('agendamento.agendamentos') }}" method="get" style="margin-bottom: 1rem;">
      <button type="submit">Agendamentos</button>
    </form>
    <form action="{{ url_for('auth.logout') }}" method="post">
      <button type="submit" class="logout">Sair</button>
    </form>
  </div>
</body>
</html>
"""

# Template de parâmetros
parametros_template = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8" />
<title>Parâmetros - Agendador Médico</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<style>
  body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea, #764ba2);
    margin: 0;
    min-height: 100vh;
    color: white;
    padding: 2rem 1rem;
  }
  .container {
    max-width: 700px;
    background: #3a3f59;
    margin: 0 auto;
    border-radius: 16px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    padding: 2rem;
  }
  h2, h3 {
    font-weight: 700;
    text-align: center;
  }
  h2 {
    margin-bottom: 2rem;
  }
  h3 {
    margin-top: 1.5rem;
    margin-bottom: 1rem;
  }
  label {
    display: block;
    margin-top: 1rem;
    font-weight: 600;
    font-size: 1rem;
    cursor: pointer;
  }
  input[type="text"],
  select {
    width: 100%;
    padding: 0.5rem;
    margin-top: 0.4rem;
    border-radius: 8px;
    border: none;
    font-size: 1rem;
    color: black;
  }
  .day-checkboxes, .time-checkboxes {
    display: flex;
    flex-wrap: wrap;
    margin-top: 0.4rem;
    gap: 12px;
  }
  .day-checkboxes label,
  .time-checkboxes label {
    flex: 1 1 30%;
    background: #57608a;
    padding: 0.4rem 0.6rem;
    border-radius: 8px;
    user-select: none;
    text-align: center;
    font-weight: 600;
    color: white;
  }
  input[type="checkbox"] {
    margin-right: 8px;
    vertical-align: middle;
  }
  button {
    margin-top: 1rem;
    width: 100%;
    padding: 1rem;
    font-size: 1.1rem;
    font-weight: 700;
    border: none;
    border-radius: 12px;
    background-color: #6a82fb;
    color: white;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  button:hover {
    background-color: #4e64da;
  }
  .back-button {
    margin-top: 1rem;
    background-color: #ff4f4f;
  }
  .back-button:hover {
    background-color: #d13f3f;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 1rem;
  }
  th, td {
    border: 1px solid #57608a;
    padding: 0.75rem;
    text-align: center;
    vertical-align: middle;
  }
  th {
    background: #4c509e;
    font-weight: 700;
  }
  td button {
    width: auto;
    margin: 0 0.25rem;
    padding: 0.4rem 0.7rem;
    font-size: 0.9rem;
  }
  .delete-button {
    background-color: #ff4f4f;
  }
  .delete-button:hover {
    background-color: #d13f3f;
  }
  .edit-button {
    background-color: #6a82fb;
  }
  .edit-button:hover {
    background-color: #4e64da;
  }

  /* Modal */
  .modal-background {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.6);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }
  .modal {
    background: #3a3f59;
    border-radius: 12px;
    padding: 1.5rem;
    width: 400px;
    max-width: 90%;
  }
  .modal h3 {
    margin-top: 0;
    margin-bottom: 1rem;
  }
  .modal label {
    font-weight: 600;
    margin-top: 0.8rem;
  }
  .modal .day-checkboxes, .modal .time-checkboxes {
    margin-top: 0.3rem;
    gap: 10px;
  }
  .modal button {
    width: 48%;
    margin-top: 1rem;
  }
  .modal-buttons {
    display: flex;
    justify-content: space-between;
  }
  
  /* Consultas por médico */
  .consultas-medico {
    margin-top: 2rem;
    padding-top: 1.5rem;
    border-top: 1px solid #57608a;
  }
  .consulta-item {
    background: #4c509e;
    border-radius: 8px;
    padding: 0.8rem;
    margin-bottom: 0.8rem;
  }
  .consulta-item p {
    margin: 0.3rem 0;
  }
  .consulta-dia {
    font-weight: 700;
    margin-top: 1.5rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid #57608a;
  }
  .sem-consultas {
    text-align: center;
    padding: 1rem;
    font-style: italic;
    color: #ccc;
  }
</style>
</head>
<body>
  <div class="container">
    <h2>Parâmetros</h2>

    <h3>Cadastrar Médico</h3>
    <form method="post" action="{{ url_for('admin.cadastrar_medico') }}">
      <label for="nome_medico">Nome do Médico</label>
      <input type="text" id="nome_medico" name="nome_medico" placeholder="Digite o nome do médico" required />

      <label for="CRM">CRM</label>
      <input type="text" id="CRM" name="CRM" placeholder="Digite o CRM" required />

      <label for="especialidade">Especialidade</label>
      <input type="text" id="especialidade" name="especialidade" placeholder="Digite a especialidade" required />

      <label>Dias da Semana que atende</label>
      <div class="day-checkboxes">
        {% for dia in dias_da_semana %}
          <label><input type="checkbox" name="dias" value="{{ dia }}" />{{ dia }}</label>
        {% endfor %}
      </div>

      <label>Horários de Atendimento</label>
      <div class="time-checkboxes" style="max-height:220px; overflow-y: auto;">
        {% for horario in horarios %}
          <label><input type="checkbox" name="horarios" value="{{ horario }}" />{{ horario }}</label>
        {% endfor %}
      </div>

      <button type="submit">Salvar</button>
    </form>

    <h3>Manutenção de Médicos</h3>
    {% if medicos and medicos|length > 0 %}
    <table>
      <thead>
        <tr>
          <th>Nome</th>
          <th>CRM</th>
          <th>Especialidade</th>
          <th>Dias Atendimento</th>
          <th>Horários Atendimento</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        {% for medico in medicos %}
        <tr>
          <td>{{ medico.nome }}</td>
          <td>{{ medico.CRM }}</td>
          <td>{{ medico.especialidade }}</td>
          <td>{{ medico.dias_atendimento }}</td>
          <td>{{ medico.horarios_atendimento }}</td>
          <td>
            <form method="get" action="{{ url_for('admin.editar_medico', medico_id=medico.id) }}" style="display:inline-block;">
              <button type="submit" class="edit-button">Alterar</button>
            </form>
            <form method="post" action="{{ url_for('admin.deletar_medico', medico_id=medico.id) }}" onsubmit="return confirm('Tem certeza que deseja deletar este médico?');" style="display:inline-block;">
              <button type="submit" class="delete-button">Deletar</button>
            </form>
          </td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
    {% else %}
      <p>Nenhum médico cadastrado.</p>
    {% endif %}
    
    <h3>Consultas por Médico</h3>
    <form id="consultas-medico-form">
      <label for="medico_consultas">Selecione o médico:</label>
      <select id="medico_consultas" name="medico_consultas">
        <option value="">Selecione...</option>
        {% for medico in medicos %}
          <option value="{{ medico.id }}">{{ medico.nome }} ({{ medico.especialidade }})</option>
        {% endfor %}
      </select>
      <button type="button" id="buscar-consultas">Buscar Consultas</button>
    </form>
    
    <div id="consultas-container" class="consultas-medico">
      <!-- As consultas serão exibidas aqui -->
    </div>
    
    <form action="{{ url_for('admin.menu') }}" method="get">
      <button type="submit" class="back-button">Voltar ao Menu</button>
    </form>
  </div>
  
  <script>
    document.getElementById('buscar-consultas').addEventListener('click', function() {
      const medicoId = document.getElementById('medico_consultas').value;
      if (!medicoId) {
        alert('Por favor, selecione um médico');
        return;
      }
      
      const consultasContainer = document.getElementById('consultas-container');
      consultasContainer.innerHTML = '<p style="text-align: center;">Carregando consultas...</p>';
      
      fetch(`/api/consultas_por_medico?medico_id=${medicoId}`)
        .then(response => response.json())
        .then(data => {
          if (!data || data.length === 0) {
            consultasContainer.innerHTML = '<p class="sem-consultas">Nenhuma consulta agendada para este médico.</p>';
            return;
          }
          
          // Agrupar consultas por dia
          const consultasPorDia = {};
          data.forEach(consulta => {
            if (!consultasPorDia[consulta.dia]) {
              consultasPorDia[consulta.dia] = [];
            }
            consultasPorDia[consulta.dia].push(consulta);
          });
          
          // Construir HTML
          let html = '';
          for (const dia in consultasPorDia) {
            html += `<div class="consulta-dia">${dia}</div>`;
            
            consultasPorDia[dia].forEach(consulta => {
              html += `
                <div class="consulta-item">
                  <p><strong>Paciente:</strong> ${consulta.nome_paciente}</p>
                  <p><strong>CPF:</strong> ${consulta.cpf}</p>
                  <p><strong>Horário:</strong> ${consulta.hora}</p>
                  <p><strong>Especialidade:</strong> ${consulta.especialidade}</p>
                </div>
              `;
            });
          }
          
          consultasContainer.innerHTML = html;
        })
        .catch(error => {
          console.error('Erro:', error);
          consultasContainer.innerHTML = '<p class="sem-consultas">Erro ao buscar consultas. Tente novamente.</p>';
        });
    });
  </script>
</body>
</html>
"""

# Template de edição de médico
editar_medico_template = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8" />
<title>Editar Médico - Agendador Médico</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<style>
  body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea, #764ba2);
    margin: 0;
    min-height: 100vh;
    color: white;
    padding: 2rem 1rem;
  }
  .container {
    max-width: 600px;
    background: #3a3f59;
    margin: 0 auto;
    border-radius: 16px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    padding: 2rem;
  }
  h2 {
    margin-bottom: 1.5rem;
    font-weight: 700;
    text-align: center;
  }
  label {
    display: block;
    margin-top: 1rem;
    font-weight: 600;
    font-size: 1rem;
    cursor: pointer;
  }
  .day-checkboxes, .time-checkboxes {
    display: flex;
    flex-wrap: wrap;
    margin-top: 0.4rem;
    gap: 12px;
  }
  .day-checkboxes label,
  .time-checkboxes label {
    flex: 1 1 30%;
    background: #57608a;
    padding: 0.4rem 0.6rem;
    border-radius: 8px;
    user-select: none;
    text-align: center;
    font-weight: 600;
  }
  input[type="checkbox"] {
    margin-right: 8px;
    vertical-align: middle;
  }
  button {
    margin-top: 2rem;
    width: 100%;
    padding: 1rem;
    font-size: 1.1rem;
    font-weight: 700;
    border: none;
    border-radius: 12px;
    background-color: #6a82fb;
    color: white;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  button:hover {
    background-color: #4e64da;
  }
  .back-button {
    margin-top: 1rem;
    background-color: #ff4f4f;
  }
  .back-button:hover {
    background-color: #d13f3f;
  }
</style>
</head>
<body>
  <div class="container">
    <h2>Alterar Dias e Horários do Médico</h2>
    <form method="post" action="{{ url_for('admin.editar_medico', medico_id=medico.id) }}">
      <label>Nome do Médico:</label>
      <input type="text" value="{{ medico.nome }}" readonly />

      <label>CRM:</label>
      <input type="text" value="{{ medico.CRM }}" readonly />

      <label>Especialidade:</label>
      <input type="text" value="{{ medico.especialidade }}" readonly />

      <label>Dias da Semana que atende</label>
      <div class="day-checkboxes">
        {% for dia in dias_da_semana %}
          <label>
            <input type="checkbox" name="dias" value="{{ dia }}" {% if dia in dias_selecionados %}checked{% endif %} />
            {{ dia }}
          </label>
        {% endfor %}
      </div>

      <label>Horários de Atendimento</label>
      <div class="time-checkboxes" style="max-height:220px; overflow-y: auto;">
        {% for horario in horarios %}
          <label>
            <input type="checkbox" name="horarios" value="{{ horario }}" {% if horario in horarios_selecionados %}checked{% endif %} />
            {{ horario }}
          </label>
        {% endfor %}
      </div>

      <button type="submit">Salvar Alterações</button>
    </form>
    <form action="{{ url_for('admin.parametros') }}" method="get">
      <button type="submit" class="back-button">Voltar</button>
    </form>
  </div>
</body>
</html>
"""

# Template de agendamentos
agendamentos_template = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8" />
<title>Agendamentos - Agendador Médico</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<style>
  body {
    background: #f0f2f5;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .chat-container {
    width: 400px;
    height: 600px;
    background: white;
    border-radius: 12px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }
  .chat-header {
    background: #6ac7ff;
    padding: 1rem;
    color: white;
    font-weight: 700;
    font-size: 1.25rem;
    text-align: center;
  }
  .chat-messages {
    flex: 1;
    padding: 1rem;
    overflow-y: auto;
  }
  .message {
    max-width: 80%;
    margin-bottom: 1rem;
    padding: 0.6rem 1rem;
    border-radius: 20px;
    line-height: 1.3;
    white-space: pre-wrap;
    word-wrap: break-word;
  }
  .message.bot {
    background-color: #add8ff;
    color: #000;
    align-self: flex-start;
  }
  .message.user {
    background-color: #a0dca0;
    color: #000;
    align-self: flex-end;
  }
  .chat-input-area {
    display: flex;
    border-top: 1px solid #ddd;
    padding: 0.5rem;
  }
  .chat-input {
    flex-grow: 1;
    border: none;
    border-radius: 20px;
    padding: 0.5rem 1rem;
    font-size: 1rem;
  }
  .send-button {
    background-color: #6ac7ff;
    border: none;
    color: white;
    padding: 0 1rem;
    margin-left: 0.5rem;
    border-radius: 20px;
    cursor: pointer;
    font-weight: 700;
    font-size: 1rem;
  }
  .send-button:hover {
    background-color: #39b3ff;
  }
  .options {
    margin-top: 0.5rem;
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
  }
  .option-button {
    background-color: #6ac7ff;
    color: black;
    border: none;
    border-radius: 20px;
    padding: 0.5rem 1rem;
    font-weight: 700;
    cursor: pointer;
    flex: 1 0 30%;
    text-align: center;
    transition: background-color 0.3s;
  }
  .option-button:hover {
    background-color: #39b3ff;
  }
  select {
    border-radius: 8px;
    padding: 0.5rem;
    font-size: 1rem;
    width: 100%;
    margin-top: 0.5rem;
  }
  .consulta-card {
    background-color: #f0f8ff;
    border-radius: 10px;
    padding: 1rem;
    margin-bottom: 1rem;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  }
  .consulta-card h3 {
    margin-top: 0;
    margin-bottom: 0.5rem;
    font-size: 1.1rem;
  }
  .consulta-card p {
    margin: 0.3rem 0;
    font-size: 0.9rem;
  }
  .consulta-actions {
    display: flex;
    justify-content: space-between;
    margin-top: 0.8rem;
  }
  .consulta-actions button {
    flex: 1;
    margin: 0 0.3rem;
    padding: 0.5rem;
    border: none;
    border-radius: 5px;
    font-weight: 600;
    cursor: pointer;
  }
  .alterar-btn {
    background-color: #6a82fb;
    color: white;
  }
  .cancelar-btn {
    background-color: #ff4f4f;
    color: white;
  }
</style>
</head>
<body>
  <div class="chat-container">
    <div class="chat-header">Agendamento Médico</div>
    <div class="chat-messages" id="chat-messages">
      <!-- Mensagens serão inseridas aqui -->
    </div>
    <form id="chat-form" class="chat-input-area" autocomplete="off">
      <input type="text" id="chat-input" class="chat-input" placeholder="Digite aqui..." />
      <button type="submit" class="send-button">Enviar</button>
    </form>
  </div>

<script>
  const chatMessages = document.getElementById('chat-messages');
  const chatForm = document.getElementById('chat-form');
  const chatInput = document.getElementById('chat-input');

  let stage = 0;
  let operacao = '';
  let agendamento = {
    nome_paciente: '',
    cpf: '',
    especialidade: '',
    medico_id: null,
    medico_nome: '',
    dia: '',
    hora: ''
  };
  let consultaSelecionada = null;

  function addMessage(text, sender) {
    const message = document.createElement('div');
    message.className = 'message ' + sender;
    message.textContent = text;
    chatMessages.appendChild(message);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function addOptions(options) {
    const container = document.createElement('div');
    container.className = 'options';
    options.forEach(opt => {
      const btn = document.createElement('button');
      btn.className = 'option-button';
      btn.type = 'button';
      btn.textContent = opt.label;
      btn.dataset.value = opt.value;
      btn.onclick = () => handleOptionClick(opt.value, opt.label);
      container.appendChild(btn);
    });
    chatMessages.appendChild(container);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function clearOptions() {
    const containers = document.querySelectorAll('.options');
    containers.forEach(c => c.remove());
  }

  function handleOptionClick(value, label) {
    addMessage(label, 'user');
    clearOptions();
    operacao = value;
    processStage(value);
  }

  function addConsultaCard(consulta) {
    const card = document.createElement('div');
    card.className = 'consulta-card';
    card.innerHTML = `
      <h3>Consulta: ${consulta.especialidade}</h3>
      <p><strong>Médico:</strong> ${consulta.medico_nome}</p>
      <p><strong>Dia:</strong> ${consulta.dia}</p>
      <p><strong>Hora:</strong> ${consulta.hora}</p>
      <div class="consulta-actions">
        <button class="alterar-btn" data-id="${consulta.id}">Alterar</button>
        <button class="cancelar-btn" data-id="${consulta.id}">Cancelar</button>
      </div>
    `;
    
    // Adicionar event listeners para os botões
    const alterarBtn = card.querySelector('.alterar-btn');
    const cancelarBtn = card.querySelector('.cancelar-btn');
    
    alterarBtn.addEventListener('click', () => {
      consultaSelecionada = consulta;
      handleAlterarConsulta(consulta);
    });
    
    cancelarBtn.addEventListener('click', () => {
      consultaSelecionada = consulta;
      handleCancelarConsulta(consulta);
    });
    
    chatMessages.appendChild(card);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  async function fetchEspecialidades() {
    const resp = await fetch('/api/especialidades');
    const data = await resp.json();
    return data;
  }

  async function fetchMedicos(especialidade) {
    const resp = await fetch(`/api/medicos?especialidade=${encodeURIComponent(especialidade)}`);
    const data = await resp.json();
    return data;
  }

  async function fetchDias(medico_id) {
    const resp = await fetch(`/api/dias?medico_id=${medico_id}`);
    const data = await resp.json();
    return data;
  }

  async function fetchHorarios(medico_id) {
    const resp = await fetch(`/api/horarios?medico_id=${medico_id}`);
    const data = await resp.json();
    return data;
  }

  async function fetchConsultasPorCPF(cpf) {
    const resp = await fetch(`/api/consultas?cpf=${cpf}`);
    if (!resp.ok) {
      throw new Error('Erro ao buscar consultas');
    }
    const data = await resp.json();
    return data;
  }

  function showSelectInput(labelText, options, onSelect) {
    const container = document.createElement('div');
    container.style.marginTop = '0.5rem';
    const label = document.createElement('label');
    label.textContent = labelText;
    label.style.fontWeight = '700';
    label.style.display = 'block';
    container.appendChild(label);

    const select = document.createElement('select');
    const defaultOption = document.createElement('option');
    defaultOption.value = '';
    defaultOption.textContent = 'Selecione...';
    select.appendChild(defaultOption);

    options.forEach(opt => {
      const option = document.createElement('option');
      option.value = opt.value;
      option.textContent = opt.label;
      select.appendChild(option);
    });
    select.onchange = () => {
      if(select.value){
        onSelect(select.value, select.options[select.selectedIndex].textContent);
        select.disabled = true;
        chatInput.disabled = false;
        chatInput.focus();
        container.remove();
      }
    };
    container.appendChild(select);
    chatMessages.appendChild(container);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    chatInput.disabled = true;
  }

  function formatUserSelection(title, text) {
    addMessage(title + ': ' + text, 'user');
  }

  function handleAlterarConsulta(consulta) {
    addMessage(`Você selecionou alterar a consulta de ${consulta.especialidade} com Dr(a). ${consulta.medico_nome} no dia ${consulta.dia} às ${consulta.hora}.`, 'bot');
    addMessage('O que você deseja alterar?', 'bot');
    
    addOptions([
      {value: 'ALTERAR_MEDICO', label: 'Médico'},
      {value: 'ALTERAR_DIA', label: 'Dia'},
      {value: 'ALTERAR_HORA', label: 'Horário'}
    ]);
    
    stage = 10; // Estágio para alteração de consulta
  }

  function handleCancelarConsulta(consulta) {
    addMessage(`Você selecionou cancelar a consulta de ${consulta.especialidade} com Dr(a). ${consulta.medico_nome} no dia ${consulta.dia} às ${consulta.hora}.`, 'bot');
    addMessage('Tem certeza que deseja cancelar esta consulta?', 'bot');
    
    addOptions([
      {value: 'CONFIRMAR_CANCELAMENTO', label: 'Sim, cancelar'},
      {value: 'CANCELAR_OPERACAO', label: 'Não, voltar'}
    ]);
    
    stage = 20; // Estágio para cancelamento de consulta
  }

  function processStage(input) {
    switch(stage) {
      case 0:
        if(input === 'AGENDAR CONSULTA') {
          addMessage('Digite seu nome completo:', 'bot');
          stage = 1;
          chatInput.disabled = false;
          chatInput.focus();
        } else if(input === 'MINHAS CONSULTAS') {
          addMessage('Digite seu CPF (somente números):', 'bot');
          stage = 5; // Estágio para busca de consultas por CPF
          chatInput.disabled = false;
          chatInput.focus();
        } else {
          addMessage('Selecione uma opção válida.', 'bot');
        }
        break;
      case 1:
        agendamento.nome_paciente = input;
        formatUserSelection('Nome completo', input);
        addMessage('Digite seu CPF (somente números):', 'bot');
        stage = 2;
        chatInput.disabled = false;
        chatInput.focus();
        break;
      case 2:
        if(!/^\d{11}$/.test(input)) {
          addMessage('CPF inválido. Por favor, digite 11 números sem pontos ou traços.', 'bot');
          chatInput.disabled = false;
          chatInput.focus();
          break;
        }
        agendamento.cpf = input;
        formatUserSelection('CPF', input);
        addMessage('Buscando especialidades médicas...', 'bot');
        fetchEspecialidades().then(especialidades => {
          if(especialidades.length === 0){
            addMessage('Nenhuma especialidade cadastrada.', 'bot');
            return;
          }
          const opts = especialidades.map(e => ({value: e.nome, label: e.nome}));
          addMessage('Selecione a especialidade médica:', 'bot');
          showSelectInput('Especialidade', opts, (val) => {
            agendamento.especialidade = val;
            formatUserSelection('Especialidade', val);
            addMessage('Buscando médicos desta especialidade...', 'bot');
            fetchMedicos(val).then(medicos => {
              if(medicos.length === 0){
                addMessage('Nenhum médico encontrado para essa especialidade.', 'bot');
                return;
              }
              const mOpts = medicos.map(m => ({value: m.id, label: m.nome}));
              addMessage('Selecione o médico:', 'bot');
              showSelectInput('Médico', mOpts, (val, label) => {
                agendamento.medico_id = val;
                agendamento.medico_nome = label;
                formatUserSelection('Médico', label);
                addMessage('Buscando dias disponíveis para o médico...', 'bot');
                fetchDias(val).then(dias => {
                  if(dias.length === 0) {
                    addMessage('Nenhum dia disponível para este médico.', 'bot');
                    return;
                  }
                  const dOpts = dias.map(dia => ({value: dia, label: dia}));
                  addMessage('Selecione o dia para agendamento:', 'bot');
                  showSelectInput('Dia', dOpts, (val) => {
                    agendamento.dia = val;
                    formatUserSelection('Dia', val);
                    addMessage('Buscando horários disponíveis...', 'bot');
                    
                    // Busca os horários disponíveis para o médico e dia selecionados
                    fetch(`/api/horarios_disponiveis?medico_id=${agendamento.medico_id}&dia=${encodeURIComponent(agendamento.dia)}`)
                      .then(response => {
                        if (!response.ok) {
                          throw new Error('Erro ao buscar horários disponíveis');
                        }
                        return response.json();
                      })
                      .then(disponiveis => {
                        console.log('Horários disponíveis:', disponiveis); // Debug
                        
                        if (!disponiveis || disponiveis.length === 0) {
                          addMessage('Nenhum horário disponível para este dia.', 'bot');
                          // Modificação: Voltar ao menu inicial após 3 segundos
                          setTimeout(() => {
                            resetChat();
                          }, 3000);
                          return;
                        }
                        
                        const hOpts = disponiveis.map(h => ({value: h, label: h}));
                        addMessage('Selecione o horário do atendimento:', 'bot');
                        showSelectInput('Horário', hOpts, (val) => {
                          agendamento.hora = val;
                          formatUserSelection('Horário', val);
                          addMessage('Agendando consulta...', 'bot');
                          fetch('/api/agendar', {
                            method: 'POST',
                            headers: {
                              'Content-Type': 'application/json'
                            },
                            body: JSON.stringify(agendamento)
                          }).then(res => res.json()).then(result => {
                            if(result.success){
                              addMessage(`Consulta agendada com sucesso!`, 'bot');
                              addMessage(`Resumo:
Nome: ${agendamento.nome_paciente}
CPF: ${agendamento.cpf}
Especialidade: ${agendamento.especialidade}
Médico: ${agendamento.medico_nome}
Dia: ${agendamento.dia}
Hora: ${agendamento.hora}`, 'bot');
                              addMessage(`Obrigado por usar nosso sistema!`, 'bot');
                              
                              // Reiniciar o chat
                              setTimeout(() => {
                                resetChat();
                              }, 3000);
                            } else {
                              addMessage('Erro ao agendar: ' + result.message, 'bot');
                            }
                          }).catch(error => {
                            addMessage('Erro ao agendar consulta: ' + error.message, 'bot');
                          });
                          chatInput.disabled = true;
                        });
                      })
                      .catch(error => {
                        console.error('Erro:', error);
                        addMessage('Erro ao buscar horários disponíveis. Por favor, tente novamente.', 'bot');
                      });
                  });
                });
              });
            });
          });
        });
        stage = 99; // Estágio de processamento, aguardando callbacks
        chatInput.disabled = true;
        break;
      case 5: // Busca de consultas por CPF
        if(!/^\d{11}$/.test(input)) {
          addMessage('CPF inválido. Por favor, digite 11 números sem pontos ou traços.', 'bot');
          chatInput.disabled = false;
          chatInput.focus();
          break;
        }
        
        const cpf = input;
        formatUserSelection('CPF', cpf);
        addMessage('Buscando suas consultas...', 'bot');
        
        fetchConsultasPorCPF(cpf)
          .then(consultas => {
            if (!consultas || consultas.length === 0) {
              addMessage('Nenhuma consulta encontrada para este CPF.', 'bot');
              
              // Oferecer opção de agendar
              addMessage('Deseja agendar uma nova consulta?', 'bot');
              addOptions([
                {value: 'AGENDAR_CONSULTA', label: 'Sim, agendar'},
                {value: 'VOLTAR_INICIO', label: 'Não, voltar ao início'}
              ]);
              
              stage = 6; // Estágio para decidir após não encontrar consultas
              return;
            }
            
            addMessage(`Encontramos ${consultas.length} consulta(s) agendada(s):`, 'bot');
            
            // Mostrar cards de consultas
            consultas.forEach(consulta => {
              addConsultaCard(consulta);
            });
            
            addMessage('Selecione a consulta que deseja gerenciar clicando em "Alterar" ou "Cancelar".', 'bot');
            
            stage = 99; // Aguardando seleção de consulta
          })
          .catch(error => {
            console.error('Erro:', error);
            addMessage('Erro ao buscar consultas. Por favor, tente novamente.', 'bot');
            chatInput.disabled = false;
            chatInput.focus();
          });
        
        chatInput.disabled = true;
        break;
      case 6: // Decisão após não encontrar consultas
        if (input === 'AGENDAR_CONSULTA') {
          // Redirecionar para o fluxo de agendamento
          addMessage('Vamos agendar uma nova consulta.', 'bot');
          addMessage('Digite seu nome completo:', 'bot');
          stage = 1;
          chatInput.disabled = false;
          chatInput.focus();
        } else if (input === 'VOLTAR_INICIO') {
          // Voltar ao início
          resetChat();
        }
        break;
      case 10: // Alteração de consulta
        if (input === 'ALTERAR_MEDICO') {
          // Alterar médico
          addMessage('Buscando médicos disponíveis...', 'bot');
          fetchMedicos(consultaSelecionada.especialidade).then(medicos => {
            if(medicos.length === 0){
              addMessage('Nenhum médico encontrado para essa especialidade.', 'bot');
              return;
            }
            const mOpts = medicos.map(m => ({value: m.id, label: m.nome}));
            addMessage('Selecione o novo médico:', 'bot');
            showSelectInput('Médico', mOpts, (val, label) => {
              const novoMedicoId = val;
              const novoMedicoNome = label;
              formatUserSelection('Novo médico', label);
              
              // Atualizar a consulta com o novo médico
              fetch('/api/alterar_consulta', {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                  consulta_id: consultaSelecionada.id,
                  campo: 'medico_id',
                  valor: novoMedicoId,
                  medico_nome: novoMedicoNome
                })
              }).then(res => res.json()).then(result => {
                if(result.success){
                  addMessage(`Consulta alterada com sucesso! O novo médico é ${novoMedicoNome}.`, 'bot');
                  
                  // Reiniciar o chat
                  setTimeout(() => {
                    resetChat();
                  }, 3000);
                } else {
                  addMessage('Erro ao alterar consulta: ' + result.message, 'bot');
                }
              }).catch(error => {
                addMessage('Erro ao alterar consulta: ' + error.message, 'bot');
              });
            });
          });
        } else if (input === 'ALTERAR_DIA') {
          // Alterar dia
          addMessage('Buscando dias disponíveis...', 'bot');
          fetchDias(consultaSelecionada.medico_id).then(dias => {
            if(dias.length === 0) {
              addMessage('Nenhum dia disponível para este médico.', 'bot');
              return;
            }
            const dOpts = dias.map(dia => ({value: dia, label: dia}));
            addMessage('Selecione o novo dia para agendamento:', 'bot');
            showSelectInput('Dia', dOpts, (val) => {
              const novoDia = val;
              formatUserSelection('Novo dia', novoDia);
              
              // Atualizar a consulta com o novo dia
              fetch('/api/alterar_consulta', {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                  consulta_id: consultaSelecionada.id,
                  campo: 'dia',
                  valor: novoDia
                })
              }).then(res => res.json()).then(result => {
                if(result.success){
                  addMessage(`Consulta alterada com sucesso! O novo dia é ${novoDia}.`, 'bot');
                  
                  // Reiniciar o chat
                  setTimeout(() => {
                    resetChat();
                  }, 3000);
                } else {
                  addMessage('Erro ao alterar consulta: ' + result.message, 'bot');
                }
              }).catch(error => {
                addMessage('Erro ao alterar consulta: ' + error.message, 'bot');
              });
            });
          });
        } else if (input === 'ALTERAR_HORA') {
          // Alterar horário
          addMessage('Buscando horários disponíveis...', 'bot');
          
          // Busca os horários disponíveis para o médico e dia selecionados
          fetch(`/api/horarios_disponiveis?medico_id=${consultaSelecionada.medico_id}&dia=${encodeURIComponent(consultaSelecionada.dia)}`)
            .then(response => {
              if (!response.ok) {
                throw new Error('Erro ao buscar horários disponíveis');
              }
              return response.json();
            })
            .then(disponiveis => {
              if (!disponiveis || disponiveis.length === 0) {
                addMessage('Nenhum horário disponível para este dia.', 'bot');
                // Modificação: Voltar ao menu inicial após 3 segundos
                setTimeout(() => {
                  resetChat();
                }, 3000);
                return;
              }
              
              const hOpts = disponiveis.map(h => ({value: h, label: h}));
              addMessage('Selecione o novo horário do atendimento:', 'bot');
              showSelectInput('Horário', hOpts, (val) => {
                const novoHorario = val;
                formatUserSelection('Novo horário', novoHorario);
                
                // Atualizar a consulta com o novo horário
                fetch('/api/alterar_consulta', {
                  method: 'POST',
                  headers: {
                    'Content-Type': 'application/json'
                  },
                  body: JSON.stringify({
                    consulta_id: consultaSelecionada.id,
                    campo: 'hora',
                    valor: novoHorario
                  })
                }).then(res => res.json()).then(result => {
                  if(result.success){
                    addMessage(`Consulta alterada com sucesso! O novo horário é ${novoHorario}.`, 'bot');
                    
                    // Reiniciar o chat
                    setTimeout(() => {
                      resetChat();
                    }, 3000);
                  } else {
                    addMessage('Erro ao alterar consulta: ' + result.message, 'bot');
                  }
                }).catch(error => {
                  addMessage('Erro ao alterar consulta: ' + error.message, 'bot');
                });
              });
            })
            .catch(error => {
              console.error('Erro:', error);
              addMessage('Erro ao buscar horários disponíveis. Por favor, tente novamente.', 'bot');
            });
        }
        stage = 99; // Aguardando callbacks
        chatInput.disabled = true;
        break;
      case 20: // Cancelamento de consulta
        if (input === 'CONFIRMAR_CANCELAMENTO') {
          // Cancelar a consulta
          fetch('/api/cancelar_consulta', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              consulta_id: consultaSelecionada.id
            })
          }).then(res => res.json()).then(result => {
            if(result.success){
              addMessage(`Consulta cancelada com sucesso!`, 'bot');
              
              // Reiniciar o chat
              setTimeout(() => {
                resetChat();
              }, 3000);
            } else {
              addMessage('Erro ao cancelar consulta: ' + result.message, 'bot');
            }
          }).catch(error => {
            addMessage('Erro ao cancelar consulta: ' + error.message, 'bot');
          });
        } else if (input === 'CANCELAR_OPERACAO') {
          // Voltar sem cancelar
          addMessage('Operação de cancelamento cancelada.', 'bot');
          
          // Reiniciar o chat
          setTimeout(() => {
            resetChat();
          }, 2000);
        }
        stage = 99; // Aguardando callbacks
        chatInput.disabled = true;
        break;
      default:
        addMessage('Selecione uma opção válida.', 'bot');
    }
  }

  function resetChat() {
    // Limpar mensagens
    chatMessages.innerHTML = '';
    
    // Resetar variáveis
    stage = 0;
    operacao = '';
    agendamento = {
      nome_paciente: '',
      cpf: '',
      especialidade: '',
      medico_id: null,
      medico_nome: '',
      dia: '',
      hora: ''
    };
    consultaSelecionada = null;
    
    // Mostrar mensagem inicial
    addMessage('Olá, bem vindo(a) ao sistema de agendamento médico. O que deseja fazer?', 'bot');
    addOptions([
      {value: 'AGENDAR CONSULTA', label: 'AGENDAR CONSULTA'},
      {value: 'MINHAS CONSULTAS', label: 'MINHAS CONSULTAS'}
    ]);
    
    // Habilitar formulário
    chatForm.addEventListener('submit', onFormSubmit);
  }

  function onFormSubmit(event){
    event.preventDefault();
    const input = chatInput.value.trim();
    if(!input) return;
    addMessage(input, 'user');
    chatInput.value = '';
    chatInput.disabled = true;
    setTimeout(() => processStage(input), 300);
  }

  chatForm.addEventListener('submit', onFormSubmit);

  addMessage('Olá, bem vindo(a) ao sistema de agendamento médico. O que deseja fazer?', 'bot');
  addOptions([
    {value: 'AGENDAR CONSULTA', label: 'AGENDAR CONSULTA'},
    {value: 'MINHAS CONSULTAS', label: 'MINHAS CONSULTAS'}
  ]);
</script>
</body>
</html>
"""
