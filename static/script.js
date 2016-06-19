function checkURL(){
    console.log("Script is running !")
    var x = document.forms['myForm']['inputURL'].value;
    if (x.substring(0,4) == "http"){
        return true;
    }
    else if (x.substring(0,3) == "www"){
        alert("Add 'http://' before your URL !")
        return false;
    }
    else
    {
        alert("Enter a valid URL !")
        return false;
    }
}