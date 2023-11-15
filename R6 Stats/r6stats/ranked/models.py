from django.db import models

# Create your models here.
ranked_sides = [
    ("attacker","attacker"),
    ("defender","defender")
]
class Operator(models.Model):
    operator_name = models.CharField(max_length=20)
    operator_side = models.CharField(max_length=20, choices=ranked_sides)
    operator_speed = models.IntegerField()
    operator_health = models.IntegerField()

    def __str__(self):
        return self.operator_name

class Map(models.Model):
    map_name = models.CharField(max_length=20)

    def __str__(self):
        return self.map_name
