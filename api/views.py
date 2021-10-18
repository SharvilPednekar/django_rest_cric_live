from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TeamSerializer, PlayerSerializer, TournamentSerializer, PointsTableSerializer, VenueSerializer, MatchSerializer, Match_Summary_Serializer
from .models import Team, Player, Tournament, PointsTable, Venue, Match, Match_Summary

# Create your views here.

'''@api_view(['GET'])
def apiOverview(request):
	api_urls = {
	'List': '/team-list/',
	'Detail View': '/team-profile/<int:id>',
	'Create': '/team-create/',
	'Update': '/team-update/<int:id>',
	'Delete': '/team-profile/<int:id>',

	}

	return Response(api_urls);
'''

# Team View Functions
@api_view(['GET'])
def ShowAll_Team(request):
	teams = Team.objects.all()
	serializer = TeamSerializer(teams, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def ViewTeam(request, pk):
	team = Team.objects.get(id=pk)
	serializer = TeamSerializer(team, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def CreateTeam(request):
	serializer = TeamSerializer(data = request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def UpdateTeam(request, pk):
	team = Team.objects.get(id=pk)
	serializer = TeamSerializer(instance = team, data = request.data)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['GET'])
def deleteTeam(request, pk):
	team = Team.objects.get(id=pk)
	team.delete()
	
	return Response('Team delete successfully.')

# Player View Functions:
@api_view(['GET'])
def ShowAll_Player(request):
	players = Player.objects.all()
	serializer = PlayerSerializer(players, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def ViewPlayer(request, pk):
	player = Player.objects.get(id=pk)
	serializer = PlayerSerializer(player, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def CreatePlayer(request):
	serializer = PlayerSerializer(data = request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def UpdatePlayer(request, pk):
	player = Player.objects.get(id=pk)
	serializer = PlayerSerializer(instance = player, data = request.data)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['GET'])
def deletePlayer(request, pk):
	player = Player.objects.get(id=pk)
	player.delete()
	
	return Response('Player delete successfully.')

# Tournament View Functions:
@api_view(['GET'])
def ShowAll_Tournament(request):
	tournaments = Tournament.objects.all()
	serializer = TournamentSerializer(tournaments, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def ViewTournament(request, pk):
	tournament = Tournament.objects.get(id=pk)
	serializer = TournamentSerializer(tournament, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def CreateTournament(request):
	serializer = TournamentSerializer(data = request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def UpdateTournament(request, pk):
	tournament = Tournament.objects.get(id=pk)
	serializer = TournamentSerializer(instance = tournament, data = request.data)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['GET'])
def deleteTournament(request, pk):
	tournament = Tournament.objects.get(id=pk)
	tournament.delete()
	
	return Response('Tournament delete successfully.')

# PointsTable View Function:
@api_view(['GET'])
def ShowAll_PointsTable(request):
	pointstables = PointsTable.objects.all()
	serializer = PointsTableSerializer(pointstables, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def ViewPointsTable(request, pk):
	pointstable = PointsTable.objects.get(id=pk)
	serializer = PointsTableSerializer(pointstable, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def CreatePointsTable(request):
	serializer = PointsTableSerializer(data = request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def UpdatePointsTable(request, pk):
	pointstable = PointsTable.objects.get(id=pk)
	serializer = PointsTableSerializer(instance = pointstable, data = request.data)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['GET'])
def deletePointsTable(request, pk):
	pointstable = PointsTable.objects.get(id=pk)
	pointstable.delete()
	
	return Response('Points Table deleted successfully.')

# Venue View Function:
@api_view(['GET'])
def ShowAll_Venue(request):
	venues = Venue.objects.all()
	serializer = VenueSerializer(venues, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def ViewVenue(request, pk):
	venue = Venue.objects.get(id=pk)
	serializer = VenueSerializer(venue, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def CreateVenue(request):
	serializer = VenueSerializer(data = request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def UpdateVenue(request, pk):
	venue = Venue.objects.get(id=pk)
	serializer = VenueSerializer(instance = venue, data = request.data)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['GET'])
def deleteVenue(request, pk):
	venue = Venue.objects.get(id=pk)
	venue.delete()
	
	return Response('Venue delete successfully.')

# Match View Function:
@api_view(['GET'])
def ShowAll_Match(request):
	matches = Match.objects.all()
	serializer = MatchSerializer(matches, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def ViewMatch(request, pk):
	match = Match.objects.get(id=pk)
	serializer = MatchSerializer(match, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def CreateMatch(request):
	serializer = MatchSerializer(data = request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def UpdateMatch(request, pk):
	match = Match.objects.get(id=pk)
	serializer = MatchSerializer(instance = match, data = request.data)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['GET'])
def deleteMatch(request, pk):
	match = Match.objects.get(id=pk)
	match.delete()
	
	return Response('Match deleted successfully.')

# Match Summary View Function:
@api_view(['GET'])
def ShowAll_Match_Summary(request):
	match_sums = Match_Summary.objects.all()
	serializer = Match_Summary_Serializer(match_sums, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def ViewMatch_Summary(request, pk):
	match_sum = Match_Summary.objects.get(id=pk)
	serializer = Match_Summary_Serializer(match_sum, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def CreateMatch_Summary(request):
	serializer = Match_Summary_Serializer(data = request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def UpdateMatch_Summary(request, pk):
	match_sum = Match_Summary.objects.get(id=pk)
	serializer = Match_Summary_Serializer(instance = match_sum, data = request.data)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['GET'])
def deleteMatch_Summary(request, pk):
	match_sum = Match_Summary.objects.get(id=pk)
	match_sum.delete()
	
	return Response('Match summary deleted successfully.')

