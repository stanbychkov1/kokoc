from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from kokoc import settings

handler403 = 'applications.polls.errors.page_forbidden'
handler404 = 'applications.polls.errors.page_not_found'
handler500 = 'applications.polls.errors.server_error'

urlpatterns = [
    path('', include('applications.polls.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('applications.users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
