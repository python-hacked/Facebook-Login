from django.urls import path,include
from. views import *


urlpatterns = [
        path('oauth/', include('social_django.urls', namespace='social')),  # <-- here
        path("",index)
]
