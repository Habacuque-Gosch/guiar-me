
var titulo = document.getElementById("titulo-formulario")

var fields = document.getElementById("campo")
var fields_age = document.getElementById("campo-age")

var field_sexo = document.getElementById("sexo")

var field_img = document.getElementById("upload-img")


var contador = 0


function show_fields(){

    contador = contador + 1

    progress(contador)

    if (contador == 1)
    {
        fields.style.display = 'none';
        fields_age.style.display = 'none';
        field_sexo.style.display = 'flex';
        titulo.innerHTML = 'Como você se identifica?';
        // btn_avancar.style.display = 'none';
        // btn_entrar.style.display = 'flex';
    }

    if (contador == 2)
    {
        field_sexo.style.display = 'none';
        titulo.innerHTML = 'Coloque sua melhor foto!';
        field_img.style.display = 'flex'
    }

    console.log(contador)

    if (contador == 3)
    {
        document.getElementById("novo_perfil").submit();
    }

};
