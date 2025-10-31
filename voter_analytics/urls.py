from django.urls import path
from . import views

urlpatterns = [
    # Map the URL (empty string) to the view
    path('', views.VoterListView.as_view(), name='voters'),
    path('graphs', views.GraphsView.as_view(), name='graphs'),
]
