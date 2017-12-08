# ---------- /polls/index.html ----------

<!-- 1 Aside from HTML that is defined in your templates
 you also need images, JavaScript, and CSS for generating
 web pages. We store those in the static directory. -->

<!-- 1 Create directory /polls/static/polls and define
style.css there -->

<!-- 3 Add the style sheet by pointing to the static directory-->
{% load static %}

<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}" />

<!-- 4 Create the directory /polls/static/polls/images and
save a repeating background image named background.png there -->

<!-- 4 Add the image as a background in style.css -->

{% if latest_question_list %}
    <ul>
        {% for question in latest_question_list %}
            <li>
                <a href="{% url 'polls:detail' question.id %}">{{question.question_text}}</a>
            </li>
        {% endfor %}
    </ul>
{% else %}
    <p>No polls are available</p>
{% endif %}

# ---------- /polls/static/polls/style.css ----------

/* 2 Change the text color of links in lists.
 Go to /polls/templates/polls/index.html to
 add the style sheet */

li a {
    color: green;
}

/* 5 Add the background */

body {
    background: white url("images/background.png");
}

/* 6 Now customize the admin page in /polls/admin.py */

# ---------- /polls/admin.py ----------

from django.contrib import admin

from .models import Question, Choice

# 9 Set up the Choice options on the Question page
# extra = 3 says to provide 3 extra choice options by
# default

# 9.a Change StackedInline to TabularInline to
# take up less space

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# 7 You can change the order of how items show up
# like this

class QuestionAdmin(admin.ModelAdmin):
    # 7 fields = ['pub_date', 'question_text']

    # 8 You can also break up the data in blocks
    ''' 9 Add choices to Question page
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]
    '''

    # 9 Updated fieldsets
    # collapse collapses a field by default
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    # 10 Change the Question list page to display the
    # date published and whether it is recent

    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # 11 Over to polls/models.py to fix was_published_recently

    # 14 Add a filter box that lets the user sort by
    # pub_date
    list_filter = ['pub_date']

    # 14 Allow the user to search by question text
    search_fields = ['question_text']

    # 15 Over to sampsite/settings.py to change the page title

# admin.site.register(Question)

# 7 Pass your change to register
admin.site.register(Question, QuestionAdmin)

# 9 Don't have Choice be on its own page
# admin.site.register(Choice)

# ---------- sampsite/settings.py ----------

Change Just this Part of Settings

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 16 Change 'DIRS': [], to
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 16 That well tell Django to look in the templates dir
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 17 Create a templates/admin directory in the dir that contains
# manage.py

WSGI_APPLICATION = 'sampsite.wsgi.application'

# 17 Find the current base_site.html template by typing
# this in your terminal
# python -c "import django; print(django.__path__)"
# Copy the contents of the file base_site.html in the directory
# templates

# ---------- sampsite/templates/admin/base_site.html ----------

{% extends "admin/base.html" %}

{% block title %}{{ title }} | {{ site_title|default:_('Django site admin') }}{% endblock %}

<!-- 18 Change this -->

<!--
{% block branding %}
<h1 id="site-name"><a href="{% url 'admin:index' %}">{{ site_header|default:_('Django administration') }}</a></h1>
{% endblock %}
-->

<!-- To this -->

{% block branding %}
<h1 id="site-name"><a href="{% url 'admin:index' %}">Polls Administration</a></h1>
{% endblock %}

{% block nav-global %}{% endblock %}

# ---------- /polls/models.py ----------

from django.db import models

import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)

    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()

        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # 12 Sort published recently based on pub_date
    was_published_recently.admin_order_field = 'pub_date'

    # 12 If boolean is true it will display an icon rather then value
    was_published_recently.boolean = True

    # 12 Change the description at the top of the table
    was_published_recently.short_description = 'Published Recently?'

    # 13 Back to polls/admin.py

class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text