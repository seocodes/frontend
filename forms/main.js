function validateForm() {
    let name = document.getElementById("nome").value;
    if (name  == ""){
        alert('Nome não inserido.');
        return false;
    }
    return True;
}

