

function voltar()
{
  history.back();
}

function progress(contador)
{
    var status_1 = document.getElementById("1")
    var status_2 = document.getElementById("2")
    var status_3 = document.getElementById("3")

    contador = contador + 1

    if (contador == 0)
    {
        status_1.style.background = "#005DDF";
    };

    if (contador == 2)
    {
        status_2.style.background = "#005DDF";
    };

    if (contador == 3)
    {
        status_3.style.background = "#005DDF";
    };

};