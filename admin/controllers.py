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
    carregar(Equipe)
    carregar(Partida)
    equipes = Equipe.listar()
    pontuacao = {}
    for e in equipes:
        pontuacao[e.sigla] = e.calcular_pontos(Partida.listar_da_equipe(e))

    return render_template( 
        'home.html',
        equipes=equipes,
        pontuacao=pontuacao,
        admin=True
        )


@admin_bp.route('/equipes')
def equipes():
    carregar(Equipe)
    equipes = Equipe.listar()
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
    carregar(Partida)
    partidas = Partida.listar()
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
