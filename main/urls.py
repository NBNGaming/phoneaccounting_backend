from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('phones', views.PhoneViewSet)
router.register('simcards', views.SIMCardViewSet)
router.register('sdcards', views.SDCardViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/phones/manufacturer/<manufacturer>', views.PhoneListByManufacturer.as_view()),
    path('api/v1/notifications/', views.NotificationList.as_view()),
    path('api/v1/simcards/number/<number>', views.SIMCardListByNumber.as_view()),
    path('api/v1/sdcards/serialNumber/<serial>', views.SDCardListBySerial.as_view()),
]
