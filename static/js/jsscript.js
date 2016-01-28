function login_validate(){
	var x = document.forms["logform"]["user"].value.trim();
	var y = document.forms["logform"]["pass"].value.trim();
	if(x == "" || y == "" || x == null || y == null){
		alert("Enter both username and password");
		return false;
	}
}

function post_validate(){
	var x = document.forms["postform"]["title"].value.trim();
	var y = document.forms["postform"]["descrip"].value.trim();
	var z = document.forms["postform"]["content"].value.trim();
	if(x == "" || y == "" || z == "" || x == null || y == null || z == null){
		document.getElementById("pst").action="#";
		alert("All fields are compulsary!!!");
	} else 
		return confirm("Are you sure u want to submit it");
}