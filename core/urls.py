from django.urls import path
from core.views import config_refresh

urlpatterns = [
    path('config/refresh/', config_refresh, name="config_refresh"),
]
