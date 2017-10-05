from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from dashboard.forms import LoginForm
from dashboard import urls as dashboard_url
from dashboard import views as core_views



urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.login, {'template_name': 'main/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^signup/$', core_views.signup, name="signup"),
    url(r'^dashboard/', include(dashboard_url, namespace='dashboard')),
]
