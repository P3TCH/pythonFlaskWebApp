function authen(){
	if(localStorage.getItem("token") === null){
		window.location.href = "/login";
	}
}

function clear_token(){
	localStorage.removeItem("token");
}
