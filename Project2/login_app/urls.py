"""Project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from login_app import views as v1
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

app_name='login_app'

urlpatterns = [
   path('index', v1.index, name='index'),
   path('register', v1.register, name='register'),
   path('login', v1.login_page, name='login'),
   path('user_login', v1.user_login, name='user_login'),
   path('logout', v1.user_logout, name='logout'),
   path('about', v1.about, name='about'),  
   
]

urlpatterns+=staticfiles_urlpatterns()
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)