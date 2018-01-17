import re
import time
from time import gmtime
from calendar import timegm

from django.shortcuts import render

def index(request):
    return render(request, 'timestamp/index.html')

def service(request, time_string):
    pattern1 = re.compile(r'^(?P<timestamp>[1-9][0-9]+?)$')
    pattern2 = re.compile(r'^(?P<month>'
                          r'(Jan(?!uary)|Feb(?!uary)|Mar(?!ch)|'
                          r'Apr(?!il)|May|Jun(?!e)|'
                          r'Jul(?!y)|Aug(?!ust)|Sep(?!tember)|'
                          r'Oct(?!ober)|Nov(?!member)|Dec(?!ember)))'
                          r'-'
                          r'(?P<day>'
                          r'([1-9]|0[1-9]|[1-2][0-9]|3[0-1]))'
                          r'-'
                          r'(?P<year>'
                          r'[1-9][0-9]+$)')
    result1 = pattern1.search(time_string)
    result2 = pattern2.search(time_string)
    if result1:
        unix = int(result1.group('timestamp'))
        struct_time = gmtime(unix)
        natural = time.strftime('%b %d, %Y', struct_time)
        context = {
            "unix": unix,
            "natural": natural
        }
    elif result2:
        date_dict = result2.groupdict()
        date_dict['month'] = date_dict['month'][:3]
        natural = '{month} {day}, {year}'.format(**date_dict)
        struct_time = time.strptime(natural, '%b %d, %Y')
        unix = timegm(struct_time)
        context = {
            "unix": unix,
            "natural": natural
        }
    else:
        context = {
            "unix": None,
            "natural": None
        }
    return render(request, 'timestamp/service.html', context)
