"""firstclass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import profile_validate.views as profile
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', profile.base, name="base"),
    #path('basic/', profile.basic, name="basic"),
    path('basic/<int:random>', profile.basic, name="basic"),
    path('photo/<int:random>', profile.photo, name="photo"),
    path('paper/<int:random>', profile.paper, name="paper"),
    path('nofilter/<int:random>', profile.noFilter, name="no-filter"),
    path('beautycheck/', profile.beautyCheck, name="beauty-check"),
    path('nofilterdone/<int:index>', profile.noFilterDone, name="nofilter-done"),
    path('paperbeautydone/<int:flag_type>', profile.paperBeautyDone, name="paper-beauty-done"),
    path('paperdetaildone/<int:index>', profile.paperDetailDone, name="paperdetail-done"),
    path('paper_detail/<int:index>', profile.paper_detail, name="paper-detail"),
    path('photo_done/', profile.profilePhotoDone, name="photo-done"),
    path("done/<int:flag_type>", profile.done, name="done"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
