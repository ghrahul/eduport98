from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'tutorial'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'subject/add/$',views.SubjectCreate.as_view(),name='subject-add'),
    url(r'note/add/$',views.NoteCreate.as_view(),name='note-add'),
    url(r'subject/(?P<pk>[0-9]+)/$',views.SubjectUpdate.as_view(),name='subject-update'),
    url(r'subject/(?P<pk>[0-9]+)/delete/$',views.SubjectDelete.as_view(),name='subject-delete'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)