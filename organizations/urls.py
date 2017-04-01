from django.conf.urls import include, url

from.import views
from.models import Organizations
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.


class Orgserializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Organizations
        fields = ('org_name', 'org_phone', 'org_email', 'org_address')

# ViewSets define the view behavior.


class OrgViewSet(viewsets.ModelViewSet):
    queryset = Organizations.objects.all()
    serializer_class = Orgserializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.SimpleRouter()
router.register(r'organization', OrgViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # /organizations/
    url(r'^$', views.index, name='index'),

    # /organizations/:id
    url(r'^(?P<org_id>[0-9]+)/$', views.detail, name='detail'),
]
