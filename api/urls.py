from django.urls import path
from .views.mango_views import Mangos, MangoDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.experiment_views import Experiments, ExpDetails
from .views.storage_views import Storages
from .views.storage_type_views import StorageTypes

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
    path('storage_types',StorageTypes.as_view(), name='storage_types'),
]
