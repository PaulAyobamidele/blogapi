from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewset, PostViewset


router = SimpleRouter()

router.register('users', UserViewset, basename='users')
router.register('', PostViewset, basename='posts')

urlpatterns = router.urls