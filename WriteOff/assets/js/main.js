$(document).ready(function () {

    var is_open = false;
    var clone = $('#new_subject').prev().clone();
    $('#new_subject').click(function(e){
        if (!is_open) {
            is_open = true;
            $('#new_subject').text('choose from existing');
            $('#new_subject').prev().remove();
            $('#new_subject').before(
                '<input type="text" class="form-control" name="new_subject" id="id_new_subject" autocomplete="off" required>');
        }
        else {
            is_open = false;
            $('#new_subject').prev().remove();
            $('#new_subject').before(clone);
            $('#new_subject').text('add new subject');
        }
    });
});
