
from django.contrib import admin
from django.urls import path, include, re_path
from tractor import views
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from tractor import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('evidence/', include('evidence.urls')),
    path('legalsite/', include('legalsite.urls')),
    path('myinfo/', include('myinfo.urls')),
    path('myinfo/feedback', include('myinfo.urls')),
    path('pdfextract/', include('pdfextract.urls')),
    path('craw/', include('craw.urls')),
    path('', views.index, name='index'),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]