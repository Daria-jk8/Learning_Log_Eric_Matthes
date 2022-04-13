"""defines the schematics URL for app --> leaning_logs"""

from django.urls import path
from .import views

app_name = 'learning_logs'
urlpatterns = [
    # --> HOME PAGE
    path('', views.index, name='index'),
    # --> PAGE list with topics
    path('topics/', views.topics, name='topics'),
    # --> PAGE for one topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]