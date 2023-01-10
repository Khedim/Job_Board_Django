from django.urls import path
from .views import send_message

app_name = 'contact'
urlpatterns = [
	path('', send_message, name='contact'),
]
