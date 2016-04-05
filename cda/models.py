from django.db import models
from django.core.urlresolvers import reverse


class Source(models.Model):
    document = models.FileField()
    reference = models.CharField(max_length=100)
    TYPE_CHOICES = (
        ('WS', 'Witness Statement'),
        ('SS', 'Suspect Statement'),
        ('RP', 'Report'),
        ('IN', 'Investigators note'),
        ('UN', 'Unknown'),
    )
    type = models.CharField(max_length=3, choices=TYPE_CHOICES, default='EN')
    title = models.CharField(max_length=256)
    src_date = models.DateField(blank=True)
    LANGUAGE_CHOICES = (
        ('EN', 'English'),
        ('FR', 'French'),
        ('AR', 'Arabic'),
        ('SP', 'Spanish'),
        ('DT', 'Dutch'),
        ('NA', 'Unknown'),
    )
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='EN')
    description = models.TextField(blank=True)
    comment = models.TextField(blank=True)
    verified = models.BooleanField(default=False)
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.reference + "  :  " + self.title


class Person(models.Model):
    first_name = models.CharField(max_length=100)
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
    comment = models.TextField(blank=True)
    source = models.ManyToManyField(Source, blank=True)
    image = models.FileField(blank=True)

    def get_absolute_url(self):
        return reverse('cda:persons')

    def __str__(self):
        return self.last_name.upper() + ", " + self.first_name


class CellMast(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=64)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    comment = models.TextField(blank=True)
    source = models.ForeignKey(Source)
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.code + "  :  " + self.name
