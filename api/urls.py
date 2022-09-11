from django.urls import path
#imports view classes
from .views.mango_views import Mangos, MangoDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.experiment_views import Experiments, ExpDetails
from .views.storage_views import Storages, StorageDetails
from .views.storage_type_views import StorageTypes, StorageTypeDetails
from .views.manufacturer_views import Manufacturers, ManufacturerDetails

urlpatterns = [
  	# Restful routing
    path('mangos', Mangos.as_view(), name='mangos'),
    path('mangos/<int:pk>', MangoDetail.as_view(), name='mango_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),
    path('experiments',Experiments.as_view(), name='experiments'),
    path('experiments/<int:pk>', ExpDetails.as_view(), name='exp_detail'),
    path('storages', Storages.as_view(), name='storages'),
    path('storages/<int:pk>', StorageDetails.as_view(), name='storage_detail'),
    path('storage_types',StorageTypes.as_view(), name='storage_types'),
    path('storage_types/<int:pk>',StorageTypeDetails.as_view(), name='storage_type_details'),
    path('manufacturers', Manufacturers.as_view(), name='manufacturers'),
    path('manufacturers/<int:pk>', ManufacturerDetails.as_view(), name='manufacturer_detail'),
]
