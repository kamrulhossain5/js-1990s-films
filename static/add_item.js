
var dataset = []
var data_entry = new Array()

 
var add_entry = function(data_entry){
    $.ajax({
        type: "POST",
        url: "/add_entry",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_entry),
        success: function(result){
            var Id = result["Id"];
            add_link(Id);
            alert("Add successfully !");

        },
        error: function(request, status, error){
            alert("Fail to add !")        
            console.log("Error")
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });    
}

var add_link = function(Id){
    var a = $("<a>");
    var href = "/view/" + Id;  
    $(a).attr("href", href);
    var p = $("<p>");
    $(p).text("link to the new item");
    $(a).append(p);
    $("#link").html(a);    
}

$(document).ready(function(){
    $("#add_form").unbind("click").submit(function(){
        var imdbId = $.trim($("input[name='imdbId']").val())
        var imdbLink = $.trim($("input[name='Imdb Link']").val())
        var title = $.trim($("input[name='Title']").val())
        var genre = $.trim($("input[name='Genre']").val())
        var poster = $.trim($("input[name='Poster']").val())
        var director = $.trim($("input[name='Director']").val())
        var actors = $.trim($("input[name='Actors']").val())
        var runtime = $.trim($("input[name='Runtime(Minutes)']").val())
        var rating = $.trim($("input[name='Rating']").val())
        var votes = $.trim($("input[name='Votes']").val())
        var revenue = $.trim($("input[name='Revenue(Millions)']").val())
        var metascore = $.trim($("input[name='Metascore']").val())
        var summary = $.trim($("input[name='Summary']").val())
        var no_error = true

        if (imdbId == '') {
            alert("imdbId cannot be empty")
            // $("input[name='imdbId']").val("")
            $("input[name='imdbId']").focus()
            no_error = false
        }
        if (!(imdbId == '') && !$.isNumeric(imdbId)) {
            alert("imdbId must be a number")
            // $("input[name='imdbId']").val("")
            $("input[name='imdbId']").focus()
            no_error = false
        }
        if (imdbLink == '') {
            alert("Imdb Link cannot be empty")
            // $("input[name='imdbId']").val("")
            $("input[name='Imdb Link']").focus()
            no_error = false
        }
        if (title == '') {
            alert("Title cannot be empty")
            // $("input[name='imdbId']").val("")
            $("input[name='Title']").focus()
            no_error = false
        }
        if (genre == '') {
            alert("Genre cannot be empty")
            // $("input[name='imdbId']").val("")
            $("input[name='Genre']").focus()
            no_error = false
        }
        if (poster == '') {
            alert("Poster cannot be empty")
            // $("input[name='imdbId']").val("")
            $("input[name='Poster']").focus()
            no_error = false
        }
        if (director == '') {
            alert("Director cannot be empty")
            // $("input[name='imdbId']").val("")
            $("input[name='Director']").focus()
            no_error = false
        }
        if (actors == '') {
            alert("Actors cannot be empty")
            // $("input[name='imdbId']").val("")
            $("input[name='Actors']").focus()
            no_error = false
        }
        if (runtime == '') {
            alert("Runtime cannot be empty")
            // $("input[name='imdbId']").val("")
            $("input[name='Runtime(Minutes)']").focus()
            no_error = false
        }
        if (!(runtime == '') && !$.isNumeric(runtime)) {
            alert("Runtime must be a number")
            // $("input[name='imdbId']").val("")
            $("input[name='Runtime(Minutes)']").focus()
            no_error = false
        }
        if (rating == '') {
            alert("Rating cannot be empty")
            // $("input[name='imdbId']").val("")
            $("input[name='Rating']").focus()
            no_error = false
        }
        if (!(rating == '') && !$.isNumeric(rating)) {
            alert("Rating must be a number")
            // $("input[name='imdbId']").val("")
            $("input[name='Rating']").focus()
            no_error = false
        }
        if (votes == '') {
            alert("Votes cannot be empty")
            // $("input[name='imdbId']").val("")
            $("input[name='Votes']").focus()
            no_error = false
        }
        if (!(votes == '') && !$.isNumeric(votes)) {
            alert("Votes must be a number")
            // $("input[name='imdbId']").val("")
            $("input[name='Votes']").focus()
            no_error = false
        }
        if (revenue == '') {
            alert("Revenue cannot be empty")
            // $("input[name='imdbId']").val("")
            $("input[name='Revenue(Millions)']").focus()
            no_error = false
        }
        if (!(revenue == '') && !$.isNumeric(revenue)) {
            alert("Revenue must be a number")
            // $("input[name='imdbId']").val("")
            $("input[name='Revenue(Millions)']").focus()
            no_error = false
        }
        if (metascore == '') {
            alert("Metascore cannot be empty")
            // $("input[name='imdbId']").val("")
            $("input[name='Metascore']").focus()
            no_error = false
        }
        if (!(metascore == '') && !$.isNumeric(metascore)) {
            alert("Runtime must be a number")
            // $("input[name='imdbId']").val("")
            $("input[name='Metascore']").focus()
            no_error = false
        }
        if (summary == '') {
            alert("Summary cannot be empty")
            // $("input[name='imdbId']").val("")
            $("input[name='Summary']").focus()
            no_error = false
        }

        if (no_error) {   
            var form_data = $("#add_form").serializeArray();
            $("#add_form")[0].reset();
            $("input[name='imdbId']").focus()
            add_entry(form_data);
        }
        return false;
    })
    
})