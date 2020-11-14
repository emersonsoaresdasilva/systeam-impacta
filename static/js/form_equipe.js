const form = document.querySelector('#formEquipe')
const submitBtn = form.querySelector('#btnSubmit')     
submitBtn.addEventListener("click", salvar)
function salvar(){
    if(validaCadastro()){
        form.submit()
    }
}
function validaCadastro(){
    //Campos
    let nome = form.querySelector('#campoNome')   
    let sigla = form.querySelector('#campoSigla')
    let local = form.querySelector('#campoLocal')
    //Avisos
    let avisoNome = form.querySelector('#avisoNome')
    let avisoSigla = form.querySelector('#avisoSigla')
    let avisoLocal = form.querySelector('#avisoLocal')

    valido = valida_vazio(nome, avisoNome) 
    valido = valida_vazio(local, avisoLocal) && valido
    valido = valida_sigla(sigla, avisoSigla) && valido

    return valido
   
}

function valida_sigla(sigla,aviso){
    if(sigla.value.length != 3){
        sigla.classList.add('is-invalid');
        aviso.innerText = "Campo sigla deve possuir exatamente 3 dígitos";
        return false
    }else{
        sigla.classList.remove('is-invalid');
        sigla.classList.add('is-valid');
        return true
    }
}

function valida_vazio(campo, aviso){
    if(campo.value == ""){
        campo.classList.add('is-invalid');
        aviso.innerText = "Campo obrigatório";
        return false
    }else{
        campo.classList.remove('is-invalid');
        campo.classList.add('is-valid');
        return true
    }
}

//Função para fazer errros de servidor desaparecer após um tempo
//setTimeout(function(){document.querySelector('.text-danger').style.display = 'none'}, 3000)