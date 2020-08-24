from django.db import models

# Create your models here.
class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


class Musician(models.Model):
    YEAR_IN_SCHOOL_CHOICES = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=50)
    year_in_school_choice = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

class Runner(models.Model):
    MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
    name = models.CharField(verbose_name="Runner name",max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)

class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

class Manufacture(models.Model):
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacture, on_delete=models.CASCADE)

class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"

class Personal(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def baby_bommer_status(self):
        "Returns the person's baby-bommer status."
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"


    @property
    def full_name(self):
        "Returns the person's full name"
        return '%s %s' % (self.first_name, self.last_name)

class MyPersonal(Personal):
    class Meta:
        proxy = True

    def do_something(self):
        #...
        pass

class OrderedPersonal(Personal):
    class Meta:
        ordering = ["last_name"]
        proxy = True

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        if self.name == "Test":
            return
        else:
            super().save(*args, **kwargs)

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ['name']

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    class Meta(CommonInfo.Meta):
        db_table = 'student_info'

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

class Supplier(Place):
    customers = models.ManyToManyField(Place, related_name='provider')

class NewManager(models.Manager):
    #..
    pass

class MyPerson(Person):
    objects = NewManager()

    class Meta:
        proxy = True

class ExtraManagers(models.Model):
    secondary = NewManager()

    class Meta:
        abstract = True

class MyPerson(Person, ExtraManagers):
    class Meta:
        proxy = True
