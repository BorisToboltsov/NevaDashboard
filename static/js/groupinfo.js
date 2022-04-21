// let groupInfo = document.querySelectorAll('.group')
//
// groupInfo.forEach(function (input) {
//     input.addEventListener("click", function (event) {
//         console.log(event.target.getAttribute('data-id'))
//     });
// });
window.onload = function () {
    $('.group').on('click', function () {
        let group = event.target;
        let group_a = group.getAttribute('data-id')
        $.ajax({
            url: "/group/detail_group/" + group_a + "/",
            success: function (data) {
                let url = "/group/detail_group/" + group_a + "/"
                $(location).attr('href', url);
            },
        });
        event.preventDefault();
    });
}