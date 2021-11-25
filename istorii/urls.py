from django.urls import path

from istorii.views import home

urlpatterns = [
    path('', view=home, name='home'),
]