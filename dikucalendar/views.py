from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.safestring import mark_safe
from django.utils.html import escape
from settings import *
from datetime import date, datetime, timedelta
from calendar import HTMLCalendar
from news.models import Article

def datetime_to_date(dt):
    if dt is not None:
        return date(dt.year, dt.month, dt.day)

class DIKUCalendar(HTMLCalendar):
    def __init__(self):
        self.events = Article.objects.all()
        super(DIKUCalendar, self).__init__()

    def formatday(self, day, weekday):
        if day == 0:
            return self.cell('')

        d = date(self.year, self.month, day)
        def in_range(article):
            start = datetime_to_date(article.event_start)
            end = datetime_to_date(article.event_end)
            if start is None and end is None:
                return False

            if start is not None and end is not None:
                return start <= d <= end

            if start is None:
                start = end
            return start == d
        
        events = filter(in_range, self.events)
        content = '<p>%s</p>' % day + '<ul>' + '\n'.join(map(self.format_article, events)) + '</ul>'
        return self.cell(content)

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(DIKUCalendar, self).formatmonth(year, month)

    @staticmethod
    def format_article(article):
        return '<li><a href="%s">%s</a></li>' % (article.url(), escape(article.title))
        
    @staticmethod
    def cell(data):
        return '<td>%s</td>' % data

def index(request):
    now = datetime.now()
    return calendar(request, now.year, now.month)

def calendar(request, year, month):
#    cal_html = DIKUCalendar().formatmonth(int(year), int(month))
    return render_to_response('calendar/index.html', RequestContext(request, {
        'active_tab': 'calendar',
#        'calendar': mark_safe(cal_html)
        }))
