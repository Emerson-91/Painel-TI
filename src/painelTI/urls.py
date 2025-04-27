from django.contrib import admin
from django.urls import path, include
from dashboard.views import CustomLogoutView
from .views import custom_login_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # URL para logout
    path('dashboard/', include('dashboard.urls')),  # URLs do dashboard
    path('ping/', include('ping_app.urls')),  # URLs do ping_app
    path('utilitarios/', include('utilitarios.urls')), # URL para utilitarios
    path('patrimonios/', include('patrimonios.urls')), # URL para patrimonios
    path('switches/', include('switches.urls')),
    path('', custom_login_view, name='login'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
