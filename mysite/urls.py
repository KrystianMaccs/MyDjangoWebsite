from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#import your app views here if it applies to your case


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('homeapp.urls'))),
]


#Setting for loading static files in Development mode(i.e debug should be True in settings)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
