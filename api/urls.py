from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from . import views

router = DefaultRouter()
router.register(r'foo', views.FooViewSet)

schema_view = get_swagger_view(title='Foo API')

urlpatterns = [
    url('^$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
