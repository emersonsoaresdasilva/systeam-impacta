var form = document.querySelector("#formPartida");
if (form.addEventListener) {                   
    form.addEventListener("submit", validaCadastro);
} else if (form.attachEvent) {                  
    form.attachEvent("onsubmit", validaCadastro);
}
 /*
function salvar(idForm){
    form = document.querySelector(idForm);
    if (valida_gols_casa(form) && valida_gols_visita(form) && valida_equipes(form)){
        form.submit()
    }    
}

function valida_gols_casa(form){
    //Validação de pontos casa
    let valido = false
    pontoscasa = form.querySelector('input#pontoscasa')
    pontoscasaAviso = form.querySelector('#pontoscasaAviso')
    if(pontoscasa.value == ""){
        pontoscasa.classList.add('is-invalid');
        pontoscasaAviso.innerText = "Campo obrigatório";
    }else if(parseInt(pontoscasa.value) < 0){
        pontoscasa.classList.add('is-invalid');
        pontoscasaAviso.innerText = "Número de gols da casa inválido!"
    }else{
        pontoscasa.classList.remove('is-invalid');
        pontoscasa.classList.add('is-valid');
        pontoscasa.value = String(parseInt(pontoscasa.value) * 1);
        valido = true
    }
    return valido
}

function valida_gols_visita(form){
    //Validação de pontos visitante
    let valido = false
    pontosvisita = form.querySelector('input#pontosvisitante')
    pontosvisitaAviso = form.querySelector('#pontosvisitanteAviso')
    if(pontosvisita.value == ""){
        pontosvisita.classList.add('is-invalid');
        pontosvisitaAviso.innerText = "Campo obrigatório"
    }else if(parseInt(pontosvisita.value) < 0){
        pontosvisita.classList.add('is-invalid');
        pontosvisitaAviso.innerText = "Número de gols do visitante inválido!"
    }else{
        pontosvisita.classList.remove('is-invalid');
        pontosvisita.classList.add('is-valid');
        pontosvisita.value = String(parseInt(pontosvisita.value) * 1);
        valido = true
    }
    return valido
}

function valida_equipes(form){
    if (form.querySelector('#equipecasa').value == form.querySelector('#equipevisitante').value){
        return false
    }else{
        return true
    }
}

// Função para capturar eventos
function captura_eventos( objeto, evento, funcao ) {
    // Testa se o navegador suporta addEventListener
    if ( objeto.addEventListener ) {
        // Adiciona addEventListener
        objeto.addEventListener( evento, funcao, true );
    } 
*/