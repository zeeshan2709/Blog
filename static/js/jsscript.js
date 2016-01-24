function login_validate(){
	var x = document.forms["logform"]["user"].value;
	var y = document.forms["logform"]["pass"].value;
	if(x == "" || y == "" || x == null || y == null){
		alert("Enter both username and password");
		return false;
	}
}

function post_validate(){
	var x = document.forms["postform"]["title"].value;
	var y = document.forms["postform"]["descrip"].value;
	var z = document.forms["postform"]["content"].value;
	if(x == "" || y == "" || z == "" || x == null || y == null || z == null){
		document.getElementById("pst").action="#";
		alert("All fields are compulsary!!!");
	} else 
		return confirm("Are you sure u want to submit it");
}