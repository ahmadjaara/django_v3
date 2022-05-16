from django.urls import path
from .views import SnackListView,SnackDetailView,SnackCreateView,SnackDeleteView,SnackUpdateView,HometView
#name for make a reference for that url or have two app and that have the same path
urlpatterns= [
    # path("",HometView.as_view(),name="home_view"),
    path("",SnackListView.as_view(),name="snack_list"),
    path("<int:pk>/",SnackDetailView.as_view(),name="snack_detail"),
    path("create/",SnackCreateView.as_view(),name="snack_craete"),
    path("<int:pk>/delete/",SnackDeleteView.as_view(),name="snack_delete"),
    path("<int:pk>/update/",SnackUpdateView.as_view(),name="snack_update")
 
    ]