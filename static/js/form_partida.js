const form = document.querySelector('#formPartida')
const submitBtn = form.querySelector('#btnSubmit')     
submitBtn.addEventListener("click", salvar)
function salvar(){
    if(validaCadastro()){
        form.submit()
    }
}
function validaCadastro(){
    //Casa
    let equipeCasa = form.querySelector('#campoEquipeCasa')   
    let pontosCasa = form.querySelector('#campoPontosCasa')
    let avisoEquipeCasa = form.querySelector('#avisoEquipeCasa')
    let avisoPontosCasa = form.querySelector('#avisoPontosCasa')
    
    //Visitante
    let equipeVisita = form.querySelector('#campoEquipeVisitante')
    let pontosVisita = form.querySelector('#campoPontosVisitante')
    let avisoEquipeVisita = form.querySelector('#avisoEquipeVisitante')
    let avisoPontosVisita = form.querySelector('#avisoPontosVisitante')

    valido = valida_equipes(equipeCasa, avisoEquipeCasa, equipeVisita, avisoEquipeVisita)
    valido = valida_pontos(pontosCasa, avisoPontosCasa) && valido
    valido = valida_pontos(pontosVisita, avisoPontosVisita) && valido 

    return valido
   
}


function valida_pontos(pontos,aviso){
    if(pontos.value == ""){
        pontos.classList.add('is-invalid');
        aviso.innerText = "Campo obrigatório";
    }else if(parseInt(pontos.value) < 0){
        pontos.classList.add('is-invalid');
        aviso.innerText = "Número de gols inválido!"
    }else{
        pontos.classList.remove('is-invalid');
        pontos.classList.add('is-valid');
        pontos.value = String(parseInt(pontos.value) * 1);
        return true
    }
    return false
}

function valida_equipes(equipeCasa, avisoCasa, equipeVisita, avisoVisita){
    if (equipeCasa.value == equipeVisita.value){
        equipeCasa.classList.add('is-invalid');
        equipeVisita.classList.add('is-invalid');
        avisoCasa.innerText = "Equipes iguais";
        avisoVisita.innerText = "Equipes iguais";
        return false
    }
    return true
}
