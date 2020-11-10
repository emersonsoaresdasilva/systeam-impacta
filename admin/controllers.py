from flask import Blueprint, render_template, request, redirect
from database.funcoes import *
from classes import *

admin_bp = Blueprint(
    'admin',
    __name__,
    template_folder='templates'    
)

@admin_bp.route('/')
def home():
    equipes = pegar_equipe()
    dados = {}
    for e in equipes:
        dados[e.sigla] = obter_dados_da_equipe(e)

    return render_template( 
        'home.html',
        equipes=equipes,
        dados=dados,
        admin=True
        )

@admin_bp.route('/equipes')
def equipes():
    equipes = pegar_equipe()
    return render_template( 
        'equipes.html',
        equipes=equipes,
        admin=True
        )

@admin_bp.route('/equipes/<sigla>')
def equipe(sigla):
    return "página de exibição da equipe" + sigla 

@admin_bp.route('/equipes/criar', methods=['GET', 'POST'])
def equipe_criar():
    funcao = 'Criar'
    criar = True
    if request.method == 'POST':
        nome = request.form['nome']
        sigla = request.form['sigla']
        local = request.form['local']

        e = Equipe(nome, sigla, local)
        criar_equipe(e)
        return redirect('/')

    return render_template(
        'form_equipes.html',
        equipe=equipe,
        funcao=funcao,
        criar=criar
    )

@admin_bp.route('/equipes/alterar/<sigla>')
def equipe_alterar(sigla):

    equipe = pegar_equipe(sigla)
    funcao = 'Alterar'

    return render_template('form_equipes.html', equipe=equipe, funcao=funcao)

@admin_bp.route('/partidas')
def partidas():
    partidas = pegar_partida()
    return render_template( 
        'partidas.html',
        partidas=partidas,
        admin=True
        )

@admin_bp.route('/partidas/<X>')
def partida(X):
    return "página de exibição da partida" + X 

@admin_bp.route('/partidas/criar')
def partida_criar():
    return render_template('form_partidas.html')

@admin_bp.route('/partidas/alterar/<sigla>')
def partida_alterar(sigla):
    return render_template('form_partidas.html')

@admin_bp.route('/sair')
def sair():
    return redirect('/')
