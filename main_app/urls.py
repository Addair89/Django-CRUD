from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.games_index, name='index'),
    path('games/<int:game_id>', views.game_detail, name='detail'),
    path('games/create', views.GameCreate.as_view(), name='games_create'),
    path('games/<int:pk>/update', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete', views.GameDelete.as_view(), name='games_delete'),
    path('games/<int:game_id>/add_owner', views.add_owner, name='add_owner'),
    path('stores/', views.StoreList.as_view(), name='stores_index'),
    path('games/<int:game_id>/assoc_store/<int:store_id>',views.assoc_store, name='assoc_store'),
    path('games/<int:game_id>/rm_assoc_store/<int:store_id>',views.rm_assoc_store, name='rm_assoc_store'),
    path('stores/create/', views.StoreCreate.as_view(), name='stores_create'),
    path('stores/<int:pk>', views.StoreDetail.as_view(), name='stores_detail'),
    path('stores/<int:pk>/update/', views.StoreUpdate.as_view(), name='stores_update'),
    path('stores/<int:pk>/delete/', views.StoreDelete.as_view(), name='stores_delete')
]