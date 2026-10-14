from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)

from .views import (
    PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet
)

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('groups', GroupViewSet, basename='groups')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/jwt/create/', TokenObtainPairView.as_view(),
         name='jwt-create'),
    path('v1/jwt/refresh/', TokenRefreshView.as_view(),
         name='jwt-refresh'),
    path('v1/jwt/verify/', TokenVerifyView.as_view(),
         name='jwt-verify'),
]