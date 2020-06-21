"""record URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.button),
    url(r'^external', views.external),
    url(r'^org', views.org),
    url(r'^pitch', views.pitch),
    url(r'^pitc', views.pitc),
    url(r'^rev', views.rev),
    url(r'^hp', views.hp),
    url(r'^lp', views.lp),
    url(r'^we', views.we),
    url(r'^ry', views.ry),
    url(r'^mip', views.mip),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
