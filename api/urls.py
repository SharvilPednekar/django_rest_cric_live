from django.urls import path
from . import views

urlpatterns = [
    #path('', views.apiOverview, name = 'apiOverview'),
    # Team URL's
    path('team-list/', views.ShowAll_Team, name = 'team-list'),
    path('team-profile/<int:pk>/', views.ViewTeam, name = 'team-profile'),
    path('team-create/', views.CreateTeam, name = 'team-create'),
    path('team-update/<int:pk>/', views.UpdateTeam, name = 'team-update'),
    path('team-delete/<int:pk>/', views.deleteTeam, name = 'team-delete'),
    # Player URL's
    path('player-list/', views.ShowAll_Player, name = 'player-list'),
    path('player-profile/<int:pk>/', views.ViewPlayer, name = 'player-profile'),
    path('player-create/', views.CreatePlayer, name = 'player-create'),
    path('player-update/<int:pk>/', views.UpdatePlayer, name = 'player-update'),
    path('player-delete/<int:pk>/', views.deletePlayer, name = 'player-delete'),
    # Tournament URL's
    path('tournament-list/', views.ShowAll_Tournament, name = 'tournament-list'),
    path('tournament-profile/<int:pk>/', views.ViewTournament, name = 'tournament-profile'),
    path('tournament-create/', views.CreateTournament, name = 'tournament-create'),
    path('tournament-update/<int:pk>/', views.UpdateTournament, name = 'tournament-update'),
    path('tournament-delete/<int:pk>/', views.deleteTournament, name = 'tournament-delete'),
    # Points Table URL's
    path('pointstable-list/', views.ShowAll_PointsTable, name = 'pointstable-list'),
    path('pointstable-profile/<int:pk>/', views.ViewPointsTable, name = 'pointstable-profile'),
    path('pointstable-create/', views.CreatePointsTable, name = 'pointstable-create'),
    path('pointstable-update/<int:pk>/', views.UpdatePointsTable, name = 'pointstable-update'),
    path('pointstable-delete/<int:pk>/', views.deletePointsTable, name = 'pointstable-delete'),
    # Venue URL's
    path('venue-list/', views.ShowAll_Venue, name = 'venue-list'),
    path('venue-profile/<int:pk>/', views.ViewVenue, name = 'venue-profile'),
    path('venue-create/', views.CreateVenue, name = 'venue-create'),
    path('venue-update/<int:pk>/', views.UpdateVenue, name = 'venue-update'),
    path('venue-delete/<int:pk>/', views.deleteVenue, name = 'venue-delete'),
    # Match URL's
    path('match-list/', views.ShowAll_Match, name = 'match-list'),
    path('match-profile/<int:pk>/', views.ViewMatch, name = 'match-profile'),
    path('match-create/', views.CreateMatch, name = 'match-create'),
    path('match-update/<int:pk>/', views.UpdateMatch, name = 'match-update'),
    path('match-delete/<int:pk>/', views.deleteMatch, name = 'match-delete'),
    # Match Summary URL's
     path('match_sum-list/', views.ShowAll_Match_Summary, name = 'match_sum-list'),
     path('match_sum-profile/<int:pk>/', views.ViewMatch_Summary, name = 'match_sum-profile'),
     path('match_sum-create/', views.CreateMatch_Summary, name = 'match_sum-create'),
     path('match_sum-update/<int:pk>/', views.UpdateMatch_Summary, name = 'match_sum-update'),
     path('match_sum-delete/<int:pk>/', views.deleteMatch_Summary, name = 'match_sum-delete'),

]