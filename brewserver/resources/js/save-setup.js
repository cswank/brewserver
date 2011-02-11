function handleSave() {
    
}

function handleSetup() {
    $.post(saveSetupUrl, JSON.stringify(setup), handleSave);
    return false;
}

$(document).ready(function() {
    $('#save-setup').click(handleSetup);
});



