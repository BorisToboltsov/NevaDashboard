"use strict"

let arrival_date_group = document.getElementById("arrival_date_group");
let departure_date_group = document.getElementById("departure_date_group");
let arrival_date_hotel = document.getElementById("arrival_date_hotel");

arrival_date_group.addEventListener("change", function () {
    document.getElementById("arrival_date_hotel").value = arrival_date_group.value;
});

departure_date_group.addEventListener("change", function () {
   document.getElementById("departure_date_hotel").value = departure_date_group.value;
});

// arrival_date_hotel.addEventListener("change", function () {
//    console.log(arrival_date_hotel.value)
// });

function setDefaultValue() {
        // Set default value for new forms
        $("input[type='number']").each(function () {
            if (!$(this).val()) {
                $(this).val(0).prop('disabled', true);
            };
        });
        // Renew current state structure
        $currentState = $(".formset_row").clone();
    };

$('.formset_row').formset({
        addText: 'добавить продукт',
        addCssClass: 'btn btn-outline-primary btn-block',
        prefix: 'orderitems',
        added: setDefaultValue,
        hideLastAddForm: true
    });