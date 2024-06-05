from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.routers import DefaultRouter

from api.views import CustomerViewSetView


router = DefaultRouter()

# router.register("register",TechnicianRegisterView,basename='reg')

router.register("customers",CustomerViewSetView,basename="customers")


urlpatterns = [

    path('token/',ObtainAuthToken.as_view(),name="token"),
    
]+router.urls