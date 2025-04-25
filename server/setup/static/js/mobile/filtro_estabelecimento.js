
function exibir_filtro() {

    var id_filtro = document.getElementById("filtro_id_mobile")

    id_filtro.style.display = "flex"

}

function fechar_filtro() {

var id_filtro = document.getElementById("filtro_id_mobile")

id_filtro.style.display = "none"

}

const value_distancia = document.querySelector("#value-distancia-filtro");
const input_distancia = document.querySelector("#value-distancia-filtro-mobile");
const value_preco = document.querySelector("#value-preco-filtro");
const input_preco = document.querySelector("#value-preco-filtro-mobile");

value_distancia.textContent = input_distancia.value;
input_distancia.addEventListener("input", (event) => {
value_distancia.textContent = event.target.value;
});

value_preco.textContent = input_preco.value;
input_preco.addEventListener("input", (event) => {
value_preco.textContent = event.target.value;
});