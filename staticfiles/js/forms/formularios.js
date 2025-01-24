

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

function show_pass(){

    var input_senha = document.getElementById("input-senha")

    if (input_senha.type == 'text')
        {
            input_senha.type = 'password'

        }
        
    else
    {
        input_senha.type = 'text'
    }
    
};

function show_pass_confirm(){

    var input_senha = document.getElementById("input-senha")

    var input_senha_confirma = document.getElementById("input-senha-confirma")

    input_senha_confirma_nova = document.getElementById("input-senha-confirma-nova")


    if (input_senha_confirma.type == 'text')
        {
            input_senha.type = 'password'
            input_senha_confirma.type = 'password'
            input_senha_confirma_nova.type = 'password'


        }
        
    else
    {
        input_senha.type = 'text'
        input_senha_confirma.type = 'text'
        input_senha_confirma_nova.type = 'text'
    }
    
};