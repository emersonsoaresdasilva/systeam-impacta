from flask import Blueprint, render_template, request, redirect, session, url_for
from database.funcoes import *
from classes import *

website_bp = Blueprint(
    'website',
    __name__,
    template_folder='templates'    
)

@website_bp.route('/')
def home():
    if 'usermail' in session:
        return redirect('admin')
    equipes = pegar_equipe()
    dados = {}
    
    for e in equipes:
        dados[e.sigla] = obter_dados_da_equipe(e)
        dados[e.sigla]['objeto'] = pegar_equipe(e.sigla)

    dados = Equipe.ordenar_por_pontos(dados)
    return render_template( 
        'home.html',
        equipes=equipes,
        dados=dados
        )

@website_bp.route('/detalhes/<sigla>')
def detalhes(sigla):
    if 'usermail' in session:
        return redirect(url_for('admin.home'))
    equipe = pegar_equipe(sigla)
    partidas = listar_partidas_da_equipe(sigla)
    return render_template(
        'detalhes.html',
        equipe = equipe,
        partidas = partidas
    )

    # equipe = pegar_equipe(sigla)
    # if equipe:
    #     return "PÁGINA DE DETALHES " + equipe.sigla
    # return "Equipe não encontrada"

@website_bp.route('/entrar', methods=['GET', 'POST'])
def entrar():
    erros = []
    if 'usermail' in session:
        return redirect(url_for('admin.home'))
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        user = pegar_usuario(email, senha)
        if user:
            session['usermail'] = email
            return redirect('entrar')
        erros.append('E-mail ou senha incorretos.') 
    #get
    return render_template(
        'entrar.html',
        erros=erros
    )