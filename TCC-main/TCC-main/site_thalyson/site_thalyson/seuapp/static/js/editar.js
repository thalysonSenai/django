let input1 = document.getElementById("id_senha");
        input1.setAttribute("onkeyup", "confereSenha()");

        let input2 = document.getElementById("id_confirma_nova_senha");
        input2.setAttribute("onkeyup", "confereSenha()");

        function confereSenha() {
            let input1 = document.getElementById("id_senha");
            let senha2 = document.getElementById("id_confirma_nova_senha");
            let btn = document.getElementById("btn");

            let result = document.getElementById("result");

            if (input1.value != senha2.value || senha2.value != input1.value) {
                result.innerText = "As senhas não conferem"
                btn.disabled = true
            } else {
                result.innerText = ""
                btn.disabled = false
            }

            if (senha2.value == "") {
                result.innerText = ""
            }

            if (input1.value == "" || senha2.value == "") {
                btn.disabled = true
            }
        };

        // formatando inputs de senha para limitar o total de digitos

        let id_senha = document.getElementById("id_senha");
        let id_confirma_senha = document.getElementById("id_confirma_nova_senha");

        id_senha.setAttribute("maxlength", "16");
        id_confirma_senha.setAttribute("maxlength", "16")