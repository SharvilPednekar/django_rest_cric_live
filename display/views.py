from django.shortcuts import render
from django.http import HttpResponse
from api.models import Team, Player, Tournament, PointsTable, Venue, Match, Match_Summary
from api.serializers import TeamSerializer, PlayerSerializer, TournamentSerializer, PointsTableSerializer, VenueSerializer, MatchSerializer, Match_Summary_Serializer


# Create your views here.
def index(request):
	'''Home Page for criclive.'''
	return render(request, 'index.html')

def displayTeamList(request):
	print('.........................')
	return render(request,"display_team_list.html")

def displayPlayerList(request):
	print('.........................')
	return render(request,"display_player_list.html")

def displayTournamentList(request):
	print('.........................')
	return render(request,"display_tournament_list.html")

def displayPointstableList(request):
	print('.........................')
	return render(request,"display_pointstable_list.html")

def displayVenueList(request):
	print('.........................')
	return render(request,"display_venue_list.html")

def displayMatchList(request):
	print('.........................')
	return render(request,"display_match_list.html")

def displayMatchSumList(request):
	print('.........................')
	return render(request,"match_sum_list.html")





