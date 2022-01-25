let groupInfo = document.querySelectorAll('.group')

groupInfo.forEach(function (input) {
    input.addEventListener("click", function (event) {
        console.log(event.target.getAttribute('data-id'))
    });
});
