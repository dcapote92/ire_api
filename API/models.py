from django.db import models

# Create your models here.

class Center(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    codename = models.CharField(max_length=2)

class User(models.Model):
    id = models.PositiveIntegerField(primary_key = True)
    code = models.CharField(max_length=4)
    pin = models.CharField(max_length=4)
    pin_reset = models.BooleanField(default=1)
    role = models.CharField(max_length=30)
    group = models.CharField(max_length=3)
    center_id = models.ForeignKey(Center, models.DO_NOTHING)
    since = models.DateField()
    active = models.BooleanField(default=1)
    user_device = models.CharField(max_length=10)

class Bet(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    type = models.CharField(max_length=30)
    numbers = models.CharField(max_length=7)
    amount = models.FloatField()
    user_id = models.ForeignKey(User, models.DO_NOTHING)
    center_id = models.ForeignKey(Center, models.DO_NOTHING)

class Winner(models.Model):
    id  = models.PositiveIntegerField(primary_key=True)
    date = models.DateField()
    user_id = models.ForeignKey(User, models.DO_NOTHING)
    numbers = models.CharField(max_length=7)
    bet_amount = models.FloatField()
    gained_amount = models.FloatField()
    center_id = models.ForeignKey(Center, models.DO_NOTHING)

class Limit(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    type = models.CharField(max_length=30)
    amount = models.FloatField()
    center_id = models.ForeignKey(Center, models.DO_NOTHING)

class Classified(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    type = models.CharField(max_length=30)
    charged_amount = models.FloatField()
    delayed_days = models.PositiveIntegerField()
    center_id = models.ForeignKey(Center, models.DO_NOTHING)

class Schedule(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    start_a = models.CharField(max_length=30)
    start_b = models.CharField(max_length=30)
    end_a = models.CharField(max_length=30)
    end_b = models.CharField(max_length=30)
    center_id = models.ForeignKey(Center, models.DO_NOTHING)

class Throw(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    hundred = models.CharField(max_length=3)
    fix_number = models.CharField(max_length=2)
    dinamic_a = models.CharField(max_length=2)
    dinamic_b = models.CharField(max_length=2)
    session = models.CharField(max_length=30)
    created_at = models.DateField()
    center_id = models.ForeignKey(Center, models.DO_NOTHING)

class Plan(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    normal_fix_number = models.CharField(max_length=2)
    normal_dinamic_number = models.CharField(max_length=2)
    normal_parle = models.CharField(max_length=7)
    normal_hundred = models.CharField(max_length=3)
    limited_fix_number = models.CharField(max_length=2)
    limited_dinamic_number = models.CharField(max_length=2)
    limited_parle = models.CharField(max_length=7)
    limited_hundred = models.CharField(max_length=3)
    ball_list = models.FloatField()
    parle_list = models.FloatField()
    center_id = models.ForeignKey(Center, models.DO_NOTHING)


