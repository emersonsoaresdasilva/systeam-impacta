from flask import Blueprint, render_template, request, redirect, url_for
from database.funcoes import *
from classes import *

website_bp = Blueprint(
    'website',
    __name__,
    template_folder='templates'    
)

@website_bp.route('/')
def home():
    carregar(Equipe)
    carregar(Partida)
    equipes = Equipe.listar()
    pontuacao = {}
    for e in equipes:
        pontuacao[e.sigla] = calcular_pontos(e)

    return render_template( 
        'home.html',
        equipes=equipes,
        pontuacao=pontuacao
        )

@website_bp.route('/detalhes/<sigla>')
def detalhes(sigla):
    return "PÁGINA DE DETALHES " + sigla

@website_bp.route('/entrar', methods=['GET', 'POST'])
def entrar():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        user = [x for x in USUARIOS if x.email == email][0]
        if user and user.senha == senha:
            return redirect('admin')
        return redirect('entrar')

    return render_template(
        'entrar.html'
    )