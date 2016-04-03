from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateTimeField(blank=True, null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'unknown'),
    )
    person_gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')
    PERSON_TYPE_CHOICES = (
        ('SUS', 'Suspect'),
        ('WIT', 'Witness'),
        ('VIC', 'Victim'),
        ('INF', 'Informant'),
        ('INT', 'Intel'),
        ('UNK', 'Unknown'),
    )
    person_type = models.CharField(max_length=3, choices=PERSON_TYPE_CHOICES, default='UNK')
    Comment = models.TextField(blank=True)

    def __str__(self):
        return self.last_name.upper() + ", " + self.first_name


class GroupType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Group(models.Model):
    group_name = models.CharField(max_length=100)
    group_type = models.ForeignKey(GroupType, on_delete=models.CASCADE)

    def __str__(self):
        return self.group_name


class PersonInGroup(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.group.group_name + " : " + self.person.first_name + " " + self.person.last_name
