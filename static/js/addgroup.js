"use strict"

let arrival_date_group = document.getElementById("arrival_date_group");
let departure_date_group = document.getElementById("departure_date_group");
let arrival_date_hotel = document.getElementById("arrival_date_hotel");

arrival_date_group.addEventListener("change", function () {
    document.getElementById("arrival_date_hotel").value = arrival_date_group.value;
    console.log(arrival_date_hotel.value)
});

departure_date_group.addEventListener("change", function () {
   document.getElementById("departure_date_hotel").value = departure_date_group.value;
});

arrival_date_hotel.addEventListener("change", function () {
   console.log(arrival_date_hotel.value)
});