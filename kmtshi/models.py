from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from kmtshi.coordinates import great_circle_distance
from django.utils import timezone
import datetime


@python_2_unicode_compatible  # unicode support for Python 2
class Field(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    subfield = models.CharField(max_length=20)

    #set default:
    timestamp=datetime.datetime(2014,1,1,00,00)
    timestamp=timestamp.replace(tzinfo=timezone.utc)

    last_date = models.DateTimeField(default=timestamp)

    def __str__(self):
        return self.subfield


@python_2_unicode_compatible  # unicode support for Python 2
class Quadrant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


@python_2_unicode_compatible  # unicode support for Python 2
class Classification(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible  # unicode support for Python 2
class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="KSP-%s")
    date_disc = models.DateTimeField()
    ra = models.FloatField()
    dec = models.FloatField()
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    quadrant = models.ForeignKey(Quadrant, on_delete=models.CASCADE)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)
    disc_im = models.ImageField(max_length=1000)
    disc_ref = models.ImageField(max_length=1000)
    disc_sub = models.ImageField(max_length=1000)
    full_photom = models.BooleanField(default=False)  # True = have gone to full photom history; False = have not.
    simbad_flag = models.BooleanField(default=False)
    ned_flag = models.BooleanField(default=False)
    Bmag = models.FloatField(default=0.0)
    Vmag = models.FloatField(default=0.0)
    Imag = models.FloatField(default=0.0)
    Bstddev = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

    def is_same_target(self, candidate):
        """
        Figure out if two candidates are the same.
        :param candidate: candidate to compare
        :return: bool: True if the candidates have the same position (within 1")

        Notes
        -----
        We consider two targets to be the same if their positions are within 1" of each other.
        """
        return great_circle_distance(self.ra, self.dec,
                                     candidate.ra, candidate.dec) < (1.0 / 3600.0)


@python_2_unicode_compatible  # unicode support for Python 2
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User')
    text = models.CharField(max_length=500)
    pub_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text


@python_2_unicode_compatible  # unicode support for Python 2
class jpegImages(models.Model):
    id = models.AutoField(primary_key=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    date_txt = models.CharField(max_length=15)
    obs_date = models.DateTimeField()
    B_image = models.ImageField(max_length=1000)
    Bref_image = models.ImageField(max_length=1000)
    Bsub_image = models.ImageField(max_length=1000)
    B_prev_im = models.ImageField(max_length=1000)
    V_prev_im = models.ImageField(max_length=1000)
    I_prev_im = models.ImageField(max_length=1000)

    def __str__(self):
        return self.candidate.name


@python_2_unicode_compatible  # unicode support for Python 2
class Photometry(models.Model):
    id = models.AutoField(primary_key=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    obs_date = models.DateTimeField()
    obs_mjd = models.FloatField()
    filter = models.CharField(max_length=10)
    flux_ap = models.FloatField()
    dflux_ap = models.FloatField()
    flux_auto = models.FloatField()
    dflux_auto = models.FloatField()
    mag_ap = models.FloatField()
    dmag_ap = models.FloatField()
    mag_auto = models.FloatField()
    dmag_auto = models.FloatField()
    ra = models.FloatField()
    dec = models.FloatField()
    dra = models.FloatField()
    ddec = models.FloatField()
    class_star = models.FloatField()
    telescope = models.CharField(max_length=3)
    flag = models.BooleanField()  # True = detection; False = Obs, but not in files.

    def __str__(self):
        return self.candidate.name
