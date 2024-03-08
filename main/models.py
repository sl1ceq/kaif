from django.db import models

class Order(models.Model):
    PAUSE_CHOICES = [
        ('pause1', 'First pause'),
        ('pause2', 'Second pause'),
        ('pause3', 'Third pause')
    ]
    PLACE_CHOICES = [
        ('firstff', 'Erste Stock'),
        ('secondff', 'Second Stock'),
    ]

    instagram_nickname = models.CharField(max_length=100)
    pause = models.CharField(max_length=100, choices=PAUSE_CHOICES)
    place = models.CharField(max_length=100, choices=PLACE_CHOICES)
    ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.insta_name
