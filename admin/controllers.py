from flask import Blueprint, render_template, request, redirect, session, url_for
from database.funcoes import *
from classes import *

admin_bp = Blueprint(
    'admin',
    __name__,
    template_folder='templates'    
)

@admin_bp.route('/')
def home():
    if not 'usermail' in session:
        return redirect(url_for('website.home'))
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
    return redirect(
        '/equipes'
    )

@admin_bp.route('/equipes', methods=['GET','POST'])
def equipes():
    mensagens=[]
    if not 'usermail' in session:
        return redirect(url_for('website.home'))
    if request.args.get('acao'):
        mensagens.append(request.args.get('acao') + " com sucesso")
    equipes = pegar_equipe()
    return render_template( 
        'equipes.html',
        equipes=equipes,
        mensagens=mensagens,
        admin=True
    )

@admin_bp.route('/equipes/criar', methods=['GET', 'POST'])
def equipe_criar():
    erros = []
    if not 'usermail' in session:
        return redirect(url_for('website.home'))
    funcao = 'Criar'
    if request.method == 'POST':
        nome = request.form['nome']
        sigla = request.form['sigla']
        local = request.form['local']
        e = Equipe(nome, sigla, local)
        if criar_equipe(e):
            return redirect('/admin/equipes?acao=Criada')
        erros.append('Equipe já existe')
    return render_template(
        'equipes_form.html',
        equipe='',
        funcao=funcao,
        erros=erros,
        admin=True
    )

@admin_bp.route('/equipes/alterar/<sigla>', methods=['GET','POST'])
def equipe_alterar(sigla):
    erros=[]
    if not 'usermail' in session:
        return redirect(url_for('website.home'))
    funcao = 'Alterar'
    if request.method == 'POST':
        nome = request.form['nome']
        sigla = request.form['sigla']
        local = request.form['local']
        sigla_antiga = request.form['sigla_antiga']
        e = Equipe(nome, sigla, local)
        #if len(listar_partidas_da_equipe(sigla)) == 0:
        if alterar_equipe(sigla_antiga,e):
            return redirect('/admin/equipes?acao=Alterada')
        erros.append('Equipe já existe!')
        #erros.append("Não é possível alterar equipes que possuem vínculos com partidas!")       
    equipe = pegar_equipe(sigla)
    return render_template(
        'equipes_form.html',
        equipe=equipe,
        funcao=funcao,
        erros=erros,
        sigla_antiga=sigla,
        admin=True
    )

@admin_bp.route('/equipes/deletar/<sigla>', methods=['GET','POST'])
def deletar_equipes(sigla):
    erros=[]
    if not 'usermail' in session:
        return redirect(url_for('website.home'))
    if len(listar_partidas_da_equipe(sigla)) == 0:
        deletar_equipe(sigla)
    else:
        equipes = pegar_equipe()
        erros.append("Não é possível deletar equipes que possuem vínculos com partidas!")
        return render_template('equipes.html',equipes=equipes, erros=erros)   
    
    return redirect(
        '/admin/equipes?acao=Deletada'
    )

@admin_bp.route('/partidas', methods=['GET'])
def partidas():
    mensagens = []
    if not 'usermail' in session:
        return redirect(url_for('website.home'))
    if request.args.get('acao'):
        mensagens.append(request.args.get('acao') + " com sucesso")
    partidas = pegar_partida()
    return render_template( 
        'partidas.html',
        partidas=partidas,
        mensagens=mensagens,
        admin=True
        )

@admin_bp.route('/partidas/criar', methods=['GET', 'POST'])
def partidas_criar():
    erros = []
    if not 'usermail' in session:
        return redirect(url_for('website.home'))
    if request.method == 'POST':
        time_casa = request.form['equipecasa']
        time_visitante = request.form['equipevisitante']
        pontos_casa = request.form['pontoscasa']
        pontos_visita = request.form['pontosvisitante'] 
        if time_casa == time_visitante:
            erros.append('Um time não pode disputar com ele mesmo!')
        else:
            p = Partida(pegar_equipe(time_casa), pegar_equipe(time_visitante), pontos_casa, pontos_visita)

            if criar_partida(p):
                return redirect('/admin/partidas?acao=Criada')
            erros.append('Partida já existente (Casa x Visitante)')
    equipes = pegar_equipe()

    return render_template(
        'partidas_form.html',
        equipes=equipes,
        funcao='Criar',
        partida=Partida(None, None, 0, 0),
        equipe_casa=None,
        equipe_visita=None,
        erros=erros,
        admin=True
    )

@admin_bp.route('/partidas/alterar/<sigla>', methods=['GET','POST'])
def partida_alterar(sigla):
    erros = []
    if not 'usermail' in session:
        return redirect(url_for('website.home'))

    if request.method == 'POST':
        time_casa = request.form['equipecasa']
        time_visitante = request.form['equipevisitante']
        pontos_casa = request.form['pontoscasa']
        pontos_visita = request.form['pontosvisitante'] 
        id_partida_antiga = request.form['id_partida_antiga'] 
        
        if time_casa == time_visitante:
            erros.append('Um time não pode disputar com ele mesmo!')
        else:
            partida = Partida(pegar_equipe(time_casa), pegar_equipe(time_visitante), pontos_casa, pontos_visita)
            if alterar_partida(id_partida_antiga, partida):
                return redirect('/admin/partidas?acao=Alterada')
            erros.append("Partida já existente (Casa x Visitante)")
    #GET
    partida = pegar_partida(sigla)
    equipes = pegar_equipe() 
    equipe_casa = partida.equipe_casa
    equipe_visita = partida.equipe_visita
    return render_template(
        'partidas_form.html',
        equipe_casa=equipe_casa,
        equipe_visita=equipe_visita,
        equipes=equipes,
        partida=partida,
        id_partida_antiga=partida.id(),
        funcao='Alterar',
        erros=erros,
        admin=True
    )


    return redirect('admin/partidas/alterar/'+sigla)

@admin_bp.route('/partidas/deletar/<id>', methods=['GET','POST'])
def partida_deletar(id):
    avisos = []
    if not 'usermail' in session:
        return redirect(url_for('website.home'))
    deletar_partida(id)
    return redirect(
        '/admin/partidas?acao=Deletado'
    )

@admin_bp.route('/sair')
def sair():
    session.clear()
    return redirect('/')