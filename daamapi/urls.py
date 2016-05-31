"""daamapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from pinpointhint import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
#router.register(r'pins', views.PinsGeoJson)

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^pinsgeojson/$', views.PinsGeoJson.as_view(), name='pins-geojson'),
    url(r'^pinsgeojson/(?P<pk>\d+)/$', views.PinsGeoJsonDetail.as_view(), name='pins-detail'),


    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'helpdesk/', include('helpdesk.urls')),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        name='auth_login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login',
        name='auth_logout'),
    url(r'^accounts/password-change/$',
        'django.contrib.auth.views.password_change',
        name='change_password'),
    url(r'^accounts/password-change/done/$',
        'django.contrib.auth.views.password_change_done'),
    url(r'^accounts/password-reset/$',
        'django.contrib.auth.views.password_reset',
        name='reset_password'),
    url(r'^accounts/password-reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    url(r'^accounts/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm'),
    url(r'^accounts/reset/done/$',
        'django.contrib.auth.views.password_reset_complete'),

    url(r'^selectable/', include('selectable.urls')),
    url(r'', include('timepiece.urls')),
]
