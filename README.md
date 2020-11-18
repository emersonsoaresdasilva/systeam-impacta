<h1 align="center">Controle de Campeonato <img src="https://i.imgur.com/VQNKvo4.gif" width="5%"></h1>

<img src="https://i.imgur.com/6JZU9Te.gif">

# Fazendo deploy

<code>virtualenv venv --python=python3</code> ⤵

<code>venv\Scripts\activate</code>

<code>pip install flask</code>

<code>python app.py</code> ✔

# Sobre o sistema

O objetivo é produzir um sistema de controle de campeonatos, com uma tabela de controle de resultados, detalhes de partidas por equipes, e todo o controle de cadastros de        novas equipes e partidas. 

Neste campeonato, um time consegue 3 pontos para cada vitória, 1 ponto para cada empate e 0 pontos por derrota. O número de vitórias é o primeiro critério de desempate.

# Tecnologias Utilizadas
O sistema é web, usando o microframework Flask no back-end, com cadastros em um banco de dados em arquivo e no front-end foi utilizado bootstrap.

# Resumo
O sistema possui duas partes: navegação e páginas principais do front-end e parte de cadastros (admin).

# Parte 1 - Navegação e Páginas Principais

- <b>A página inicial:</b> Mostra o resultado atual do campeonato, mostrando as equipes ordenadas pelo número de pontos (e sua posição nesse caso), mostrando também: número de     jogos, vitórias, empates e derrotas. Para cada equipe há um link para os detalhes de partidas deste time.

- <b>Detalhes da Equipe:</b> Mostra uma lista de todas as partidas que o time apareceu, com o resultado e estilos diferentes para partidas ganhas, empatadas e perdidas.

- <b>Entrar:</b> O formulário de login, que recebe um e-mail e uma senha para fazer o login.

# Parte 2 - Área Administrativa
- <b>Admin:</b> Área administrativa, que só pode ser acessada com o login feito, com caminhos para os cadastros de equipes e partidas, além do botão de sair (logout).
- <b>Equipes:</b> Listagem de todas as equipes cadastradas, mostrando o nome, sigla e local da equipe na lista, e botões de alteração e remoção da equipe. Além disso, na tela há   um botão de inclusão de nova equipe.
  - <b>Nova Equipe:</b> Formulário de criação de nova equipe, para coletar o nome, sigla e local da equipe. Botão salvar e limpar. Ao salvar volta para a listagem.
  - <b>Alterar Equipe:</b> Formulário de alteração da equipe, com os campos de nome, sigla e local já preenchidos e prontos para alteração. Botão salvar e limpar ao salvar volta   para a listagem.
    
  - <b>Remover Equipe:</b> Mostra uma janela de confirmação ao clicar em remover a equipe e volta para a tela de listagem.

- <b>Partidas:</b> Listagem de todas as partidas cadastradas, mostrando o nome, sigla e local de ambas as equipes na lista, com o resultados, e botões de alteração e remoção da    partida. Além disso, há um botão de inclusão de nova partida.

  - <b>Nova Partida:</b> Formulário de criação de nova partida, para coletar o time da casa, o visitante e os pontos de cada um. Botão salvar e limpar.  
    Ao salvar, volta para a listagem.
    
  - <b>Alterar Partida:</b> Formulário de alteração da partida, com os campos de time da casa, visitante e pontos de ambos já preenchidos e prontos para alteração.  
    Botão salvar e limpar ao salvar volta para a listagem.
    
  - <b>Remover Partida:</b> Mostra uma janela de confirmação ao clicar em remover a partida e volta para a tela de listagem.
