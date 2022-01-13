"use strict"

let modal = document.querySelector('.modal');
let btn_date = document.querySelector('.top_button_date');
let btn_apply = document.querySelector('.top_button_apply');
let btn_close = document.querySelector('.top_button_close');
let top_date = document.querySelectorAll('.top_date');
let tableSummary = document.querySelector('.table_summary');

let currentTime = (new Date()).getTime();

let row = 0;
let cell = 0;

let dateFrom = '';
let dateBefore = '';

let group1 = {
    name: 'Group1',
    dateB: '2022-01-10',
    dateE: '2022-01-13',
    days: 3,
    color: '#FF0000'
};

let group2 = {
    name: 'Group2',
    dateB: '2022-01-14',
    dateE: '2022-01-18',
    days: 3,
    color: '#FF69B4'
};

let group3 = {
    name: 'Group3',
    dateB: '2022-01-01',
    dateE: '2022-01-09',
    days: 3,
    color: '#ADFF2F'
};

let group4 = {
    name: 'Group4',
    dateB: '2022-01-08',
    dateE: '2022-01-13',
    days: 5,
    color: '#FF7F50'
};

let group5 = {
    name: 'Group5',
    dateB: '2022-01-06',
    dateE: '2022-01-16',
    days: 6,
    color: '#FFFF00'
};

let group6 = {
    name: 'Group6',
    dateB: '2022-01-05',
    dateE: '2022-01-09',
    days: 14,
    color: '#F0E68C'
};

let group7 = {
    name: 'Group7',
    dateB: '2022-01-10',
    dateE: '2022-01-13',
    days: 9,
    color: '#7FFFD4'
};

let group8 = {
    name: 'Group8',
    dateB: '2022-01-10',
    dateE: '2022-01-13',
    days: 9,
    color: '#DA70D6'
};

let group9 = {
    name: 'Group9',
    dateB: '2022-01-10',
    dateE: '2022-01-13',
    days: 9,
    color: '#0000CD'
};

let group10 = {
    name: 'Group10',
    dateB: '2022-01-10',
    dateE: '2022-01-13',
    days: 3,
    color: '#FFF8DC'
};

let group = [group1, group2, group3, group6, group10];
let groupTwo = [group1, group2];
group.sort((prev, next) => prev.days - next.days);
group.sort((prev, next) => Date.parse(prev.dateB) - Date.parse(next.dateB));

groupTwo.sort((prev, next) => prev.days - next.days);
groupTwo.sort((prev, next) => Date.parse(prev.dateB) - Date.parse(next.dateB));

// Предположим что у нас 4 групп
// 1 группа: даты с 01.11.2021 по 07.11.2021
// 2 группа: даты с 08.11.2021 по 12.11.2021
// 3 группа: даты с 13.11.2021 по 20.11.2021
// 4 группа: даты с 21.11.2021 по 26.11.2021


function randColor() {
    /*СОЗДАЕМ ПЕРЕМЕННЫЕ
    r,g,b - отвечают за кодировку и вместе выводят цвет
    color - в нее записываем полную строку значения цвета
    */
    let r = Math.floor(Math.random() * (256));
    let g = Math.floor(Math.random() * (256));
    let b = Math.floor(Math.random() * (256));
    let color = '#' + r.toString(16) + g.toString(16) + b.toString(16);
    return color;
}

function markedCell(groupMassive) {
    let cellTd = document.querySelectorAll(`td[data-row="${row - 1}"]`);
    let massive = [];
    let state = false;
    let cellColor = randColor();
    let endMassive = [];
    var a = 0;
    var b = 0;
    for (let index = 0; index < groupMassive.length; index++) {
        let massiveCell = [];
        a = Date.parse(groupMassive[index].dateB);
        b = Date.parse(groupMassive[index].dateE);
        for (let j = 0; j < cellTd.length; j++) {
            // parse.Date переводит дату как "дата 3:00 ночи", 10800000 мс это - 3 часа и 75599000 мс это + 21:59:59
            if (cellTd[j].getAttribute('data-date') >= a - 10800000 && cellTd[j].getAttribute('data-date') <= b + 75599000) {
                if (cellTd[j].getAttribute('data-marked') == 'true') {
                    if (state == false) {
                        tableBody(Number(cellTd[0].getAttribute('data-date')), Number(cellTd[cellTd.length - 1].getAttribute('data-date')));
                        state = true;
                    }
                    massive.push(...groupMassive.splice(index, 1));
                    continue;
                }
                massiveCell.push(cellTd[j]);
                cellTd[j].setAttribute('data-marked', true);
                cellTd[j].setAttribute('data-group', groupMassive[index].name);
            }
        }
        if (massiveCell.length > 0) {
            endMassive.push([groupMassive[index], massiveCell]);
        }
    }
    for (let index = 0; index < endMassive.length; index++) {
        for (let j = 0; j < endMassive[index][1].length; j++) {
            endMassive[index][1][j].style.backgroundColor = endMassive[index][0].color;
        }
    }
    console.log(endMassive)
    if (massive.length > 0) {
        markedCell(massive);
    }
}

function tableHeading(dateBegin, dateEnd) {
    let trHead = document.createElement('tr');
    for (let index = dateBegin; index < dateEnd + 86400000; index += 86400000) {
        let a = new Date(index);
        let thHead = document.createElement('th');
        thHead.innerHTML = `${a.getDate()}.${a.getMonth() + 1}`;
        trHead.appendChild(thHead);
    }
    tableSummary.appendChild(trHead);
}

function tableBody(dateBegin, dateEnd) {
    let tr = document.createElement('tr');
    for (let index = dateBegin; index < dateEnd + 86400000; index += 86400000) {
        let td = document.createElement('td');
        td.setAttribute('data-date', index);
        td.setAttribute('data-marked', false);
        td.setAttribute('data-row', row);
        td.setAttribute('data-cell', cell);
        cell++
        td.classList.add('td');
        tr.appendChild(td);
    }
    tableSummary.appendChild(tr);
    row++;
}

let currentTimeEnd = currentTime + 1522800000; // + 18 дней 1522800000
let currentTimeBegin = currentTime - 604800000; // - 7 дней 604800000

tableHeading(currentTimeBegin, currentTimeEnd);
tableBody(currentTimeBegin, currentTimeEnd);
markedCell(group);

btn_date.addEventListener("click", function () {
    modal.style.display = "block";
});

btn_apply.addEventListener("click", function () {
    tableSummary.innerHTML = "";
    if ((dateFrom != '' && dateBefore != '') && (dateFrom < dateBefore)) {
        tableHeading(dateFrom, dateBefore);
        tableBody(dateFrom, dateBefore);
        markedCell(groupTwo);
        // modal.style.display = "none";
    } else {
        alert('Необходимо заполнить даты.');
    }
});

top_date.forEach(function (input) {
    input.addEventListener("input", function (event) {
        if (event.target.classList.contains("dateFrom")) {
            dateFrom = Date.parse(event.target.value);
        } else if (event.target.classList.contains("dateBefore")) {
            dateBefore = Date.parse(event.target.value);
        }
    });
});

btn_close.addEventListener("click", function () {
    modal.style.display = "none";
});