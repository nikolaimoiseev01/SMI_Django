from django.urls import path, include
from posts.views import *

# from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('rest_framework_social_oauth2.urls')),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    path('post/<int:pk>', PostRetrieveView.as_view()),
    # path('post/update/<int:pk>', PostUpdateView.as_view()),
    path('posts/all', PostListView.as_view()),
    path('post-topics/all', PostTopicListView.as_view()),
]
