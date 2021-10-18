from django.urls import path
from . import views

urlpatterns = [
	path('displayTeamList/', views.displayTeamList, name = 'displayTeamList'),
	path('displayPlayerList/', views.displayPlayerList, name = 'displayPlayerList'),
	path('displayTournamentList/', views.displayTournamentList, name = 'displayTournamentList'),
	path('displayPointstableList/', views.displayPointstableList, name = 'displayPointstableList'),
	path('displayVenueList/', views.displayVenueList, name = 'displayVenueList'),
	path('displayMatchList/', views.displayMatchList, name = 'displayMatchList'),
	path('displayMatchSumList/', views.displayMatchSumList, name = 'displayMatchSumList'),
	 
]