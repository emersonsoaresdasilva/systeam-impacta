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
    equipes = Equipe.listar()
    return render_template( 
        'home.html',
        equipes=equipes,
        admin=True
        )

@admin_bp.route('/equipes')
def equipes():
    return "página de exibição das equipes"

@admin_bp.route('/equipes/<sigla>')
def equipe(sigla):
    return "página de exibição da equipe" + sigla 


@admin_bp.route('/sair')
def sair():
    return redirect('/')
