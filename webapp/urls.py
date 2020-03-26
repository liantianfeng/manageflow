from django.urls import path
from . import views

app_name = 'webapp'
urlpatterns = [
    path('',        views.index,  name='index'),
    path('index/',  views.index,  name='index'),
    path('login/',  views.login,  name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('about/',  views.about,  name='about'),
    path('terms/',  views.terms,  name='terms'),
    path('policy/', views.policy, name='policy'),
    path('faq/',    views.faq,    name='faq'),
    path('forgot/', views.forgot, name='forgot'),
    path('boards/', views.boards, name='boards'),
    path('detail/', views.detail, name='detail')
]