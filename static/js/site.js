document.querySelectorAll('nav a').forEach(function(a){ 
if(a.href == window.location.href.split('?')[0]){
    a.classList.add('active')
}else{
    a.classList.remove('active')
}
})

setTimeout(function(){document.querySelector('.text-danger').style.display = 'none'},3000)