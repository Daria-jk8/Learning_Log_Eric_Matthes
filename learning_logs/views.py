from django.shortcuts import render
# Create your views here.
from .models import Topic

def index(request):
    """HOME PAGE app Learning LOG"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """show list of the topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """ show ONE topic and all info """
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added') 
    context ={'topics':topics, 'entries':entries}
    return render(request,  'learning_logs/topic.html', context)

