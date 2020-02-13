from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users',
                views.UserViewSet)
router.register(r'gender',
                views.GenderViewSet)
router.register(r'adress',
                views.AdressViewSet)
router.register(r'client',
                views.ClientViewSet)
router.register(r'individualclientdetails',
                views.IndividualClientDetailsViewSet)
router.register(r'companyclientdetails',
                views.CompanyClientDetailsViewSet)
router.register(r'position',
                views.PositionViewSet)
router.register(r'employee',
                views.EmployeeViewSet)
router.register(r'gearboxtype',
                views.GearboxTypeViewSet)
router.register(r'fueltype',
                views.FuelTypeViewSet)
router.register(r'carcategory',
                views.CarCategoryViewSet)
router.register(r'car',
                views.CarViewSet)
router.register(r'house',
                views.HouseViewSet)
router.register(r'insurancepolicy',
                views.InsurancePolicyViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
