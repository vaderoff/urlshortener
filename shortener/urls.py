from django.urls import path
from .views import index, generate


urlpatterns = [
    path('<int:hash>', index),
    path('generate/<path:origin_url>', generate)
]