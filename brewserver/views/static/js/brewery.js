
function handleDeviceDrop(event, ui) {
    var clone = $(ui.draggable).clone();
    $(this).append(clone);
}

function handleTankName() {

}

function handleTankDrop(event, ui) {
    console.log('tank drop');
    var clone = $(ui.draggable).clone();
    if (clone.attr('id') != 'new-tank') {
        return;
    }
    var em = $('<div class="tank-holder">NEW TANK</div>');
    em.droppable({greedy:true, drop:handleDeviceDrop});
    $(this).append(em);
}

$(document).ready(function() {
    $( "#new-tank" ).draggable({ opacity: 0.7, helper: "clone" });
    $( ".config-device" ).draggable({ opacity: 0.7, helper: "clone" });
    $( "#brewery-holder" ).droppable({
        greedy:false,
	drop: handleTankDrop,
    });
});



