from django.urls import path
from .views import detail, getData

urlpatterns = [
    path('', detail, name = 'detail'),
    path('<int:prkey>', getData, name = 'getData')
]