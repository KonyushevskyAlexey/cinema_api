from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movies.views import MovieViewSet
from halls.views import HallViewSet
from screenings.views import ScreeningViewSet
from tickets.views import TicketViewSet
from users.views import UserViewSet
from .views import home_view  # Импортируем наше view

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'halls', HallViewSet, basename='hall')
router.register(r'screenings', ScreeningViewSet, basename='screening')
router.register(r'tickets', TicketViewSet, basename='ticket')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', home_view, name='home'),  # Добавляем главную страницу
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('rest_framework.urls')),
]
