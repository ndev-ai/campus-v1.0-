from django.db import models


class Event(models.Model):
    """Event model for managing campus events"""
    name = models.CharField(max_length=200, verbose_name="Event Name")
    date = models.DateField(verbose_name="Event Date")
    location = models.CharField(max_length=200, verbose_name="Location")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date']
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.name
