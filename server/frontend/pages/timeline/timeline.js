var DAYS_IN_WEEK = 7;
var DAY_BEGIN_TIME = Time('9:00 am');
var DAY_END_TIME = Time('8:00 pm');
var SHEDULE_MINUTES_STEP = 15;


/*  Working hours 
 * 
 *  Fields
 *  ------
 *  begin <Time>  Working day begining time
 *  end   <Time>  Working day ending time
 *  step  <Time>  Shedule minimum interval 
 */

function getSheduleIntervals(begin, end, step) {
    var steps = [];
    var time = begin;

    if (begin === undefined || end === undefined || step === undefined) {
        console.error('Missed required parameters'); 
        return;
    }

    while(true) {
        steps.push(Time(time.toString())); // Couldn't be simply .push(time) - thats reference
    
        if ((time.hours24() > end.hours24()) || 
            (time.hours24() == end.hours24() && time.minutes() > end.minutes())) {
            break;
        }

        if (!time.shift(0, step))
            break;
    }

    return steps;
}

/*  Creates time row (from template)
 *
 *  Parameters
 *  ----------
 *  data 
 */

function timeRow(data) {
    var tmpl = document.getElementById('row-tmpl');
    var element;

    if (tmpl === null) 
        console.error('Row template not found')

    for (selector in data) {
        element = tmpl.content.querySelector(selector)

        if (element === null)
            console.error('Nothing matched by selector: ' + selector);

        element.innerHTML = data[selector];
    }

    return document.importNode(tmpl.content, true);
}

/*  Set busy time range.  
 *
 *  Parameters
 *  ----------
 *  begin  <Date>  Busy period begining time.
 *  end    <Date>  Budy period end time.
 */

function addEvent(begin, end) {

}



$(function() {
    var intervals = getSheduleIntervals(DAY_BEGIN_TIME, DAY_END_TIME, SHEDULE_MINUTES_STEP);
    var formatStr = '<h5 class="text-center">{name}<br>{date.day}.{date.month}.{date.year}</h5>';

    $('thead').append(timeRow({
        '.mon': pyformat(formatStr, {name: 'Понедельник', date: {year: 2016, month: 9, day: 12}}),
        '.tue': pyformat(formatStr, {name: 'Вторник',     date: {year: 2016, month: 9, day: 13}}),
        '.wed': pyformat(formatStr, {name: 'Среда',       date: {year: 2016, month: 9, day: 14}}),
        '.thu': pyformat(formatStr, {name: 'Четверг',     date: {year: 2016, month: 9, day: 15}}),
        '.fri': pyformat(formatStr, {name: 'Пятница',     date: {year: 2016, month: 9, day: 16}}),
        '.sat': pyformat(formatStr, {name: 'Суббота',     date: {year: 2016, month: 9, day: 17}}),
        '.sun': pyformat(formatStr, {name: 'Воскресенье', date: {year: 2016, month: 9, day: 18}})
    }));

    for (var i in intervals) {
        $('tbody').append(timeRow({
            '.time': intervals[i].toString(), 
            '.mon': '',
            '.tue': '',
            '.wed': '',
            '.thu': '',
            '.fri': '',
            '.sat': '',
            '.sun': ''
        })); 
        
        if (i % 4 != 0)
            $('tbody').children().last().css('color', 'transparent'); 
    }
});
