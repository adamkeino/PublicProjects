from django.urls import path
# from . import views ;;; function-based views import statement
from .views import HomeView, BlogDetail, Articles

urlpatterns = [
    # path('', views.home, name="home") - functionbased url
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', BlogDetail.as_view(), name="blog-detail"),
    path('articles', Articles.as_view(), name='articles'),
]
