from django.urls import path

from Photos.views.views import work

urlpatterns = [
    path('', work, name='work page')
]
