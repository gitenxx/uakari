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
    path('all_urls', views.get_urls),
    path('get_spurl', views.get_specific_url),
    path('delete_url', views.delete_url),
    path('delete_all', views.delete_all)
]

admin.site.site_header = 'Uakari'
admin.site.site_title = 'Uakari'
admin.site.index_title = ''
admin.site.site_url = None
