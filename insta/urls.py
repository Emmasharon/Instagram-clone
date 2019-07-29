from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^accounts/profile/$',views.profile,name = 'profile'),
    url(r'^accounts/timeline/$',views.timeline,name = 'timeline'),
    url(r'^accounts/new_post/$',views.new_post,name = 'new_post'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)