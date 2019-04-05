
from django.contrib import admin
from django.urls import path
from django.urls import include
from study import urls as study_urls
from dashboard import urls as dashboard_urls
from testmode import urls as testmode_urls
from register import urls as register_urls


urlpatterns = [
    path('admin/', admin.site.urls),

    path('dashboard/', include(dashboard_urls)),
    # 'vocabuilder/'
    path('vocabuilder/', include(study_urls)),
    path('', include(study_urls)),

    path('test/', include(testmode_urls)),

    path('signup/',include(register_urls, namespace="register")),

]
