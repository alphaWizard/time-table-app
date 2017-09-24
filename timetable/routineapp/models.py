from django.db import models


class days(models.Model):
    dayname = models.CharField(max_length=10)

    def __str__(self):
        return self.dayname


class periods(models.Model):
    periodname =models.IntegerField()

    def __str__(self):
        return str(self.periodname)

class subject(models.Model):
    day = models.ForeignKey(days)
    period = models.ForeignKey(periods)
    value = models.CharField(max_length=100)


    class Meta:
        order_with_respect_to = 'day'

    def __str__(self):
        return '%s %s :- %s' % (self.day, self.period,self.value)
