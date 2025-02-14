from django.urls import path
from . import views

app_name="blog"

urlpatterns=[
    path("", views.index,name="index"),
    path("post/<str:slug>",views.detail,name="detail"),
    path("new_url_redirect",views.new_url_redirect,name="new_page_url"),
    path("old_url_redirect",views.old_url_redirect,name="old_url"),
    path("contacts",views.contacts,name="contact"),
    path("about",views.about,name="about")
]   