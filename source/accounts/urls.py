from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import RegisterView, RegisterActivateView, UserDetailView, \
    UserChangeView
from accounts.views import BaseView, RegisterView

app_name = 'accounts'

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='create'),
    path('activate/<uuid:token>/', RegisterActivateView.as_view(), name='activate'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', UserChangeView.as_view(), name='change'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)