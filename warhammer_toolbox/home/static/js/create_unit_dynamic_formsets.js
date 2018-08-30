$(document).ready(main);

function main() {
    var degressiveProfileRows = "[id^=degressive-row-display]";
    var degressiveMode = $('#profile-life-col select').val() === "*";
    var rows = $('#profiles_table_body').children().not(degressiveProfileRows);

    $('select').on('change', CheckDegressiveProfileValue);
    $('#add-profile-button').on('click', ClickAddButton);
    AddButtonsToRows();

    if (!degressiveMode) {
        $('#add-profile-button').removeClass('hide');
        $("#profile-life-col option[value='*']").addClass('hide');
        // if (rows.length > 1 ) {
        //     $(".degressive-value option[value='*']").addClass('hide');
        // }
    }
    RefreshDegressiveColsDisplay();


    function CheckDegressiveProfileValue() {
        var lifeFieldIsDegressive = $('#profile-life-col select').val() === "*";
        var degressiveSelection = $('select option:selected:contains("*")');

        if (degressiveSelection.length === 1 && lifeFieldIsDegressive && degressiveMode === true) {
            UnsetDegressiveProfile();
        } else if (degressiveSelection.length >= 1 && !lifeFieldIsDegressive && degressiveMode === true) {
            UnsetDegressiveProfile(all = true);
        } else if (degressiveSelection.length >= 1 && degressiveMode === false) {
            SetDegressiveProfile();
        } else if (degressiveSelection.length === 0 && degressiveMode === true) {
            UnsetDegressiveProfile();
        } else if (degressiveSelection.length >= 1) {
            RefreshDegressiveColsDisplay();
        }
    }

    function SetDegressiveProfile() {
        degressiveMode = true;

        //hide multiple profiles button
        $('#add-profile-button').addClass('hide');

        // change life value to '*'
        $("#profile-life-col select").val('*');

        // remove extra forms
        var rows = $('#profiles_table_body').children().not(degressiveProfileRows);
        rows.each(function (index) {
            if (index !== 0)
                $(this).remove()
        });
        $('#id_profiles-TOTAL_FORMS').val(1);

        RefreshDegressiveColsDisplay();
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

        RefreshDegressiveColsDisplay();
    }

    function RefreshDegressiveColsDisplay() {

        if (!degressiveMode) {
            $(degressiveProfileRows).addClass('hide');
            return
        } else
            $(degressiveProfileRows).removeClass('hide');

        var degressiveCols = $(".degressive-col");
        degressiveCols.each(function () {
            var split = $(this).attr('id').split('-');
            var fieldName = split[0];
            var fieldSelect = $("select[id$=" + fieldName + "]");
            if (fieldSelect.val() === '*'){
                $(this).addClass('grey lighten-5');
                $(this).find('select').removeClass('hide');
            } else {
                $(this).removeClass('grey lighten-5');
                $(this).find('select').addClass('hide');
            }
        });
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
        var tableBody = $('#profiles_table_body');
        var rows = tableBody.children().not(degressiveProfileRows);

        var newRow = rows.last().clone();
        ResetSelectValues(newRow);
        tableBody.append(newRow);

        AddButtonsToRows();
        rows = $('#profiles_table_body').children().not(degressiveProfileRows);
        RenameIds(rows);
        PatchHiddenFields(rows);
        $('#id_profiles-TOTAL_FORMS').val(rows.length);

        // hide all value '*' in dropdowns
        $(".degressive-value option[value='*']").addClass('hide');
    }

    function ClickRemoveButton() {
        $(this).parent().parent().remove()

        AddButtonsToRows();
        var profile_rows = $('#profiles_table_body').children().not(degressiveProfileRows);
        RenameIds(profile_rows);
        $('#id_profiles-TOTAL_FORMS').val(profile_rows.length);

        if (profile_rows.length === 1) {
            // show all value '*' in dropdowns
            $(".degressive-value option[value='*']").removeClass('hide');
        }
    }

    function ResetSelectValues(newRow) {
        selects = newRow.find('select');
        selects.each(function () {
           $(this).val('0');
        });
    }

    function PatchHiddenFields(rows) {
        if (!editMode)
            return;

        var hiddenFieldsList = $('#profiles_hidden_fields');
        rows.each( function (rowIndex) {
            var input = hiddenFieldsList.find('input[id="id_profiles-' + rowIndex + '-id"]');
            if (input.length === 0) {
                var idProfile = '<li> <input id="id_profiles-' + rowIndex + '-id" name="profiles-' + rowIndex + '-id" value="" type="hidden"> </li>';
                var foreignKeyUnit = ' <li> <input id="id_profiles-' + rowIndex + '-unit" name="profiles-' + rowIndex + '-unit" value="' + unitId + '" type="hidden"> </li>';
                hiddenFieldsList.append(idProfile);
                hiddenFieldsList.append(foreignKeyUnit);
            }
        });
    }

    function RenameIds(rows) {
        var fieldsSelector = 'input,select,textarea,label,div';
        rows.each(function (rowIndex) {
            var fields = $(this).find(fieldsSelector);
            fields.each(function () {
                renameElem($(this), rowIndex);
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
