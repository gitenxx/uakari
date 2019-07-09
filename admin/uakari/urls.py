from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from uakari import views

router = routers.DefaultRouter()
router.register(r'records', views.RecordViewSet)

urlpatterns = [
    path('', admin.site.urls),
    path('', include(router.urls)),
    path('add_url', views.process_url),
    path('all_urls', views.get_urls)
]

admin.site.site_header = 'Uakari'
admin.site.site_title = 'Uakari'
admin.site.index_title = ''
admin.site.site_url = None
