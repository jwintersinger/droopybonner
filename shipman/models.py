from django.db import models

class Spacesuit(models.Model):
  size = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  class Meta:
    db_table = 'spacesuits'

class Employee(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  ssn = models.CharField(max_length=10, primary_key=True)
  supervisor = models.ForeignKey('self')
  birthdate = models.DateTimeField()
  salary = models.DecimalField(decimal_places=2, max_digits=15)
  spacesuits = models.ManyToManyField(Spacesuit)
  class Meta:
    db_table = 'employees'

class PlanetaryBody(models.Model):
  coord_x = models.FloatField()
  coord_y = models.FloatField()
  coord_z = models.FloatField()
  class Meta:
    db_table = 'planetary_bodies'

class Atmosphere(models.Model):
  atmosphere = models.CharField(max_length = 100)
  class Meta:
    db_table = 'atmospheres'

class Location(models.Model):
  planetary_body = models.ForeignKey(PlanetaryBody)
  address = models.CharField(max_length = 400)
  class Meta:
    db_table = 'locations'

class Depot(models.Model):
  name = models.CharField(max_length=100)
  location = models.ForeignKey(Location)
  class Meta:
    db_table = 'depots'

class Storefront(models.Model):
  name = models.CharField(max_length=100)
  location = models.ForeignKey(Location)
  class Meta:
    db_table = 'storefronts'

class Spaceship(models.Model):
  crew_members = models.ForeignKey(Employee)
  volume = models.FloatField()
  type = models.CharField(max_length=100)
  current_coord_x = models.FloatField()
  current_coord_y = models.FloatField()
  current_coord_z = models.FloatField()
  destination = models.ForeignKey(Location)
  class Meta:
    db_table = 'spaceships'

class Hovertruck(models.Model):
  crew_members = models.ForeignKey(Employee)
  volume = models.FloatField()
  current_coord_x = models.FloatField()
  current_coord_y = models.FloatField()
  current_coord_z = models.FloatField()
  destination = models.ForeignKey(Location)
  class Meta:
    db_table = 'hovertrucks'

class Recipient(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  location = models.ForeignKey(Location)
  class Meta:
    db_table = 'recipients'

class Shipper(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  location = models.ForeignKey(Location)
  class Meta:
    db_table = 'shippers'

class Package(models.Model):
  width = models.FloatField()
  height = models.FloatField()
  depth = models.FloatField()
  mass = models.FloatField()
  spaceship = models.ForeignKey(Spaceship)
  hovertruck = models.ForeignKey(Hovertruck)
  storefront = models.ForeignKey(Storefront)
  depot = models.ForeignKey(Depot)
  recipient = models.ForeignKey(Recipient)
  shipper = models.ForeignKey(Shipper)
  class Meta:
    db_table = 'packages'
