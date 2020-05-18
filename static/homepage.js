var dataset = []

var begin = function(){
    $.ajax({
        type: "POST",
        url: "/init",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(null),
        success: function(result){
            dataset = result["dataset"]
            display(dataset)
        },
        error: function(request, status, error){
            alert("Fail to init !")        
            console.log("Error")
            console.log(request)
            console.log(status)
            console.log(error)
        }    
    });          
}

var display = function(dataset){
    $("#window").empty()

    $.each(dataset.slice(-10), function(i, data_entry){
        var item = $("<div class='col-md-3 card'  style='width: 18rem;'>");
        var a = $("<a>")
        var href = "/view/" + data_entry["Id"]
        $(a).attr("href", href);
        var img = $("<img class='card-img-top' alt='Poster'>")
        var src = data_entry["Poster"]
        $(img).attr("src", src)
        var p1 = $("<h5 class='card-title'>")
        $(p1).text(data_entry["Title"])   
        a.append(img)
        a.append(p1)
        item.append(a)
        $("#window").append(item)  
        $("#window").append($("<div class='col-md-1'>"))        
    });  
}

$(document).ready(function(){
    begin();
})

    