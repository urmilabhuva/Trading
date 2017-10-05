from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from forms import LoginForm

urlpatterns = [
	url(r'^login/$', login, {'template_name': 'main/login.html', 'authentication_form': LoginForm}),
	url(r'^$', views.home, name="home"),
	#url(r'^signup/$', views.SignUp.as_view(), name="signup" )




]