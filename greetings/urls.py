from re import template
from django.urls import path
from .views import welcome, about, contact
from django.views.generic import TemplateView

urlpatterns = [
   path("", welcome, name="welcome"),
   path("about/", TemplateView.as_view(template_name="greetings/about.html"), name="about"),
   path("contact/", TemplateView.as_view(template_name="greetings/contact.html"), name="contact"),
]