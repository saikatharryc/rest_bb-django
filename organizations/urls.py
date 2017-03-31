from django.conf.urls import url

from.import views

urlpatterns = [
    # /organizations/
    url(r'^$', views.index, name='index'),

    # /organizations/:id
    url(r'^(?P<org_id>[0-9]+)/$', views.detail, name='detail'),
]
