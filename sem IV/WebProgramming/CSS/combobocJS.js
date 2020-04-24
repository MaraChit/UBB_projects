function insertValue(){
    var select = document.getElementById("name"),
        txtVal = document.getElementById("value").value,
        newOption = document.createElement("option"),
        newOptionVal = document.createTextNode(txtVal);

    if(txtVal == ""){
        alert("Empty field!");
        return;
    }
    newOption.appendChild(newOptionVal);
    select.insertBefore(newOption, select.firstChild);
}

function removeValue() {

    idName=document.getElementById("name");
    value = document.getElementById("name").selectedIndex;
    idName.removeChild(idName[value])
}