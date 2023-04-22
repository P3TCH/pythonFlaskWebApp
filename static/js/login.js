function login(){
	username = document.getElementById("username").value;
	password = document.getElementById("password").value;

	fetch("/db_login", {
		method: "POST",
		headers: {
			"Content-Type": "application/json"
		},
		body: JSON.stringify({
			username: username,
			password: password
		})
	})
	.then(response => response.json())
	.then(data => {
		if(data.status === "success"){
			localStorage.setItem("token", username);
			window.location.href = "/redirect";
		}
		else{
			alert("Invalid username or password");
		}
	}
	);
}
