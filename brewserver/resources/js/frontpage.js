var temperaturePlot;
var volumePlot;

function updateTemperaturePlot(data) {
    newData = [];
    for (var tank in data.tanks) {
        var history = tank.temperatureHistory;
        if (history != undefined)
            newData.push(history);
    }
    temperaturePlot.setData(newData);
    temperaturePlot.draw();
    temperaturePlot.setupGrid();
}

function updateVolumePlot(data) {
    newData = [];
    for (var i in data.tanks) {
        var tank = data[i];
        var history = tank.temperatureHistory;
        if (history != undefined)
            newData.push(history);
    }
    volumePlot.setData(newData);
    volumePlot.draw();
    volumePlot.setupGrid();
}

function handleNotification(data) {
    timeoutId = setTimeout(getState, 1000);
}

function handleState(data) {
    updateVolumePlot(data);
    updateTemperaturePlot(data);
    $('#hlt-temperature').text(data.hlt.temperature.toFixed(1));
    $('#hlt-volume').text(data.hlt.volume.toFixed(2));
    $('#tun-temperature').text(data.tun.temperature.toFixed(1));
    $('#tun-volume').text(data.tun.volume.toFixed(2));
    $('#boiler-temperature').text(data.boiler.temperature.toFixed(1));
    $('#boiler-volume').text(data.boiler.volume.toFixed(2));
    if (data.waiting != undefined) {
        alert(data.waiting);
        $.post(notificationUrl, {'post_message':data.waiting}, handleNotification);
    }
    else
        timeoutId = setTimeout(getState, 1000);
}

function getState() {
    $.get(stateUrl, handleState);
}

$(document).ready(function() {
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
    getState();
});



