$(document).ready(function(){
    var mark_as_deleted = false;
    $("#ratingInput").hide();
    $("#submit1").hide();
    $("#discard1").hide();
    $("#votesInput").hide();
    $("#submit2").hide();
    $("#discard2").hide();
    $("#edit1").click(function(){
        $("#redBtn1").hide();
        $("#rating").hide();
        $("#edit1").hide();
        $("#ratingInput").show();
        $("input[name='inputRating']").focus()
        $("#submit1").show();
        $("#discard1").show();
        $("#discard1").click(function(){
            $("#edit1").show();
            $("#submit1").hide();
            $("#discard1").hide();
            $("#ratingInput").hide();
            $("#rating").show();
            $("#redBtn1").show();
        })
        $("#rating_form").unbind("click").submit(function(){
            var inputRating = $.trim($("input[name='inputRating']").val())
            console.log(inputRating)
            $("#rating").show();
            $("#rating").append( ', ' + inputRating );
            $("#ratingInput").hide();
            $("#submit1").hide();
            $("#discard1").hide();
            $("#redBtn1").show();
            $("#edit1").show();
        })

    });
    $("#edit2").click(function(){
        $("#redBtn2").hide();
        $("#votes").hide();
        $("#edit2").hide();
        $("#votesInput").show();
        $("input[name='inputVotes']").focus()
        $("#submit2").show();
        $("#discard2").show();
        $("#discard2").click(function(){
            $("#edit2").show();
            $("#submit2").hide();
            $("#discard2").hide();
            $("#votesInput").hide();
            $("#votes").show();
            $("#redBtn2").show();
        })
        $("#votes_form").unbind("click").submit(function(){
            var inputVotes = $.trim($("input[name='inputVotes']").val())
            console.log(inputVotes)
            $("#votes").show();
            $("#votes").append( ', ' + inputVotes );
            $("#votesInput").hide();
            $("#submit2").hide();
            $("#discard2").hide();
            $("#redBtn2").show();
            $("#edit2").show();
        })

    });
    $("#undo1").hide();
    $("#undo2").hide();
    $("#redBtn1").click(function(){
        $("#edit1").hide();
        $("#rating").hide();
        $("#redBtn1").hide();
        $("#undo1").show();
        mark_as_deleted = false
    });
    $("#undo1").click(function(){
        $("#edit1").show();
        $("#rating").show();
        $("#redBtn1").show();
        $("#undo1").hide();
        mark_as_deleted = true
    });
    $("#redBtn2").click(function(){
        $("#edit2").hide();
        $("#votes").hide();
        $("#redBtn2").hide();
        $("#undo2").show();
        mark_as_deleted = false
    });
    $("#undo2").click(function(){
        $("#edit2").show();
        $("#votes").show();
        $("#redBtn2").show();
        $("#undo2").hide();
        mark_as_deleted = true
    });
});