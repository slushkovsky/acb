var DAYS_IN_WEEK = 7;

/*  Working hours 
 * 
 *  Fields
 *  ------
 *  begin <Time>  Working day begining time
 *  end   <Time>  Working day ending time
 *  step  <int>   Bids step (in minutes)
 */

class WorkShedule {
    constructor(begin, end, step) {
        this.begin = begin; 
        this.end   = end; 
        this.step  = parseInt(step);
    } 

    getSteps() {
        var steps = [];
        var time = this.begin; 

        while(true) {
            steps.push(time);
        
            try {
                time = Time.sumTime(time, new Time(0, this.step));

                if (time.moreThan(this.end))
                    break;
            }
            catch (err) {
                break;
            }
        }

        return steps;
    }
}

var WORK_SHEDULE = new WorkShedule(new Time(9, 0), new Time(20, 0), 15);



/*  Setup table weekdays header
 * 
 *  Parameters
 *  ----------
 *  format <String>       Header format string (in PyFormat)
 *  days   <Array(dict)>  Days description
 */

function setWeekdaysHeader(format, days) {
    assert(days.length === DAYS_IN_WEEK, 'Unexpected week days count: ' + String(days.length));

    var headers = $('thead').children().children(); 

    assert(headers.length == DAYS_IN_WEEK + 1, 'Unexpend thead columns count'); // Days + time column

    for (var i in days) 
        headers.eq(parseInt(i) + 1).html(pyformat(format, days[i]));
}

/*  Add time row
 * 
 *  Parameters
 *  ----------
 *  time  <Time>  Days description.
 */

function addTimeRow(timeStr, visible) {
    $('tbody').loadTemplate($('#row-tmpl'), {
        time: timeStr
    }, {
        append: true,
        success: function() {
            if (visible === false)
                $('tbody').children()
                          .last()
                          .find('.time-col')
                          .css('color', 'transparent');
        }
    });
}

/*  Set busy time range.  
 *
 *  Parameters
 *  ----------
 *  begin  <Date>  Busy period begining time.
 *  end    <Date>  Budy period end time.
 */

function setBusyPeriod(begin, end) {

}



$(function() {
    var format_str = '<h5 class="text-center">{name}<br>{date.day}.{date.month}.{date.year}</h5>';
    var days_data = [
        {
            name: 'Понедельник', 
            date: {year: 2016, month: 6, day: 7}
        },
        {
            name: 'Вторник', 
            date: {year: 2016, month: 6, day: 8}
        }, 
        {
            name: 'Среда', 
            date: {year: 2016, month: 6, day: 9}
        }, 
        {
            name: 'Четверг', 
            date: {year: 2016, month: 6, day: 10}
        }, 
        {
            name: 'Пятница', 
            date: {year: 2016, month: 6, day: 11}
        },
        {
            name: 'Суббота',
            date: {year: 2016, month: 6, day: 12}
        }, 
        {
            name: 'Воскресенье', 
            date: {year: 2016, month: 6, day: 13}
        }
    ] 

    setWeekdaysHeader(format_str, days_data);

    var timeSteps = WORK_SHEDULE.getSteps();

    for (var i in timeSteps) 
        addTimeRow(timeSteps[i].toString(), i % 4 == 0);

    // $.ajax({
    //     url:, 
    //     method: 'GET', 
    //     success: function(data) {
    //         data = JSON ... 

    //         for .. in rest 
    //             setBusyPeriod(rest.begin, rest.end); 
    //     }, 
    //     error: function() {

    //     }
    // });
});
