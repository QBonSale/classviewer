var randomScalingFactor = function(){ return Math.round(Math.random()*100)};
var lineChartData = {
    labels : ["January","February","March","April","May","June","July"],
    datasets : [
	{
	    label: "My First dataset",
	    fillColor : "rgba(220,220,220,0.2)",
	    strokeColor : "rgba(220,220,220,1)",
	    pointColor : "rgba(220,220,220,1)",
	    pointStrokeColor : "#fff",
	    pointHighlightFill : "#fff",
	    pointHighlightStroke : "rgba(220,220,220,1)",
	    data : [randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor()]
	},
	{
	    label: "My Second dataset",
	    fillColor : "rgba(151,187,205,0.2)",
	    strokeColor : "rgba(151,187,205,1)",
	    pointColor : "rgba(151,187,205,1)",
	    pointStrokeColor : "#fff",
	    pointHighlightFill : "#fff",
	    pointHighlightStroke : "rgba(151,187,205,1)",
	    data : [randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor()]
	}
    ]

}

function populateChart(JSON_points) {
    var labels = [];
    var data = [];
    for(var i = 0; i < JSON_points.length; i++) {
	labels[labels.length] = JSON_points[i].snapshot_time;
	data[data.length] = parseInt(JSON_points[i].num_en);
    }
    dataset = {
	label: "Plot",
	fillColor : "rgba(151,187,205,0.2)",
	strokeColor : "rgba(151,187,205,1)",
	pointColor : "rgba(151,187,205,1)",
	pointStrokeColor : "#fff",
	pointHighlightFill : "#fff",
	pointHighlightStroke : "rgba(151,187,205,1)",
	data: data
    };
    //console.log(JSON_points);
    var ctx = document.getElementById("canvas").getContext("2d");
    console.log(dataset);
    var myLine = new Chart(ctx).Line({
	labels : labels,
	datasets: [dataset]}, {
	responsive: true
    });
}

function load_graph(){
    return;
    var ctx = document.getElementById("canvas").getContext("2d");
    var myLine = new Chart(ctx).Line(lineChartData, {
	responsive: true
    });
}
