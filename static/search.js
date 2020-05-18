var dataset = []
var data_entry = new Array()
var result = []

var search = function(input){
    $.ajax({
        type: "POST",
        url: "/search_input",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(input),
        success: function(result){
            console.log(result["result"])
            if (result["result"].length !== 0){
                alert("Found " + result["result"].length + " results!")
                dataset = result["result"]
                display(dataset)                
                }
            else{
                alert("Found 0 results!")
            }

        },
        error: function(request, status, error){
            alert("Not found !")        
            console.log("Error")
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });    
}

var delete_item = function(id){
    $.ajax({
        type: "POST",
        url: "/delete_item",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(id),
        success: function(result){
            dataset = result["result"]
            display(dataset)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });        
}

var display = function(dataset){
    $("#window").empty()
    
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
        $("#window").append(item) 
        $("#window").append($("<div class='col-md-1'>"))
    });  
}

$(document).ready(function(){
    $("#search_form").submit(function(){  
    var input = $("#input").val();

    search(input);
    return false;
    })
    
})