function createChart(e) {
    const days = document.querySelectorAll(".chart-values li");
    const tasks = document.querySelectorAll(".chart-bars li");
    const daysArray = [...days];

    tasks.forEach(el => {
        const duration = el.dataset.duration.split("-");
        const startDay = duration[0];
        const endDay = duration[1];
        let left = 0,
            width = 0;

        

        const filteredArrayStart = daysArray.filter(day => day.textContent === startDay);
        const filteredArrayEnd = daysArray.filter(day => day.textContent === endDay);

        if (filteredArrayEnd.length === 0 && filteredArrayStart.length === 0) {
            // el.remove();
        } else {
            if (filteredArrayStart.length > 0) {
                left = filteredArrayStart[0].offsetLeft + filteredArrayStart[0].offsetWidth / 10;
            } else {
                left = daysArray[0].offsetLeft + daysArray[0].offsetWidth / 10 - left;
            }
            if (filteredArrayEnd.length > 0) {
                width = filteredArrayEnd[0].offsetLeft + filteredArrayEnd[0].offsetWidth / 10 - left;
            } else {
                width = daysArray[daysArray.length - 1].offsetLeft + daysArray[daysArray.length - 1].offsetWidth / 10 - left;
            }
            // apply css
            el.style.left = `${left}px`;
            el.style.width = `${width}px`;
            if (e.type == "load") {
                el.style.backgroundColor = el.dataset.color;
                el.style.opacity = 1;
            }
        }
    });
}

window.addEventListener("load", createChart);
window.addEventListener("resize", createChart);