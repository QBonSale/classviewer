function class_list() {


    var xmlhttp = new XMLHttpRequest();
    var url = "myTutorials.txt";

    xmlhttp.onreadystatechange = function() {
	if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            var classes = JSON.parse(xmlhttp.responseText);
            populate_class_search(classes);
	}
    }
    xmlhttp.open("GET", url, true);
    xmlhttp.send();

    function populate_class_search(classes) {
	search_bar=document.getElementById("class_search");
	var out = "";
	var i;
	for(i = 0; i < arr.length; i++) {
	    search_bar.innerHTML+="<option value='" + classes[i][major] + " " + classes[i][course_number] + "'></option>"
	}
    }

}
