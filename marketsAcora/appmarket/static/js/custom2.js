var urlPersona = "/api/Persona/";
var edirId = 0;



validarPersona = function (formName,json) {
    formName.children('div').removeClass('text-danger');
    formName.find('select,input').removeClass('border-danger').addClass('border-primary');
    formName.find('small').html('');
    if(json.ap_paterno){
        formName.find('input[name=ap_paterno]').parent().addClass('text-danger');
        formName.find('input[name=ap_paterno]').siblings('small').html(json.ap_paterno[0]);
        formName.find('input[name=ap_paterno]').removeClass('border-primary').addClass('border-danger');
    }
    if(json.dni){
        formName.find('input[name=dni]').parent().addClass('text-danger');
        formName.find('input[name=dni]').removeClass('border-primary').addClass('border-danger');
        formName.find('input[name=dni]').siblings('small').html(json.dni[0]);
    }
    if(json.anterior){
        formName.find('input[name=anterior]').parent().addClass('text-danger');
        formName.find('input[name=anterior]').siblings('small').html(json.anterior[0]);
        formName.find('input[name=anterior]').removeClass('border-primary').addClass('border-danger');
    }
};

verPersona = function (id) {
    // window.open('/obstetrica/imprimir/'+id);
    $(location).attr('href','/obstetrica/imprimir/'+id);
};

function editarPersona(id) {
    edirId = id+'/';
    $("#editar_persona #validar").html('');
    $("#editar_persona input").removeClass('border-danger').addClass('border-primary');
    $('#editar_persona input').parent().removeClass('text-danger');
    $('#editar_persona input').siblings('small').html('');
    $.ajax({
        type: "GET",
        url: urlPersona+edirId,
        data: 'json',
        success: function(data)
        {
            $("#editar_persona input[name=ap_paterno]").val(data.ap_paterno);
            $("#editar_persona input[name=ap_materno]").val(data.ap_materno);
            $("#editar_persona input[name=nombre]").val(data.nombre);
            $("#editar_persona input[name=dni]").val(data.dni);
            $("#editar_persona select[name=sexo]").val(data.sexo);
            $("#editar_persona input[name=celular]").val(data.celular);
            $("#editar_persona input[name=correo_electronico]").val(data.correo_electronico);
            $("#editar_persona input[name=fecha_nacimiento]").val(data.fecha_nacimiento);
            $("#editar_persona input[name=direccion]").val(data.direccion);
            $("#editar_persona input[name=lugar_nacimiento]").val(data.lugar_nacimiento);
            $("#editar_persona input[name=ocupacion]").val(data.ocupacion);
            $("#editar_persona input[name=anterior]").val(data.anterior);
        },
        error: function (xhr, ajaxOptions, thrownError) {
            $("#editar_persona").find('#validar').append('<li>error ' + xhr.status +'</li>');
        }
    });
    $('#editPersona').modal('show');
}

$('#editar_persona').submit(function (event) {
    event.preventDefault();
    $("#editar_persona #validar").html('');
    $.ajax({
        type: "PUT",
        url: urlPersona+edirId,
        data: $("#editar_persona input,select").filter(function(index, element) { return $(element).val() != '';}).serialize(),
        success: function(data)
        {
           window.location.reload(true);
        },
        error: function (xhr, ajaxOptions, thrownError) {
            if(xhr.status === 400){
                validarPersona($('#editar_persona'), xhr.responseJSON);
            } else {
                $("#editar_persona").find('#validar').append('<li>error ' + xhr.status +'</li>');
            }
        }
    });
});

$('#form_persona').submit(function (event) {
    event.preventDefault();
    $('#form_persona').find('#validar').html('');
    $.ajax({
        type: "POST",
        url: urlPersona,
        data: $("#form_persona input,select").filter(function(index, element) { return $(element).val() != '';}).serialize(),
        success: function(data)
        {
           window.location.reload(true);
        },
        error: function (xhr, ajaxOptions, thrownError) {
            if(xhr.status === 400){
                validarPersona($('#form_persona'), xhr.responseJSON);
            } else {
                $("#form_persona").find('#validar').append('<li>error ' + xhr.status +'</li>');
            }
        }
    });
});

$('input').change(function (event) {
    $(this).removeClass('border-danger').addClass('border-primary');
    $(this).parent().removeClass('text-danger');
    $(this).siblings('small').html('');
});
