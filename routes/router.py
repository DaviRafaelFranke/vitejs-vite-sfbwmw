from flask import Blueprint, render_template, request, redirect, url_for, jsonify

# Cria um Blueprint para as rotas
router = Blueprint('router', __name__)

# Página de login (GET e POST)
@router.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtém dados do formulário
        username = request.form['username']
        password = request.form['password']
        
        # Lógica de verificação de login (exemplo simples)
        if username == "admin" and password == "admin":
            return redirect(url_for('router.home'))
        else:
            return "Login falhou. Tente novamente."
    
    # Renderiza a página de login (login.html)
    return render_template('login.html')

# Rota para processamento de login via API (para integração com React)
@router.route('/login', methods=['POST'])
def login_api():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Lógica de verificação do login
    if username == "admin" and password == "admin":
        return jsonify({"message": "success"}), 200
    else:
        return jsonify({"message": "Login falhou"}), 401

# Página inicial após o login bem-sucedido
@router.route('/home')
def home():
    # Renderiza a nova página "home"
    return render_template('src/pages/home.html')

# Página de agenda
@router.route('/agenda')
def agenda():
    # Renderiza a página de agenda
    return render_template('src/pages/agenda.html')

# Página de gerenciamento de horários
@router.route('/gerenciar-horarios')
def gerenciar_horarios():
    # Renderiza a página de gerenciamento de horários
    return render_template('src/pages/gerenciar_horarios.html')

# Página de cadastro de alunos
@router.route('/cadastrar-alunos')
def cadastrar_alunos():
    # Renderiza a página de cadastro de alunos
    return render_template('src/pages/cadastrar_alunos.html')

# Página de cadastro de usuários
@router.route('/cadastrar-usuarios')
def cadastrar_usuarios():
    # Renderiza a página de cadastro de usuários
    return render_template('src/pages/cadastrar_usuarios.html')

# Página de opções
@router.route('/opcoes')
def opcoes():
    # Renderiza a página de opções
    return render_template('src/pages/opcoes.html')
