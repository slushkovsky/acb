// @flow

var PAGES = { // TODO: Autogenerate 
 	start: 0, 
	timepicker: 1, 
	datepicker: 2, 
	filters: 3, 
	found: 4
};
var NAVS_UPDATE_TIMEOUT = 1000;

var user_data = {
	mode: undefined,
	timestamp: undefined, 
	filters: undefined, 
}

var user_history = [0]; 
var history_index = 0;
var ready_to_roll = true;

function update_navs_visible() {
	var btn_prev = $('.active .btn-prev'); 
	var btn_next = $('.active .btn-next');


	if (history_index == 0) {
		btn_prev.hide(); 
		btn_prev.click(function(){
			console.error('[PAGES] Clicked on hided \'prev\' button');
		})
	}
	else {
    	btn_prev.show();
    	btn_prev.click(on_page_prev);
	}
   
    if (history_index == user_history.length - 1) {
    	btn_next.hide(); 
    	btn_next.click(function(){
			console.error('[PAGES] Clicked on hided \'next\' button');
		})
    }
    else {
    	btn_next.show();
    	btn_next.click(on_page_next);
    }

    ready_to_roll = true; 
}  

function __role_on(number) {
	if (!ready_to_roll)
		return;	

	$('#pages').carousel(number);
	
	ready_to_roll = false;

	setTimeout(update_navs_visible, NAVS_UPDATE_TIMEOUT);
}

function on_page(name) { 
	var page_number = PAGES[name]; 

	if (!page_number)
		console.error('[PAGE] Try to move on unexisted page \'' + name + '\'');

	if (history_index != user_history.length - 1) 
		user_history = user_history.slice(0, history_index + 1); 
	
	user_history.push(page_number);
	++history_index; 

	__role_on(page_number);
}

function on_page_prev() {
	if (!ready_to_roll)
		return;

	if (history_index == 0) 
		console.warn('[PAGES] Couldn\'t go on the previos page (always in the begin of history)'); 
	else if (history_index < 0) 
		console.error('[PAGES] Bad history_index (less than 0)');
	else
		__role_on(user_history[--history_index]); 
}

function on_page_next() {
	if (!ready_to_roll)
		return;

	if (history_index == user_history.length - 1) 
		console.warn('[PAGES] Couldn\'t go on the next page (always in the end of history)');
	else if (history_index > user_history.length - 1)
		console.error('[PAGES] Bad history_index (out of array)');
	else
		__role_on(user_history[++history_index])
}
