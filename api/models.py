from django.db import models

# Create your models here.
class Team(models.Model):
	name = models.CharField(max_length = 100, null = False, blank = False)
	test_captain = models.CharField(max_length = 100, null = False, blank = False)
	one_Day_captain =  models.CharField(max_length = 100, null = False, blank = False)
	first_Test = models.TextField()
	first_Odi = models.TextField()
	first_T20 = models.TextField()
	association = models.CharField(max_length = 200, null = False, blank = False)
	coaches = models.TextField() 

	def __str__(self):
		return self.name

class Player(models.Model):
	team = models.ForeignKey(Team, on_delete = models.CASCADE)
	name = models.CharField(max_length = 100, null = False, blank = False)
	born = models.CharField(max_length = 100, null = False, blank = False)
	batting_style = models.CharField(max_length = 100, null = False, blank = False)
	bowling_style = models.CharField(max_length = 100, null = False, blank = False)
	first_Test = models.TextField()
	first_Odi = models.TextField()
	first_T20 = models.TextField()
	profile = models.TextField()

	class Meta:
		verbose_name_plural = 'players'

	def __str__(self):
		return self.name

class Tournament(models.Model):
	name = models.CharField(max_length = 100, null = False, blank = False)
	date = models.CharField(max_length = 100, null = False, blank = False)
	
	def __str__(self):
		return self.name

class PointsTable(models.Model):
	tournament = models.ForeignKey(Tournament, on_delete = models.CASCADE)
	team = models.CharField(max_length = 100, null = False, blank = False)
	match = models.IntegerField()
	won = models.IntegerField()
	lost = models.IntegerField()
	tied = models.IntegerField()
	no_result = models.IntegerField()
	points = models.IntegerField()
	net_run_rate = models.DecimalField(max_digits=4, decimal_places=3)

	def __str__(self):
		return self.team

class Venue(models.Model):
	name = models.CharField(max_length = 100, null = False, blank = False)
	location = models.CharField(max_length = 100, null = False, blank = False)
	capacity = models.IntegerField()

	def __str__(self):
		return self.name

class Match(models.Model):
	venue = models.ForeignKey(Venue, on_delete = models.CASCADE)
	game = models.CharField(max_length = 100, null = False, blank = False)
	time = models.CharField(max_length = 100, null = False, blank = False)
	date = models.CharField(max_length = 100, null = False, blank = False)
	result = models.CharField(max_length = 100, null = True, blank = True)

	def __str__(self):
		return self.game

class Match_Summary(models.Model):
	game = models.ForeignKey(Match, on_delete = models.CASCADE)
	team_detail = models.TextField()
	winner = models.CharField(max_length = 100, null = False, blank = False)
	loser = models.CharField(max_length = 100, null = False, blank = False)
	mom = models.CharField(max_length = 100, null = False, blank = False)
	bom = models.CharField(max_length = 100, null = True, blank = True)
	best_fielder = models.CharField(max_length = 100, null = True, blank = True)

	def __str__(self):
		return self.winner






