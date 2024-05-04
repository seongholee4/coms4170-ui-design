$(document).ready(function () {
    $("#submit_answer").click(function() {
        $.ajax({
            type: "POST",
            url: "/quiz/{{ question.quiz_id }}/check_answer",
            data: {
                answer: $('input[name="answer"]:checked').val(),
            },
            success: function(response) {
                console.log(response);
                if (response.correct) {
                    $("#feedback").html("<div class='alert alert-success'>Correct!</div>");
                } else {
                    $("#feedback").html("<div class='alert alert-primary'>" + response.message + "</div>");
                    if (response.feedback) {
                        $("#feedback").append("<div class='alert alert-info'>Hint: " + response.feedback + "</div>");
                    }
                }
            }
        });
    });

    $("#right_button").click(function () {
        if ("{{question.next_question}}" == "end") {
            window.location.href = "/quiz_results";
        } else {
            window.location.href = "/quiz/" + (parseInt("{{quiz_id}}")+1);
        }
    });

    $("#left_button").click(function () {
        if ("{{question.prev_question}}" == "start") {
            sessionStorage.removeItem('startTime');
            window.location.href = "/start_quiz";
        } else {
            window.location.href = "/quiz/" + (parseInt("{{quiz_id}}")-1);
        }
    });
});