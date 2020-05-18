var dataset = []

var start = function(){
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
    $("#window1").empty()

    $.each(dataset, function(i, data_entry){
        var item = $("<div class='col-md-2 item'>");
        var redbtn = $("<button class='btn btn-danger'>");
        $(redbtn).text('X');
        $(redbtn).click(function(){
            delete_item(i)
        })
        var a = $("<a>")
        var href = "/view/" + data_entry["Id"]
        $(a).attr("href", href);
        var img = $("<img>")
        var src = data_entry["Poster"]
        $(img).attr("src", src)
        var li = $("<li>")
        $(li).text(data_entry["Rating"])
        var p1 = $("<p>")
        $(p1).text(data_entry["Title"])
        var p2 = $("<p>")
        $(p2).text(data_entry["Genre"])    
        a.append(img)
        a.append(li)
        a.append(p1)
        a.append(p2)
        item.append(a)
        item.append(redbtn)
        $("#window1").append(item)  
        $("#window1").append($("<div class='col-md-1'>"))        
    });  
}

$(document).ready(function(){
    start();
})

    
    