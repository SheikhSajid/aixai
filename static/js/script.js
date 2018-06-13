$(document).ready(() => {
    // setup session cookie data. This is Django-related
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            let cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    let csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    // end session cookie data setup.

    $('.modal').on('submit', function (event) {
        event.preventDefault();
        let formData = $(event.target).serializeArray();
        let data = {};

        for (let entry of formData)
            data[entry.name] = entry.value;

        console.log(data);

        let submissionId = data['edit-submission-id'];
        let newName = data.name;

        $(`#modal${submissionId}`).modal('hide');

        $.ajax({
            method: 'PATCH',
            data,
            url: '/submissions/',
            success: () => $(`#submission-name-${submissionId}`).html(newName),
            error: () => alert('Oops! Could not change the submission record. Please try again later.')
        })
    });

    $('.text-danger').on('click', function (event) {
       let buttonId = event.target.id.split('-').pop();

       $.ajax({
           method: 'DELETE',
           data: { id: buttonId },
           url: '/submissions/',
           success: () => $(`#submission-${buttonId}`).remove(),
           error() { alert('Delete operation failed') }
       })
    });


    $('#new-status-form').submit(function (event) {
        event.preventDefault();
        let formData = new FormData(this);
        let formEntries = {};

        for (let entry of formData.entries()) {
            // entry = [name, value]
            formEntries[entry[0]] = entry[1];
        }

        let months = {
            0: 'January',
            1: 'February',
            2: 'March',
            3: 'April',
            4: 'May',
            5: 'June',
            6: 'July',
            7: 'August',
            8: 'September',
            9: 'October',
            10: 'November',
            11: 'December'
        };
        let d = new Date();
        let newStatusElement = `<div class="card mt-3">
                                <div class="card-header">
                                    ${$('#username').html()} <span class="text-muted">${months[d.getMonth()]} ${d.getDate()}, ${d.getFullYear()}, ${d.getHours()}:${d.getMinutes()}</span>
                                </div>
                                <div class="card-body">
                                    ${formEntries['status-body']}
                                </div>
                            </div>`;

        $.ajax({
            method: 'POST',
            data: formEntries,
            url: '/marketplace/status/',
            success: () => $('#posts').append(newStatusElement)
        })

    })
});

