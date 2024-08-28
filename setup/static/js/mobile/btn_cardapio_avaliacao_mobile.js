
function show_reviews() {
            
    var id_cardapio = document.getElementById("hide-cardapio-mobile")
    var id_cardapio_btn = document.getElementById("btn-cardapio-mobile")
    var id_reviews = document.getElementById("hide-reviews-mobile")
    var id_reviews_btn = document.getElementById("btn-reviews-mobile")
    

    id_cardapio.style.display = 'none'
    id_cardapio_btn.className = 'btn-opcao-desativado-cardapio-mobile'
    id_reviews.style.display = 'flex'
    id_reviews_btn.className = 'btn-opcao-ativado-cardapio-mobile'


}

function show_produtos() {

    var id_cardapio = document.getElementById("hide-cardapio-mobile")
    var id_cardapio_btn = document.getElementById("btn-cardapio-mobile")
    var id_reviews = document.getElementById("hide-reviews-mobile")
    var id_reviews_btn = document.getElementById("btn-reviews-mobile")

    id_cardapio.style.display = 'flex'
    id_reviews.style.display = 'none'
    id_reviews_btn.className = 'btn-opcao-desativado-cardapio-mobile'
    id_cardapio_btn.className = 'btn-opcao-ativado-cardapio-mobile'

}