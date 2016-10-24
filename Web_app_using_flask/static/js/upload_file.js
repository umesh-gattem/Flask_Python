$(document).ready(function() {
    $('#upload-file-btn').click(function() {
        var form_data = new FormData($('#upload-file')[0]);
        $.ajax({
            type: 'POST',
            url: '/upload',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: false,
            success: function(data) {
                alert("File uploaded Successfully")
                location.reload()
            },
            error :function(error) {
                alert("File should be 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'py', 'csv' extensions")
                location.reload()
            }
        });
    });
});