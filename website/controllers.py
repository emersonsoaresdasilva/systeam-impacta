from flask import Blueprint, render_template, request, redirect
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
    equipes = Equipe.listar()
    return render_template( 
        'home.html',
        equipes=equipes
        )

@website_bp.route('/detalhes/<sigla>')
def detalhes(sigla):
    return "PÁGINA DE DETALHES " + sigla

@website_bp.route('/entrar', methods=['GET', 'POST'])
def entrar():
    if request.method == 'GET':
        return render_template('entrar.html')
    if request.method == 'POST':
        return redirect('/admin')