function populate_term_search(terms) {
    $("#term_search").empty();
    $("#term_search").append("<option value=''></option>");
    $("#professor_search").empty();
    $("#professor_search").append("<option value=''></option>");
    var i;
    for(i = 0; i < terms.length; i++) {
	var term_string = terms[i]["year"]+ " " + terms[i]["quarter"];
	var year = terms[i]["year"];
	var quarter = terms[i]["quarter"];
	$("#term_search").append("<option value='" + year + "*"+quarter+ "'>"+term_string+"</option>");
    }
    $("#term_search").trigger("chosen:updated");
    $("#professor_search").trigger("chosen:updated");
}

function populate_professor_search(professor_and_lecture_num) {
    $("#professor_search").empty();
    $("#professor_search").append("<option value=''></option>");
    var i;
    for(i = 0; i < professor_and_lecture_num.length; i++) {
	var professor = professor_and_lecture_num[i]["professor"];
	var lecture_num = professor_and_lecture_num[i]["lecture_number"];
	$("#professor_search").append("<option value='" + professor + "*"+lecture_num+"'>"+professor+"</option>");
    }
    $("#professor_search").trigger("chosen:updated");    
}


function populate_class_search(classes) {
    $("#class_search").empty();
    $("#class_search").append("<option value=''></option>");
    var i;
    for(i = 0; i < classes.length; i++) {
	var class_string = classes[i]["major"]+ " " +classes[i]["course_number"];
	var major = classes[i]["major"];
	var course_number = classes[i]["course_number"];
	$("#class_search").append("<option value='" + major + "*" + course_number+"'>"+class_string+"</option>");
    }
    $("#class_search").trigger("chosen:updated");
}



function class_list() {

    var xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function() {
	if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            var classes = JSON.parse(xmlhttp.responseText);
            populate_class_search(classes);
	}
    }
    xmlhttp.open("GET", "get_class_list.php", true);
    xmlhttp.send();


    var on_class_change = function() {
	var element = $("#class_search").chosen().val();
	var major="";
	var course_number="";
	var i;
	for(i = 0; i < element.length; i++) {
	    if(element[i]!='*')
		major+=element[i];
	    else {
		i++;
		break;
	    }
	}
	for( ; i<element.length;i++) {
	    course_number+=element[i];
	}
	var xmlhttp2 = new XMLHttpRequest();

	xmlhttp2.onreadystatechange = function() {
	    if (xmlhttp2.readyState == 4 && xmlhttp2.status == 200) {
		var terms = JSON.parse(xmlhttp2.responseText);
		populate_term_search(terms);
	    }
	}
	
	var url = "get_term_list.php?major="+major+"&course_number="+course_number;
	xmlhttp2.open("GET", url, true);

	xmlhttp2.send();
    }

    var on_term_change = function() {
	var element = $("#class_search").chosen().val();
	var major="";
	var course_number="";
	var i;
	for(i = 0; i < element.length; i++) {
	    if(element[i]!='*')
		major+=element[i];
	    else {
		i++;
		break;
	    }
	}
	for( ; i<element.length;i++) {
	    course_number+=element[i];
	}

	element = $("#term_search").chosen().val();
	var year="";
	var quarter="";
	var i;
	for(i = 0; i < element.length; i++) {
	    if(element[i]!='*')
		year+=element[i];
	    else {
		i++;
		break;
	    }
	}
	for( ; i<element.length;i++) {
	    quarter+=element[i];
	}
	var xmlhttp2 = new XMLHttpRequest();

	xmlhttp2.onreadystatechange = function() {
	    if (xmlhttp2.readyState == 4 && xmlhttp2.status == 200) {
		var professor_and_lecture_num = JSON.parse(xmlhttp2.responseText);
		populate_professor_search(professor_and_lecture_num);
	    }
	}
	
	var url = "get_professor_list.php?major="+major+"&course_number="+course_number
	    +"&quarter="+quarter+"&year="+year;
	xmlhttp2.open("GET", url, true);

	xmlhttp2.send();
    }

    var on_professor_change = function() {
	var element = $("#class_search").chosen().val();
	var major="";
	var course_number="";
	var i;
	for(i = 0; i < element.length; i++) {
	    if(element[i]!='*')
		major+=element[i];
	    else {
		i++;
		break;
	    }
	}
	for( ; i<element.length;i++) {
	    course_number+=element[i];
	}

	element = $("#term_search").chosen().val();
	var year="";
	var quarter="";
	var i;
	for(i = 0; i < element.length; i++) {
	    if(element[i]!='*')
		year+=element[i];
	    else {
		i++;
		break;
	    }
	}
	for( ; i<element.length;i++) {
	    quarter+=element[i];
	}


	element = $("#professor_search").chosen().val();
	var professor=""; //not used in query
	var lecture_num="";
	var i;
	for(i = 0; i < element.length; i++) {
	    if(element[i]!='*')
		professor+=element[i];
	    else {
		i++;
		break;
	    }
	}
	for( ; i<element.length;i++) {
	    lecture_num+=element[i];
	}


	var xmlhttp2 = new XMLHttpRequest();

	xmlhttp2.onreadystatechange = function() {
	    if (xmlhttp2.readyState == 4 && xmlhttp2.status == 200) {
		var points = JSON.parse(xmlhttp2.responseText);
		populateChart(points);
	    }
	}
	
	var url = "get_class_data_over_time.php?major="+major+"&course_number="+course_number+"&year="+year+"&quarter="+quarter+"&lecture_number="+lecture_num;
	xmlhttp2.open("GET", url, true);

	xmlhttp2.send();
    }


    $("#class_search").chosen().change(on_class_change);
    $("#term_search").chosen().change(on_term_change);
    $("#professor_search").chosen().change(on_professor_change);
}
