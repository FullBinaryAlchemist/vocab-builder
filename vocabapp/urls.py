
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import include
from study import urls
from dashboard import urls as dashboard_urls
from testmode import urls as testmode_urls
from register import urls as register_urls


urlpatterns = [
    path('admin/', admin.site.urls),

    path('dashboard/', include(dashboard_urls)),
    # 'vocabuilder/'
    path('vocabuilder/', include(urls)),
    path('', include(urls)),

    path('test/', include(testmode_urls)),

    path('signup/',include(register_urls, namespace="register")),

    path('login/',auth_views.LoginView.as_view(template_name='register/login.html'),name='login'),

    path('logout/',auth_views.LogoutView.as_view(template_name='register/logout.html'),name='logout'),

]
