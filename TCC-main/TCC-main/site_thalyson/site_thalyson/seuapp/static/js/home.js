// Criando card que surge ao passar o mouse em cima do icone de usuario

let userCard = document.getElementById("userCard");
let user = document.getElementById("user");
let btn = document.getElementById("btn");


// adicionando botao de up para top de pagina

let subir = document.getElementById("up");
subir.addEventListener("click", () => {
    window.scrollTo(top)
})

if(userCard && user && btn) {
    user.addEventListener("mouseover", () => {
        userCard.classList = "userCard open"
    })
    
    userCard.addEventListener("mouseover", () => {
        userCard.classList = "userCard open"
    })
    
    user.addEventListener("mouseout", () => {
        userCard.classList = "userCard"
    })
    
    userCard.addEventListener("mouseout", () => {
        userCard.classList = "userCard"
    })
    
    btn.addEventListener("click", () => {
        window.location.href = "/dologout/"
    })
}