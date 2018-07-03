function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#image_upload_preview').attr('src', e.target.result);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }

    $("#uploadimg").change(function () {
        readURL(this);
    });
    $("#btn-upload").click(function () {

        var fx = new FormData();
        var file_data = $('input[type="file"]')[0].files; // for multiple files
        console.log(file_data);
        for (var i = 0; i < file_data.length; i++) {
            fx.append("file_" + i, file_data[i]);
        }
        console.log(fx);
        var form = $('form')[0];
        var fd = new FormData(form);
        var file_data = $('input[type="file"]')[0].files; // for multiple files

        fd.append("file", file_data);
        fd.append("option", option);
        fd.append("aux", aux);


        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:8000/Pm/scalarOperators/',
            data: fd,
            cache: false,
            contentType: false,
            processData: false,
            success: function (data) {
                console.log("Success");

                $("#image_result_preview").attr("src", "data:image/jpg;base64," + data)

            },
            error: function (data) {
                console.log("ERRORRR");
            }
        })
    });
    /**
 * Created by Maverick on 20/03/2018.
 */
