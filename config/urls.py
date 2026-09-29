from django.urls import path

from visits.views import index

urlpatterns = [path('', index)]
