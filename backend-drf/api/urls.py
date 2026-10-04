from django.urls import path
from users import views as UserViews
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from products import views as ProductView


urlpatterns=[
    path('register/', UserViews.RegisterView.as_view()),
    path("token/",TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path("token/refresh/",TokenRefreshView.as_view(),name="token_refresh"),
    path("profile/",UserViews.ProfileView.as_view(),name="profile"),
    path('categories/',ProductView.CategoryListView.as_view()),
    path('products/',ProductView.ProductListView.as_view()),
    path('products/<int:pk>/',ProductView.ProductdetailView.as_view()),
]