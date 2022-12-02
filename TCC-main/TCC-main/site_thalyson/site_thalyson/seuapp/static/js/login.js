// comfigurando scripts da tela de login 

function confereSenha() {
    let senha1 = document.getElementById("id_senha");
    let senha2 = document.getElementById("id_confirma_senha");
    let btn = document.getElementById("btn");

    let result = document.getElementById("result");

    if(senha1.value != senha2.value || senha2.value != senha1.value) {
        result.innerText = "As senhas não conferem"
        btn.disabled = true
    } else {
        result.innerText = ""
        btn.disabled = false
    }

    if(senha2.value == "") {
        result.innerText = ""
    }

    if(senha1.value == "" || senha2.value == "") {
        btn.disabled = true
    }
}