var droppedTank;
var editedDevice;

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
var outputDevices = ['Intermittent Stirrer', 'Electric Burner', 'Cooler', 'Fill Valve'];

var analogChannels = 0;
var intputChannels = 0;
var outputChannels = 0;

function getChannel(name) {
    var i = analogDevices.indexOf(name);
    var returnValue;
    if (i != -1) 
        return analogChannels++;
    i = outputDevices.indexOf(name); 
    if (i != -1)
        return outputChannels++;
    i = inputDevices.indexOf(name);
    if (i != -1)
        return inputChannels++;
}

function handleDeviceForm() {
    editedDevice.attr('channel', $('input[name="channel"]').val());
    editedDevice.attr('device-class', $('input[name="device-class"]').val());
    $('#new-device-form').dialog('close');
}

function handleDeviceClick() {
    var em = $(this);
    editedDevice = em;
    $('input[name="device-class"]').val(em.attr('device-class'));
    $('input[name="channel"]').val(em.attr('channel'));
    $('#new-device-form').dialog({
	autoOpen: true,
	height: 220,
	width: 750,
	modal: true,
        close:function() {
            $('#device-class').val('');
            $('#channel').val('');
        },
	buttons: {
	    "Ok": handleDeviceForm,
	    "Cancel": function() {
                $('#device-class').val("");
                $('#channel').val("");
		$(this).dialog("close");
	    }
	},
    });
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
    clone.click(handleDeviceClick);
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
    $('#new-device-form').hide();
});



