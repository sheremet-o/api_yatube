from django.urls import path, include

from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet

v1_router = SimpleRouter()

v1_router.register('v1/posts', PostViewSet)
v1_router.register('v1/groups', GroupViewSet)
v1_router.register(r'v1/posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='comments')

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('', include(v1_router.urls))
]
