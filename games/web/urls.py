from django.urls import path

from games.web.views import home, profile_create, profile_details, profile_edit, profile_delete, dashboard, game_create, \
    game_details, game_edit, game_delete

urlpatterns = (
    path('', home, name='home'),
    path('profile/create/', profile_create, name='create profile'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/edit/', profile_edit, name='edit profile'),
    path('profile/delete/', profile_delete, name='delete profile'),
    path('dashboard/', dashboard, name='dashboard'),
    path('game/create', game_create, name='create game'),
    path('game/details/<int:pk>/', game_details, name='game details'),
    path('game/edit/<int:pk>/', game_edit, name='edit game'),
    path('game/delete/<int:pk>/', game_delete, name='delete game'),
)
