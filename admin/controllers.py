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
    pontuacao = {}
    jogos = {}
    for e in equipes:
        pontuacao[e.sigla] = contar_pontos_da_equipe(e)
        jogos[e.sigla] = contar_jogos_da_equipe(e)

    return render_template( 
        'home.html',
        equipes=equipes,
        pontuacao=pontuacao,
        jogos=jogos,
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

@admin_bp.route('/sair')
def sair():
    return redirect('/')
