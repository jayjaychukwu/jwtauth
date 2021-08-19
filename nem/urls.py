from django.contrib import admin
from django.urls import path,include

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Nemesis API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('app.urls')),
    path('api/details/', include('disp.urls')),
    path('', schema_view),

]
