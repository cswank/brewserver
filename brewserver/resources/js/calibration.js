var timeoutId;
var calPlot;
var device;

function handleCalibrationState(data) {
    $('#current-value').text(data.volume.toFixed(2));
    timeoutId = setTimeout(getCalibationState, 1000);
}

function getCalibationState() {
    $.get(stateUrl, handleCalibrationState);
}

function handleCalibrateClose(){
    clearTimeout(timeoutId);
}

function handleCurve(data) {
    calPlot = $.plot($("#calibration-table"),
           [{data: data.data, lines: { show: false }, points:{ show: true }}, {data:data.fit, points:{show:false}}], {
               grid: { hoverable: true, clickable: true },
           }
          );
    $("#calibration-table").bind("plotclick", function (event, pos, item) {
     
   if (item) {
            deletePoint(item.dataIndex);
        }
    });
    calPlot.draw();
}

function getCurve() {
    $.get(calibrationCurveUrl, {device:device}, handleCurve);
}


function handleCalibrate() {
    $('#calibration').dialog('open');
    device = $(this).attr('device');
    timeoutId = setTimeout(getCalibationState, 1000);
    getCurve();
}

function handleDelete(data) {
    console.log(data);
    if (data.error == undefined)
        getCurve();
    else
        alert(data.error);
}

function deletePoint(point) {
    $( "#dialog-confirm" ).dialog({
	resizable: false,
	height:140,
	modal: true,
	buttons: {
	    "Delete point": function() {
		$.get(deletePointUrl, {point:point, device:device}, handleDelete);
                $(this).dialog( "close" );
	    },
	    Cancel: function() {
		$(this).dialog( "close" );
	    }
	}
    });
}

function setCalibrationPoint() {
    data = {
        set_point:$('#calibration-point').val(),
        device:device,
    }
    $.get(savePointUrl, data, getCurve);
}

$(document).ready(function(){
    $( "#calibration").bind( "dialogclose", handleCalibrateClose);
    $('#calibrate-volume').click(handleCalibrate);
    $('#calibrate-temperature').click(handleCalibrate);
    $('#dialog-confirm').hide();
    $('#set-calibration-point').click(setCalibrationPoint);
});



