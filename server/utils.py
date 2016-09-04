from django.contrib import messages

def choices_max_lenght(choices): 
    return max(map(lambda choice: len(choice[0]), choices))

def flash_form_errors(request, form):
    HEADER_TMPL = 'Ivalid field <b>{field}</b>:'

    for field, problems in form.errors.as_data().items():
        header = HEADER_TMPL.format(field=field)
        prob_list = ['- ' + str(p.message) for p in problems]

        messages.error(request, '<br>'.join([header] + prob_list))
