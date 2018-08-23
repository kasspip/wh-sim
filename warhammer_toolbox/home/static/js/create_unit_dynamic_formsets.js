$(document).ready(main);

function main() {
    var degressiveProfileRows = "[id^=degressive-row-display]";
    var degressiveMode = $('#profile-life-col select').val() === "*";
    $('select').on('change', CheckDegressiveProfileValue)
    $('#add-profile-button').on('click', ClickAddButton);
    AddButtonsToRows();
    HideDegressiveCols();

    if (!degressiveMode) {
        $('#add-profile-button').removeClass('hide');
        $("#profile-life-col option[value='*']").addClass('hide')
    } else {
        ShowDegressiveCol();
    }

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
            HideDegressiveCols();
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
        var rows = $('#profiles_table_body').children().not(degressiveProfileRows);
        rows.each(function (index) {
            if (index !== 0)
                $(this).remove()
        });
        $('#id_profiles-TOTAL_FORMS').val(rows.length);

        // show degressive col
        ShowDegressiveCol();
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

        // hide degressive cols
        HideDegressiveCols();
        // hide degressive rows
    }

    function ShowDegressiveCol() {
        $(degressiveProfileRows).removeClass('hide');


        var selectedDegressiveSelects = $('select').has('option:selected:contains("*")');
        var degressiveRows = $(degressiveProfileRows);
        selectedDegressiveSelects.each(function () {
            var split = $(this).attr('id').split('-');
            var fieldName = split[split.length - 1];
            var tds = degressiveRows.find('[id^=' + fieldName + ']');
            tds.each(function () {
                if (!$(this).hasClass('grey lighten-5')) {
                    $(this).children('select').removeClass('hide');
                    $(this).addClass('grey lighten-5');
                }
            })
        });
    }

    function HideDegressiveCols() {

        var displayedCells = $("td.grey.lighten-5");

        displayedCells.each(function () {
            var split = $(this).attr('id').split('-');
            var fieldName = split[0];
            var fieldSelect = $("select[id$=" + fieldName + "]");

            if (fieldSelect.val() === '*'){
                if ($(this).parent().hasClass('grey lighten-5')) {
                    $(this).parent().removeClass('grey lighten-5');
                    $(this).addClass('hide');
                }
            }
        });
        $(degressiveProfileRows).addClass('hide');
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

        tableBody.append(newRow);

        AddButtonsToRows();
        rows = $('#profiles_table_body').children().not(degressiveProfileRows);
        RenameIds(rows);
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
