$(document).ready(main);

function main(){
    var degressiveMode = $('#profile-life-col select').val() == "*";
    $('select').on('change', CheckDegressiveProfileValue)
    $('#add-profile-button').on('click', ClickAddButton);
    AddButtonsToRows();

    if (!degressiveMode){
      $('#add-profile-button').removeClass('hide');
    }

    function CheckDegressiveProfileValue(){

        var lifeFieldIsDegressive = $('#profile-life-col select').val() == "*";
        var globalSelection = $('select option:selected:contains("*")');

        console.log(globalSelection.length)
        if (globalSelection.length == 1 && lifeFieldIsDegressive && degressiveMode == true) {
           console.log('off solo');
           UnsetDegressiveProfile();
        } else if (globalSelection.length >=1 && !lifeFieldIsDegressive && degressiveMode == true) {
           console.log('off all');
           UnsetDegressiveProfile(all=true);
        } else if (globalSelection.length >= 1 && degressiveMode == false) {
           console.log('on');
           SetDegressiveProfile();
        } else if (globalSelection.length == 0 && degressiveMode == true) {
           console.log('off');
           UnsetDegressiveProfile();
        }
    }

    function SetDegressiveProfile() {
         degressiveMode = true;

        //hide multiple profiles button
        $('#add-profile-button').addClass('hide');

        // re-select life
        $("#profile-life-col select").val('*');

        // remove extra forms
        $('#profiles_table_body').children().each(function (index) {
            if (index != 0)
                $(this).remove()
        })
        $('#id_profiles-TOTAL_FORMS').val($('#profiles_table_body').children().length);
    }

    function UnsetDegressiveProfile(all=false) {
        degressiveMode = false;

        //show multiple profiles button
        $('#add-profile-button').removeClass('hide');

        if (!all) {
            // re-select life
            var select = $("#profile-life-col select").val(0);
        } else {
            var selects = $(".degressive-value select");
            selects.each(function () {
                if ($(this).val() == "*")
                    $(this).val(0);
            });
        }
    }

    function AddButtonsToRows() {
        var rows = $('#profiles_table_body').children();

        rows.each(function (index) {
            var deleteButton = $('<a id="delete-button-' + index +'" class="btn-floating waves-effect waves-light black" href="javascript:void(0)" title="remove profile"><i class="material-icons">delete</i> </a>');
            var lastCell = $(this).children().last();

            if (index != 0){
                lastCell.empty();
                deleteButton.on('click', ClickRemoveButton);
                lastCell.append(deleteButton);
            }
        });
    }

    function ClickAddButton() {
        var tableBody = $('#profiles_table_body')
        var rows = tableBody.children();
        var newRow = rows.last().clone();

        tableBody.append(newRow);

        AddButtonsToRows();
        RenameIds($('#profiles_table_body').children());
        $('#id_profiles-TOTAL_FORMS').val($('#profiles_table_body').children().length);
    }

    function ClickRemoveButton() {
        $(this).parent().parent().remove()

        AddButtonsToRows();
        RenameIds($('#profiles_table_body').children());
        $('#id_profiles-TOTAL_FORMS').val($('#profiles_table_body').children().length);
    }

    function RenameIds(rows) {
        var fieldsSelector = 'input,select,textarea,label,div';
        rows.each(function (row_index) {
            var fields = $(this).find(fieldsSelector);
            fields.each(function (field_index) {
                renameElem($(this), row_index);
            });
        })
    }

    function renameElem (elem, index) {
        var idRegex = new RegExp('profiles-(\\d+)-');
        var replacement = 'profiles-' + index + '-';

        if (elem.attr("for")) elem.attr("for", elem.attr("for").replace(idRegex, replacement));
        if (elem.attr('id')) elem.attr('id', elem.attr('id').replace(idRegex, replacement));
        if (elem.attr('name')) elem.attr('name', elem.attr('name').replace(idRegex, replacement));
    }
}
