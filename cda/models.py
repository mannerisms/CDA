from django.db import models


class Person(models.Model):
    date_of_birth = models.DateTimeField(blank=True)
    date_of_death = models.DateTimeField(blank=True)
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
        ('UNK', 'Unknown'),
    )
    person_type = models.CharField(max_length=3, choices=PERSON_TYPE_CHOICES, default='UNK')
    Comment = models.TextField()


class PersonName(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    NAME_TYPE_CHOICES = (
        ('FN', 'First Name'),
        ('LN', 'Last Name'),
        ('NN', 'Nick Name'),
        ('SN', 'Short Name'),
        )
    name_type = models.CharField(max_length=3, choices=NAME_TYPE_CHOICES, default='FN')
    name = models.CharField(max_length=100, blank=True)

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
