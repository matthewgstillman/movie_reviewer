from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^movies$', views.movies, name='movies'),
    url(r'^reviews$', views.reviews, name='reviews'),
    url(r'^register$', views.register, name='register'),
]