from django.urls import path
from .views import *

app_name = 'algebra'

urlpatterns = [
	path('', home, name='home'),
	path('formulalar/', formulalar, name='formulalar'),
	path('misollar/', misollar, name='misollar'),
	path('about/', about, name='about'),
	path('hisob/', hisob, name='hisob'),
	path('faq/', faq, name='faq'),
	path('a/', a, name='a'),
	path('i/', i, name='i'),
	path('c/', c, name='c'),
	path('r/', r, name='r'),
	path('n/', n, name='n'),
	path('k/', k, name='k'),
	path('sodda/', c_1, name='c_1'),
	path('murakkab/', c_2, name='c_2'),
	path('soddar/', r_1, name='r_1'),
	path('murakkabr/', r_2, name='r_2'),
	path('soddan/', n_1, name='n_1'),
	path('murakkabn/', n_2, name='n_2'),


]