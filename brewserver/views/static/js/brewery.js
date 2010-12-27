var droppedTank;

var classes = {
    'Thermometer': 'pyrobot.brewery.devices:Thermometer',
    'Gauge': 'pyrobot.brewery.devices:TankGauge',
    'Intermittent Stirrer': 'pyrobot.brewery.devices:IntermittentStirrer',
    'Electric Burner': 'pyrobot.brewery.devices:ElectricBurner',
    'Cooler': 'pyrobot.brewery.devices:Cooler',
    'Fill Valve': 'pyrobot.brewery.devices:FillValve',
};

var analogDevices = ['Thermometer', 'Gauge'];
var inputDevices = [];
var outputDevices = ['IntermittentStirrer', 'Electric Burner', 'Cooler', 'Fill Valve'];

var analogChannels = 0;
var intputChannels = 0;
var outputChannels = 0;

function getChannel(name) {
    var i = analogDevices.indexOf(name);
    var returnValue;
    if (name != -1) 
        return analogChannels++;
    i = outputDevices.indexOf(name); 
    if (name != -1)
        return outputChannels++;
    i = inputDevices.indexOf(name);
    if (name != -1)
        return inputChannels++;
}

function handleDeviceDrop(event, ui) {
    var clone = $(ui.draggable).clone();
    if (clone.attr('id') == 'new-tank')
        return;
    $(this).append(clone);
    var name = $('a', clone).text();
    var deviceClass = classes[name];
    var channel = getChannel(name);
    clone.attr('device-class', deviceClass);
    clone.attr('channel', channel);
    clone.click(function(){$('#new-device-form').dialog('open')});
}

function handleTankName() {
    var tankName = $('#tank-name').val();
    $( this ).dialog("close");
    var em = $('<div class="tank-holder"><h3>' + tankName + '</h3></div>');
    em.droppable({greedy:true, drop:handleDeviceDrop});
    $("#brewery-holder").append(em);
    return false;
}

function handleTankDrop(event, ui) {
    droppedTank = $(ui.draggable).clone();
    if (droppedTank.attr('id') != 'new-tank') {
        return;
    }
    $('#new-tank-form').dialog('open');
}

function handleDeviceForm() {
    return false;
}

$(document).ready(function() {
    $( "#new-tank" ).draggable({ opacity: 0.7, helper: "clone" });
    $( ".config-device" ).draggable({ opacity: 0.7, helper: "clone" });
    $( "#brewery-holder" ).droppable({
        greedy:false,
	drop: handleTankDrop,
    });

    $('#new-tank-form').dialog({
	autoOpen: false,
	height: 300,
	width: 350,
	modal: true,
        close:function() {
                $('#tank-name').val( "" );
        },
	buttons: {
	    "Ok": handleTankName,
	    "Cancel": function() {
                $('#tank-name').val( "" );
		$( this ).dialog( "close" );
	    }
	},
    });
    $('#new-device-form').dialog({
	autoOpen: false,
	height: 300,
	width: 350,
	modal: true,
        close:function() {
            $('#device-class').val( "" );
            $('#channel').val( "" );
        },
	buttons: {
	    "Ok": handleDeviceForm,
	    "Cancel": function() {
                $('#device-class').val( "" );
                $('#channel').val( "" );
		$( this ).dialog( "close" );
	    }
	},
    });
});



