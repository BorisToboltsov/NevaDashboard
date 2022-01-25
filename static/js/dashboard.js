function createChart(e) {
    const days = document.querySelectorAll(".chart-values li");
    const tasks = document.querySelectorAll(".chart-bars li");
    const daysArray = [...days];

    tasks.forEach(el => {
        const duration = el.dataset.duration.split("#");
        const startDay = duration[0];
        const endDay = duration[1];
        let left = 0,
            width = 0;


        Date.prototype.addDays = function (days) {
            let dat = new Date(this.valueOf())
            dat.setDate(dat.getDate() + days);
            return dat;
        }

        function getDates(startDate, stopDate) {
            let dateArray = new Array();
            let currentDate = startDate;
            while (currentDate <= stopDate) {
                dateArray.push(currentDate.toISOString().split('T')[0])
                currentDate = currentDate.addDays(1);
            }
            return dateArray;
        }

        let groupDateArray = getDates(new Date(startDay), (new Date(endDay)));

        const filteredArrayStart = daysArray.filter(day => day.textContent === startDay);
        const filteredArrayEnd = daysArray.filter(day => day.textContent === endDay);

        if (filteredArrayEnd.length === 0 && filteredArrayStart.length === 0) {
            for (let i = 0; i < daysArray.length; i++) {
                if (groupDateArray.indexOf(daysArray[i].textContent) !== -1) {
                    left = daysArray[0].offsetLeft + daysArray[0].offsetWidth / 10 - left;
                    width = daysArray[daysArray.length - 1].offsetLeft + daysArray[daysArray.length - 1].offsetWidth / 10 - left;
                    break;
                } else {
                    if (i === daysArray.length - 1) {
                        el.remove();
                    }
                }
            }

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
        }
        el.style.left = `${left}px`;
        el.style.width = `${width}px`;
        if (e.type == "load") {
            el.style.backgroundColor = el.dataset.color;
            el.style.opacity = 1;
        }

    });
}

window.addEventListener("load", createChart);
window.addEventListener("resize", createChart);