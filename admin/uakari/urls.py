from django.urls import path
from django.contrib import admin


urlpatterns = [
    path('', admin.site.urls),
]

admin.site.site_header = 'Uakari'
admin.site.site_title = 'Uakari'
admin.site.index_title = ''
admin.site.site_url = None
