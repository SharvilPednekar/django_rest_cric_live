from rest_framework import serializers

from .models import Team, Player, Tournament, PointsTable, Venue, Match, Match_Summary

class TeamSerializer(serializers.ModelSerializer):
	class Meta:
		model = Team
		fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Player
		fields = '__all__'

class TournamentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tournament
		fields = '__all__'

class PointsTableSerializer(serializers.ModelSerializer):
	class Meta:
		model = PointsTable
		fields = '__all__'

class VenueSerializer(serializers.ModelSerializer):
	class Meta:
		model = Venue
		fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
	class Meta:
		model = Match
		fields = '__all__'

class Match_Summary_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Match_Summary
		fields = '__all__'