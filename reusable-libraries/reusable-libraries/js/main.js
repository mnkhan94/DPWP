(function(){
        document.getElementById("submit").onclick =
        function validateForm() {
            var x = document.forms["form"]["title"].value;
            var y = document.forms["form"]["artist"].value;
            var z = document.forms["form"]["link"].value;
            if (x=="" || y=="" || z=="") {
                //document.forms["form"]["wage"].value = 0;
                alert("Please, fill out all fields to add the song to your collection!");
                return false;
            }
        }
    
})();