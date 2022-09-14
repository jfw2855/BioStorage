from django.urls import path
#imports view classes
from .views.mango_views import Mangos, MangoDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.experiment_views import Experiments, ExpDetails
from .views.storage_views import Storages, StorageDetails
from .views.storage_type_views import StorageTypes, StorageTypeDetails
from .views.manufacturer_views import Manufacturers, ManufacturerDetails
from .views.category_views import Categories, CategoryDetails
from .views.container_views import Containers, ContainerDetails
from .views.item_type_views import ItemTypes

urlpatterns = [
  	# RESTful routing
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
    path('categories', Categories.as_view(), name='categories'),
    path('categories/<int:pk>', CategoryDetails.as_view(), name='category_detail'),
    path('containers',Containers.as_view(), name='containers'),
    path('containers/<int:pk>', ContainerDetails.as_view(), name='container_details'),
    path('item_types', ItemTypes.as_view(), name='item_types'),
]
