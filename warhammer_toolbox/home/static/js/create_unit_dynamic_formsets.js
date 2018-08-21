$(document).ready(main);

function main() {
    var degressiveProfileRows = "[id^=degressive-row-display]";
    var degressiveMode = $('#profile-life-col select').val() === "*";
    $('select').on('change', CheckDegressiveProfileValue)
    $('#add-profile-button').on('click', ClickAddButton);
    AddButtonsToRows();

    if (!degressiveMode) {
        $('#add-profile-button').removeClass('hide');
        $("#profile-life-col option[value='*']").addClass('hide')
    } else {
    }

    function CheckDegressiveProfileValue() {

        var lifeFieldIsDegressive = $('#profile-life-col select').val() === "*";
        var globalSelection = $('select option:selected:contains("*")');

        console.log(globalSelection.length)
        if (globalSelection.length === 1 && lifeFieldIsDegressive && degressiveMode === true) {
            console.log('off solo');
            UnsetDegressiveProfile();
        } else if (globalSelection.length >= 1 && !lifeFieldIsDegressive && degressiveMode === true) {
            console.log('off all');
            UnsetDegressiveProfile(all = true);
        } else if (globalSelection.length >= 1 && degressiveMode === false) {
            console.log('on');
            SetDegressiveProfile();
        } else if (globalSelection.length === 0 && degressiveMode === true) {
            console.log('off');
            UnsetDegressiveProfile();
        } else if (globalSelection.length >= 1) {
            HideAllDegressiveCols();
            ShowDegressiveCol();
        }
    }

    function SetDegressiveProfile() {
        degressiveMode = true;

        //hide multiple profiles button
        $('#add-profile-button').addClass('hide');

        // change life value to '*'
        $("#profile-life-col select").val('*');

        // remove extra forms
        var rows = $('#profiles_table_body').children().not(degressiveProfileRows)
        rows.each(function (index) {
            if (index !== 0)
                $(this).remove()
        });
        $('#id_profiles-TOTAL_FORMS').val(rows.length);

        // show and update degressive row
        $(degressiveProfileRows).removeClass('hide')
    }

    function UnsetDegressiveProfile(all=false) {
        degressiveMode = false;

        //show multiple profiles button
        $('#add-profile-button').removeClass('hide');

        // change life or all degressive values to '-'
        if (!all) {
            var select = $("#profile-life-col select").val(0);
        } else {
            var selects = $(".degressive-value select");
            selects.each(function () {
                if ($(this).val() === "*")
                    $(this).val(0);
            });
        }

        // hide degressive row
        $(degressiveProfileRows).addClass('hide');
    }

    function ShowDegressiveCol(){

    }

    function HideAllDegressiveCols(){

    }

    function AddButtonsToRows() {
        var rows = $('#profiles_table_body').children().not(degressiveProfileRows);

        rows.each(function (index) {
            var deleteButton = $('<a id="delete-button-' + index + '" class="btn-floating waves-effect waves-light black" href="javascript:void(0)" title="remove profile"><i class="material-icons">delete</i> </a>');
            var lastCell = $(this).children().last();

            if (index !== 0) {
                lastCell.empty();
                deleteButton.on('click', ClickRemoveButton);
                lastCell.append(deleteButton);
            }
        });
    }

    function ClickAddButton() {
        var tableBody = $('#profiles_table_body')
        var rows = tableBody.children().not(degressiveProfileRows);
        var newRow = rows.last().clone();

        tableBody.append(newRow);

        AddButtonsToRows();
        rows = $('#profiles_table_body').children().not(degressiveProfileRows)
        RenameIds(rows);
        $('#id_profiles-TOTAL_FORMS').val(rows.length);

        // hide all value '*' in dropdowns
        $(".degressive-value option[value='*']").addClass('hide');
    }

    function ClickRemoveButton() {
        $(this).parent().parent().remove()

        AddButtonsToRows();
        var body = $('#profiles_table_body');
        RenameIds(body.children().not(degressiveProfileRows));
        $('#id_profiles-TOTAL_FORMS').val(body.children().length);

        if (body.children().length === 1) {
            // show all value '*' in dropdowns
            $(".degressive-value option[value='*']").removeClass('hide');
        }
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

    function renameElem(elem, index) {
        var idRegex = new RegExp('profiles-(\\d+)-');
        var replacement = 'profiles-' + index + '-';

        if (elem.attr("for")) elem.attr("for", elem.attr("for").replace(idRegex, replacement));
        if (elem.attr('id')) elem.attr('id', elem.attr('id').replace(idRegex, replacement));
        if (elem.attr('name')) elem.attr('name', elem.attr('name').replace(idRegex, replacement));
    }
}
