from django.contrib import admin
from .models import Team, Player, Tournament, PointsTable, Venue, Match, Match_Summary

# Register your models here.
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Tournament)
admin.site.register(PointsTable)
admin.site.register(Venue)
admin.site.register(Match)
admin.site.register(Match_Summary)
