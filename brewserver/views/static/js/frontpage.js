

function handleState(data) {
    //data = JSON.parse(data);
    $('#hlt-temperature').text(data.hlt.temperature.toFixed(1));
    $('#hlt-volume').text(data.hlt.volume.toFixed(2));
    $('#tun-temperature').text(data.tun.temperature.toFixed(1));
    $('#tun-volume').text(data.tun.volume.toFixed(2));
    $('#boiler-temperature').text(data.boiler.temperature.toFixed(1));
    $('#boiler-volume').text(data.boiler.volume.toFixed(2));
    timeoutId = setTimeout(getState, 1000);
}

function getState() {
    $.get(stateUrl, handleState);
}

$(document).ready(function() {
    getState();
});



