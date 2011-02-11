var droppedTank;
var editedDevice;

var deviceClasses = {
    'temperature': {'class':'pyrobot.brewery.devices:Thermometer', 'type':'sensors'},
    'volume': {'class': 'pyrobot.brewery.devices:TankGauge', 'type': 'sensors'},
    'stirrer': {'class': 'pyrobot.brewery.devices:Stirrer', 'type': 'devices'},
    'electric burner': {'class': 'pyrobot.brewery.devices:ElectricBurner', 'type': 'devices'},
    'cooler': {'class': 'pyrobot.brewery.devices:Cooler', 'type': 'devices'},
    'valve switch': {'class': 'pyrobot.brewery.devices:ValveSwitch', 'type': 'devices'},
};

var analogDevices = ['temperature', 'volume'];
var inputDevices = [];
var outputDevices = ['stirrer', 'electric burner', 'cooler', 'valve switch'];

var analogChannels = 0;
var intputChannels = 0;
var outputChannels = 0;

var setup = {
    'devices': {
    },
    'tanks': {
    },
};

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
    //$('#new-device-form').dialog('close');
}

function handleDeviceClick() {
    var em = $(this);
    editedDevice = em;
    $('input[name="channel"]').val(em.attr('channel'));
    $('#new-device-form').dialog({
	autoOpen: true,
	height: 180,
	width: 250,
	modal: true,
        close:function() {
            handleDeviceForm();
            return false;
        },
	buttons: {
	    "Ok": handleDeviceForm,
	    "Cancel": function() {
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
    var deviceDef = deviceClasses[name];
    var deviceClass = deviceDef['class'];
    var channel = getChannel(name);
    clone.attr('device-class', deviceClass);
    clone.attr('channel', channel);
    clone.click(handleDeviceClick);
    var tankName = $(this).attr('tankname');
    if (tankName == 'devices')
        setup[deviceDef['type']][name] = {'class': deviceClass, 'channel': channel};
    else 
        setup['tanks'][tankName][deviceDef['type']][name] = {'class': deviceClass, 'channel': channel};
    console.log(setup);
}

function handleTankName() {
    var tankName = $('#tank-name').val();
    $(this).dialog("close");
    var em = $('<div class="tank-holder" tankname="' + tankName + '"><h3>' + tankName + '</h3></div>');
    em.droppable({greedy:true, drop:handleDeviceDrop});
    $("#brewery-holder").append(em);
    setup.tanks[tankName] = {'sensors':{}, 'devices':{}};
    return false;
}

function handleTankDrop(event, ui) {
    droppedTank = $(ui.draggable).clone();
    if (droppedTank.attr('id') != 'new-tank') {
        return;
    }
    $('#new-tank-form').dialog('open');
    $('#tank-name').focus();
}

function addGlobalDevices() {
    var em = $('<div class="tank-holder" tankname="devices"><h3>Global Devices</h3></div>');
    em.droppable({greedy:true, drop:handleDeviceDrop});
    $("#brewery-holder").append(em);
}

$(document).ready(function() {
    $("#new-tank").draggable({opacity: 0.7, helper: "clone"});
    $(".config-device").draggable({opacity: 0.7, helper: "clone"});
    $("#brewery-holder").droppable({
        greedy:false,
	drop: handleTankDrop,
    });
    $('#new-tank-form').dialog({
	autoOpen: false,
	height: 180,
	width: 320,
	modal: true,
        close: function() {
            $('#tank-name').val( "" );
            return false;
        },
	buttons: {
	    "Ok": handleTankName,
	    "Cancel": function() {
                $('#tank-name').val( "" );
		$(this).dialog("close");
	    }
	},
    });
    $('#new-device-form').hide();
    addGlobalDevices();
});



