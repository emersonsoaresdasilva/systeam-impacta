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
    equipes = pegar_equipe()
    dados = {}
    for e in equipes:
        dados[e.sigla] = obter_dados_da_equipe(e)
        
    return render_template( 
        'home.html',
        equipes=equipes,
        dados=dados
        )

@website_bp.route('/detalhes/<sigla>')
def detalhes(sigla):
    equipe = pegar_equipe(sigla)
    if equipe:
        return "PÁGINA DE DETALHES " + equipe.sigla
    return "Equipe não encontrada"

@website_bp.route('/entrar', methods=['GET', 'POST'])
def entrar():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        user = pegar_usuario(email, senha)
        if user and user.senha == senha:
            return redirect('admin')
        return redirect('entrar')#DEVE-SE INFORMAR AO USUARIO QUE ELE ERROU O USER OU SENHA
    #IF GET:
    return render_template(
        'entrar.html'
    )