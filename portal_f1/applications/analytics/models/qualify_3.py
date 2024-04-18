from django.db import models
from analytics.models.qualifying import Qualifying


class Qualify_3(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Q3 ID", blank=False, null=False)
    time = models.TimeField(verbose_name="Q3 Lap Time", blank=True, null=True)
    qualifying = models.ForeignKey(Qualifying, on_delete=models.PROTECT, verbose_name="Qualifying ID", blank=False, null=False)

    def __str__(self):
        return "{}".format(self.time)

    class Meta:
        verbose_name_plural = "Q3s"
