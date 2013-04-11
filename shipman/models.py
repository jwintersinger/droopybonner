from django.db import models

class Spacesuit(models.Model):
  size = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  colour = models.CharField(max_length=100)
  class Meta:
    db_table = 'spacesuits'
  def __unicode__(self):
    return '%s %s %s' % (self.size, self.colour, self.model)

class PlanetaryBody(models.Model):
  name = models.CharField(max_length=100)
  coord_x = models.FloatField()
  coord_y = models.FloatField()
  coord_z = models.FloatField()
  def __unicode__(self):
    return self.name
  class Meta:
    db_table = 'planetary_bodies'
    verbose_name_plural = 'planetary bodies'

class Atmosphere(models.Model):
  atmosphere = models.CharField(max_length = 100)
  def __unicode__(self):
    return self.atmosphere
  class Meta:
    db_table = 'atmospheres'

class Location(models.Model):
  planetary_body = models.ForeignKey(PlanetaryBody)
  address = models.CharField(max_length = 400)
  def __unicode__(self):
    return '%s on %s' % (self.address, self.planetary_body.__unicode__())
  class Meta:
    db_table = 'locations'

class Depot(models.Model):
  name = models.CharField(max_length=100)
  location = models.ForeignKey(Location)
  def __unicode__(self):
    return self.name
  class Meta:
    db_table = 'depots'

class Storefront(models.Model):
  name = models.CharField(max_length=100)
  location = models.ForeignKey(Location)
  def __unicode__(self):
    return self.name
  class Meta:
    db_table = 'storefronts'

class Spaceship(models.Model):
  volume = models.FloatField()
  type = models.CharField(max_length=100)
  current_coord_x = models.FloatField()
  current_coord_y = models.FloatField()
  current_coord_z = models.FloatField()
  destination = models.ForeignKey(Location)
  class Meta:
    db_table = 'spaceships'
  def __unicode__(self):
    return '%s m^3 spaceship at (%s, %s, %s)' % (
        self.volume,
        self.current_coord_x,
        self.current_coord_y,
        self.current_coord_z,
      )

class Hovertruck(models.Model):
  volume = models.FloatField()
  current_coord_x = models.FloatField()
  current_coord_y = models.FloatField()
  current_coord_z = models.FloatField()
  destination = models.ForeignKey(Location)
  class Meta:
    db_table = 'hovertrucks'
  def __unicode__(self):
    return '%s m^3 hovertruck at (%s, %s, %s)' % (
        self.volume,
        self.current_coord_x,
        self.current_coord_y,
        self.current_coord_z,
      )

class Employee(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  ssn = models.CharField(max_length=10, primary_key=True, verbose_name='SSN')
  supervisor = models.ForeignKey('self', blank=True, null=True)
  birthdate = models.DateField()
  salary = models.DecimalField(decimal_places=2, max_digits=15)
  spacesuits = models.ManyToManyField(Spacesuit)
  spaceship = models.ForeignKey(Spaceship, related_name='crew_members', null=True, blank=True)
  hovertruck = models.ForeignKey(Hovertruck, related_name='crew_members', null=True, blank=True)
  def __unicode__(self):
    return '%s %s' % (self.first_name, self.last_name)
  class Meta:
    db_table = 'employees'


class Customer(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  location = models.ForeignKey(Location)
  def __unicode__(self):
    return '%s %s' % (self.first_name, self.last_name)
  class Meta:
    db_table = 'customers'

class Package(models.Model):
  width = models.FloatField()
  height = models.FloatField()
  depth = models.FloatField()
  mass = models.FloatField()
  recipient = models.ForeignKey(Customer, related_name='received_packages')
  shipper = models.ForeignKey(Customer, related_name='shipped_packages')
  storefront = models.ForeignKey(Storefront, null=True, blank=True)
  depot = models.ForeignKey(Depot, null=True, blank=True)
  spaceship = models.ForeignKey(Spaceship, null=True, blank=True)
  hovertruck = models.ForeignKey(Hovertruck, null=True, blank=True)
  def __unicode__(self):
    return 'Package from %s to %s' % (self.shipper.__unicode__(), self.recipient.__unicode__())
  class Meta:
    db_table = 'packages'
