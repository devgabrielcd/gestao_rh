function utilizouHoraExtra(id){
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: "/horas-extras/utilizou-hora-extra/" + id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result) {
            console.log(result);
            $("#mensagem").text('Hora extra marcada como utilizada!');
            $("#horas_atualizadas").text(result.horas);
        }
    });
}

function process_response(funcionarios) {
    func_select = document.getElementById('funcionarios');
    func_select.innerHTML = "";

    funcionarios.forEach(function(funcionario){
        var option = document.createElement("option");
        option.text = funcionario.fields.nome;
        func_select.add(option);
    });
}

function filtraFuncionarios(){
    depart_id = document.getElementById("departamentos").value;

    $.ajax({
        type: 'GET',
        url: '/filtra-funcionarios/',
        data: {
            outro_param: depart_id
        },
        success: function(result) {
            console.log(result);
            process_response(result);
            $("#mensagem").text("Funcionarios Carregados");
        }
    });
}