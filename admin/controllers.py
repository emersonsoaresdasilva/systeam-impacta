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
    return render_template('detalhes.html')

@admin_bp.route('/equipes/criar', methods=['GET', 'POST'])
def equipe_criar():
    funcao = 'Criar'
    if request.method == 'POST':
        nome = request.form['nome']
        sigla = request.form['sigla']
        local = request.form['local']

        e = Equipe(nome, sigla, local)
        if criar_equipe(e):
            return redirect('/admin')

    return render_template(
        'equipes_form.html',
        equipe=equipe,
        funcao=funcao,
        admin=True
    )

@admin_bp.route('/equipes/alterar/<sigla>')
def equipe_alterar(sigla):
    equipe = pegar_equipe(sigla)
    funcao = 'Alterar'

    return render_template(
        'equipes_form.html',
        equipe=equipe,
        funcao=funcao,
        admin=True
    )

@admin_bp.route('/equipes/deletar/<sigla>', methods=['GET','POST'])
def deletar_equipes(sigla):
    deletar_equipe(sigla)
    return redirect(
        '/admin/equipes'
    )

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

@admin_bp.route('/partidas/criar', methods=['GET', 'POST'])
def partidas_criar():
    funcao = 'Criar'
    if request.method == 'POST':
        time_casa = request.form['equipecasa']
        time_visitante = request.form['equipevisitante']
        pontos_casa = request.form['pontoscasa']
        pontos_visita = request.form['pontosvisitante'] 

        p = Partida(pegar_equipe(time_casa), pegar_equipe(time_visitante), pontos_casa, pontos_visita)

        if criar_partida(p):
            return redirect('/admin/partidas')
    equipes = pegar_equipe()

    return render_template(
        'partidas_form.html',
        equipes=equipes,
        funcao=funcao,
        partida=0,
        admin=True
    )

@admin_bp.route('/partidas/alterar/<sigla>')
def partida_alterar(sigla):
    partida = pegar_partida(sigla)
    funcao = 'Alterar'

    return render_template(
        'partidas_form.html',
        partida=partida,
        funcao=funcao,
        admin=True
    )

@admin_bp.route('/sair')
def sair():
    return redirect('/')