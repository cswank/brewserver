var burnerButton;
var timeoutId;
var historyTimeoutId;
var temperatureTarget;
var temperaturePlot;
var volumePlot;
var temperatureHistory = [];
var volumeHistory = [];
var mode = 'receive';
var counter = 0;
var historyStep = 5;

function handleSendCommand(data) {
    
}

function setThermometer(val) {
    
}

function handleThermometerChange(e, ui){
    args = {
        'command': 'set ' + name + ' target temperature',
        'kw': {'temperature': ui.value},
    };
    if (mode == 'receive')
        return;
    $.post(sendCommandUrl, JSON.stringify(args), handleSendCommand);
}

function handleThermometerSlide(e, ui){
    var val = ui.value;
    $("#thermometer-target-text").text(val.toFixed(1));
}

function handleVolumeSlide(e, ui){
    var val = ui.value;
    val = val/4.0;
    $("#volume-target-text").text(val.toFixed(2));
}

function handleVolumeChange(e, ui){
    args = {
        'command': 'set ' + name + ' target volume',
        'kw': {'volume': ui.value/4.0},
    };
    if (mode == 'receive')
        return;
    $.post(sendCommandUrl, JSON.stringify(args), handleSendCommand);
}

function makeButton(selector, handler) {
    var args = {'disabled': true};
    if (selector == '#mode-button')
        args = {'disabled': false};
    var em = $(selector);
    em.click(handler);
    em.button(args);
}

function toggleButton(button) {
    var on;
    if (button.attr('checked')) {
        button.button({'label': 'On'});
        on = true;
    }
    else {
        button.button({'label': 'Off'});
        on = false;
    }
    return on
}

function getOnArgs(em) {
    var args
    if (em.attr('id') == 'burner-button') {
        args = {
            'command': 'heat ' + name, 
            'kw': {'temperature': parseFloat($("#thermometer-target-text").text())},
        }
    }
    else if (em.attr('id') == 'cooler-button') {
        args = {
            'command': 'cool ' + name, 
            'kw': {'temperature': parseFloat($("#thermometer-target-text").text())},
        }
    }
    else if (em.attr('id') == 'stirrer-button') {
        args = {
            'command': 'stir ' + name, 
            'kw': {},
        }
    }
    else if (em.attr('id') == 'fill-valve-button') {
        args = {
            'command': 'fill ' + name,
            'kw': {'volume': parseFloat($("#volume-target-text").text())},
        }
    }
    return args
}

function getOffArgs(em) {
    var args
    if (em.attr('id') == 'burner-button') {
        args = {
            'command': 'stop heating ' + name, 
            'kw': {},
        }
    }
    else if (em.attr('id') == 'cooler-button') {
        args = {
            'command': 'stop cooling ' + name, 
            'kw': {},
        }
    }
    else if (em.attr('id') == 'stirrer-button') {
        args = {
            'command': 'stop stirring ' + name, 
            'kw': {},
        }
    }
    else if (em.attr('id') == 'fill-valve-button') {
        args = {
            'command': 'stop filling ' + name,
            'kw': {},
        }
    }
    return args
}

function handleButton() {
    var em = $(this);
    var on = toggleButton(em);
    var args;
    if (on)
        args = getOnArgs(em);
    else
        args = getOffArgs(em);
    $.post(sendCommandUrl, JSON.stringify(args), handleSendCommand);
}

function handleMode(data) {
    var em = $(this);
    if (em.attr('checked')) {
        em.button({'label': 'Send'});
        clearTimeout(timeoutId);
        mode = 'send';
        $('#thermometer-target').slider({'disabled': false});
        $('#volume-target').slider({'disabled': false});
        $('#burner-button').button({'disabled': false});
        $('#cooler-button').button({'disabled': false});
        $('#stirrer-button').button({'disabled': false});
        $('#fill-valve-button').button({'disabled': false});
    }
    else {
        em.button({'label': 'Receive'});
        $.get(stateUrl, handleState);
        mode = 'receive';
        $('#thermometer-target').slider({'disabled': true});
        $('#volume-target').slider({'disabled': true});
        $('#burner-button').button({'disabled': true});
        $('#cooler-button').button({'disabled': true});
        $('#stirrer-button').button({'disabled': true});
        $('#fill-valve-button').button({'disabled': true});
    }
}

function getState() {
    $.get(stateUrl, handleState);
}

function updatePlot(plot, data) {
    if (data == undefined)
        return;
    plot.setData([data]);
    plot.draw();
    plot.setupGrid();
}

function handleHistory(data) {
    updatePlot(volumePlot, data.volume);
    updatePlot(temperaturePlot, data.temperature);
    historyTimeoutId = setTimeout(getHistory, 1000 * 60);
 }

function getHistory() {
    $.get(historyUrl, handleHistory);
}

function handleNotification(data) {
    timeoutId = setTimeout(getState, 1000);
}

function handleState(stateData) {
    data = stateData.tanks[name];
    $('#thermometer-text').text(data.temperature.toFixed(1));
    $('#thermometer').progressbar({'value': data.temperature});
    $('#volume-text').text(data.volume.toFixed(2));
    $('#volume').progressbar({'value': data.volume});
    $('#burner-button').attr('checked', data.burner);
    $('#burner-button').button('refresh');
    toggleButton($('#burner-button'));
    $('#cooler-button').attr('checked', data.cooler);
    $('#cooler-button').button('refresh');
    toggleButton($('#cooler-button'));
    $('#stirrer-button').attr('checked', data.stirrer);
    $('#stirrer-button').button('refresh');
    toggleButton($('#stirrer-button'));
    $('#fill-valve-button').attr('checked', data.fill_valve);
    $('#fill-valve-button').button('refresh');
    toggleButton($('#fill-valve-button'));
    $('#thermometer-target').slider({'value': data.target_temperature});
    var val = data.target_temperature;
    if (val != undefined)
        val = val.toFixed(1);
    $('#volume-target-text').text(val);
    $('#thermometer-target-text').text(val);
    val = data.target_volume;
    $('#volume-target').slider({'value': val * 4.0});
    if (val != undefined)
        val = val.toFixed(2);
    $('#volume-target-text').text(val);
    if (stateData.waiting != undefined) {
        alert(stateData.waiting);
        $.post(notificationUrl, {'post_message':stateData.waiting}, handleNotification);
    }
    else
        timeoutId = setTimeout(getState, 1000);
}

function handleCalibrationOpen(){
    clearTimeout(timeoutId);
}

function handleCalibrationClose(){
    getState();
}

$(document).ready(function(){
    $('#calibration').dialog({
	modal: true,
        autoOpen: false,
        width: 700,
        height: 440,
        close: handleCalibrationClose,
        open: handleCalibrationOpen,
    });
    
    $('#thermometer').progressbar({'value':0});
    $('#thermometer-target').slider(
        {
            'animate': true,
            'step': 1,
            'slide': handleThermometerSlide,
            'change': handleThermometerChange,
            'disabled': true,
        }
    );

    $('#volume').progressbar({'value':0});

    $('#volume-target').slider(
        {
            'animate': true,
            'step': 1,
            'slide': handleVolumeSlide,
            'change': handleVolumeChange,
            'disabled': true,
        }
    );
    
    makeButton('#burner-button', handleButton);
    makeButton('#cooler-button', handleButton);
    makeButton('#stirrer-button', handleButton);
    makeButton('#fill-valve-button', handleButton);
    makeButton('#mode-button', handleMode);
    temperaturePlot = $.plot(
        $("#temperature-table"), 
        [{data: [], lines: { show: true }, points:{ show: true }}],
        {
            yaxis: {
                min: 0,
                max: 100,
        }
        });
    volumePlot = $.plot(
        $("#volume-table"), 
        [{data: [], lines: { show: true }, points:{ show: true }}],
        {
            yaxis: {
                min: 0,
                max: 10,
        }
        });
    $.get(stateUrl, handleState);
    $.get(historyUrl, handleHistory);
});



