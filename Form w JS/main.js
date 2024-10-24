function mask(t, mask)
{
    var i = t.value.length;
    var exit = mask.substring(1,0);
    var text = mask.substring(i);
    if (text.substring(0,1) != exit)
    {
        t.value += text.substring(0,1);
    }
}

function validateForm() {
    alert('Formulário enviado com sucesso!');
    }

function resetQuestion(){
    confirm("Deseja apagar dados?");
}

// function validateEmail(field){
//     usuario = field.value.substring(0, field.value.indexOf("@"));
//     dominio = field.value.substring(field.value.indexOf("@") + 1, field.value.length);

//     if ((usuario.length >= 1) &&
//     (dominio.length >= 3) &&
//     (usuario.search("@") == -1) &&
//     (dominio.search("@") == -1) &&
//     (usuario.search(" ") == -1) &&
//     (dominio.search(" ") == -1) &&
//     (dominio.indexOf(".") >= 1) &&
//     (dominio.search(".") != -1) &&
//     (dominio.lastIndexOf(".") < dominio.length - 1)) {
//         alert("Email válido!");
//         return true;
//     }
//     else{
//         alert("Email inválido.")
//         return false;
//     }
// }