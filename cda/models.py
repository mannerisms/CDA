from django.db import models


class Person(models.Model):
    date_of_birth = models.DateTimeField()
    date_of_death = models.DateTimeField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'unknown'),
    )
    person_gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')
    PERSON_TYPE_CHOICES = (
        ('SUS', 'Suspect'),
        ('WIT', 'Witness'),
        ('INF', 'Informant'),
        ('INT', 'Intel'),
    )
    person_type = models.CharField(max_length=3, choices=PERSON_TYPE_CHOICES)
    Comment = models.TextField()


class PersonName(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)


class Group(models.Model):
    group_name = models.CharField(max_length=100)
    GROUP_TYPE_CHOICES = (
        ('BUS', 'Business'),
        ('NET', 'Network'),
        ('SOC', 'Social'),
        ('FAM', 'Family'),
    )
    group_type = models.CharField(max_length=3, choices=GROUP_TYPE_CHOICES)


class PersonInGroup(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
