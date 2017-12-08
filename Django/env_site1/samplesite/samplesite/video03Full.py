# ---------- /polls/admin.py ----------

# 1 Django automates the interface used to add, change
# and delete content
# To create a user : python3 manage.py createsuperuser
# Username: admin
# Email address: db@compuserve.com
# Enter passwords

# 1 Run the server : python3 manage.py runserver
# Open localhost:8000/admin

# 1 Tell admin that our poll system has an admin interface
# in polls/admin.py

# 1 You can change any of the options and click History
# to see a list of the changes
# You can also add or delete questions

# 1 Now add more views in polls/views.py

from django.contrib import admin

# Register your models here.

# - Import Question
from .models import Question

# - Register Question for showing in admin
admin.site.register(Question)

# ---------- /polls/views.py ----------

from django.http import HttpResponse

# 7 Opens a 404 page if get doesn't supply a result
from django.shortcuts import get_object_or_404

# 2 Each view is represented by a function
# We'll create :
# index : Display the latest questions
# detail : Display the question and the choices
# results : Display question results

# - Original index function
'''
def index(request):
    return HttpResponse("You're in the polls index")
'''

# 4
# Import Question and Choice from our models file
from .models import Question, Choice

'''
# 4 New index function
def index(request):

    # 4 Receive a list of 5 questions ordered by date
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # 4 Cycle through the questions to create a list
    output = ', '.join([q.question_text for q in latest_question_list])

    # Return the text to display
    return HttpResponse(output)

'''

# 4 This isn't the best solution because the results are
# hard coded into the Python. Let's use a template to
# separate the design from the code
# Create a directory named templates in polls
# Create a directory named polls in the templates directory
# Create a file named index.html in that polls directory
# and create the template

# 6 Create a new index function that sends the question list
# to the template

# 6 Renders a page when it is passed a template and
# any data required by the template
from django.shortcuts import render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # 6 Define the name for the data to pass to the template
    context = {
        'latest_question_list': latest_question_list,
    }

    # 6 Render the page in the browser using the template
    # and data required by the template
    return render(request, 'polls/index.html', context)


# 2 add these 3 new views

'''
def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)
'''

'''
def results(request, question_id):
        response = "You're looking at the results of question %s"
        return HttpResponse(response % question_id)
'''

# 10 Let's update results() to show voting results
def results(request, question_id):

    # 10 Get the question id passed or 404
    question = get_object_or_404(Question, pk=question_id)

    # 10 Render the template
    return render(request, 'polls/results.html',
                  {'question': question})

# 10 Now create /templates/polls/results.html template

'''
def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)

# 7 Let's update detail to use a 404 page and template
'''

# 9 Now we will update vote() to except the choice picked

# 9 Used to avoid receiving data twice from a form if the user
# clicks the back button
from django.http import HttpResponseRedirect

# 9 Used to return a url we can point to based on the
# current question we are dealing with
from django.urls import reverse

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # 9 Try to get the selected radio button
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except(KeyError, Choice.DoesNotExist):

        # 9 Re-render the form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:

        # 9 If a choice was selected increment it in the DB
        selected_choice.votes += 1
        selected_choice.save()

        # 9 Protect from data being sent twice if user clicks back
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def detail(request, question_id):
    # 7 Check if the page exists, or display 404 page
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question})

# 7 Now create the detail.html template in templates/polls/

# 2 Add them to polls/urls.py


# ---------- /polls/urls.py ----------

from django.conf.urls import url

from . import views

# 3 Add a namespace so Django knows what directory to load
# if another app has views with the same name
app_name = 'polls'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # 3 Add the 3 views
    # The data surrounded by parentheses is sent to the function
    # ?P<question_id> defines the name for the data within
    # the parentheses
    # [0-9]+ says we will match 1 or more numbers
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

# 3 Now let's update polls/views.py

# ---------- /polls/templates/polls/index.html ----------

<!-- 5 If a list of questions is available create
an unordered list of the questions or print
that none are available -->
{% if latest_question_list %}
    <ul>
        {% for question in latest_question_list %}
            <li>
                <!-- 5 url defines directory to open based
                 on using the namespace defined in polls/urls.py
                 and the url defined in sampsite/urls.py -->
                <a href="{% url 'polls:detail' question.id %}">{{question.question_text}}</a>
            </li>
        {% endfor %}
    </ul>
{% else %}
    <p>No polls are available</p>
{% endif %}

<!-- 5 Back to polls/views.py to update index -->

# ---------- /polls/templates/polls/detail.html ----------

<!-- 8 Display the question passed and the choices
available -->

<h1>{{question.question_text}}</h1>

<!-- 8 Display error message -->
{% if error_message %}
<p><strong>{{error_message}}</strong></p>
{% endif %}

<!-- 8 Create a form which allows users to pick a choice -->
<!-- Point at the vote function in polls/views.py using
the namespace and pass the question id -->
<form action="{% url 'polls:vote' question.id %}" method="post">

<!-- 8 Protects your site from Cross Site Request Forgeries
which occur when another site tries to target your form -->
{% csrf_token %}

<!-- 8 Cycle through all choices for this question and
create a radio button for each -->
{% for choice in question.choice_set.all %}

    <!-- 8 When submitted the choice id is sent -->
    <input type="radio" name="choice"
           id="choice{{ forloop.counter }}"
           value="{{ choice.id }}" />

    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label>
    <br>

{% endfor %}

<input type="submit" value="Vote" />
</form>

<!-- 8 Now update the vote function in polls/views.py -->

# ---------- /polls/templates/polls/results.html ----------

<!-- 11 Displays choice results for the passed question -->

<h1>{{question.question_text}}</h1>

<!-- Cycle through all the choices for the question -->
<ul>
    {% for choice in question.choice_set.all %}
        <li>
            <!-- Add a s to vote if not 1 -->
            {{choice.choice_text}} -- {{choice.votes}} vote{{choice.votes|pluralize}}
        </li>
    {% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote Again</a>