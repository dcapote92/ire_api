from django.urls import path,include
from rest_framework import routers
from API import views

router = routers.DefaultRouter()
router.register(r'centers', views.CenterViewSet)

# REGISTRAR RUTA DE CADA VIEW
router.register(r'users', views.UserViewSet)
router.register(r'bets', views.BetsViewSet)
router.register(r'winners', views.WinnersViewSet)
router.register(r'limits', views.LimitsViewSet)
router.register(r'classifieds', views.ClassifiedViewSet)
router.register(r'schedule', views.ScheduleViewSet)
router.register(r'throws', views.ThrowViewSet)
router.register(r'plans', views.PlansViewSet)

urlpatterns = [
    path('', include(router.urls))
]
