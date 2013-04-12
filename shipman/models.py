from django.db import models
from django.db.models.signals import pre_save, post_save
from datetime import datetime
import hashlib

class Spacesuit(models.Model):
  size = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  colour = models.CharField(max_length=100)
  class Meta:
    db_table = 'spacesuits'
  def __str__(self):
    return '%s %s %s' % (self.size, self.colour, self.model)

class PlanetaryBody(models.Model):
  name = models.CharField(max_length=100)
  coord_x = models.FloatField()
  coord_y = models.FloatField()
  coord_z = models.FloatField()
  def __str__(self):
    return self.name
  class Meta:
    db_table = 'planetary_bodies'
    verbose_name_plural = 'planetary bodies'

class Atmosphere(models.Model):
  atmosphere = models.CharField(max_length = 100)
  def __str__(self):
    return self.atmosphere
  class Meta:
    db_table = 'atmospheres'

class Location(models.Model):
  street_address = models.CharField(max_length = 400)
  city = models.CharField(max_length = 100)
  province = models.CharField(max_length = 100)
  postal_code = models.CharField(max_length = 100)
  country = models.CharField(max_length = 100)
  planetary_body = models.ForeignKey(PlanetaryBody)
  def __str__(self):
    return '%s, %s, %s, %s on %s' % (
      self.street_address,
      self.city,
      self.province,
      self.country,
      self.planetary_body
    )
  class Meta:
    db_table = 'locations'

class Depot(models.Model):
  name = models.CharField(max_length=100)
  location = models.ForeignKey(Location)
  def __str__(self):
    return self.name
  class Meta:
    db_table = 'depots'

class Storefront(models.Model):
  name = models.CharField(max_length=100)
  location = models.ForeignKey(Location)
  def __str__(self):
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
  def __str__(self):
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
  def __str__(self):
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
  def __str__(self):
    return '%s %s' % (self.first_name, self.last_name)
  class Meta:
    db_table = 'employees'


class Customer(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  location = models.ForeignKey(Location)
  def __str__(self):
    return '%s %s' % (self.first_name, self.last_name)
  class Meta:
    db_table = 'customers'

class Package(models.Model):
  tracking_number = models.CharField(max_length=100, primary_key=True)
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
  delivered = models.BooleanField()
  def __str__(self):
    return 'Package from %s to %s' % (self.shipper, self.recipient)
  class Meta:
    db_table = 'packages'

  def determine_status(self):
    if self.delivered:
      return 'delivered to %s' % self.recipient
    elif self.depot:
      return 'at depot %s (%s)' % (self.depot, self.depot.location)
    elif self.storefront:
      return 'at storefront %s (%s)' % (self.storefront, self.storefront.location)
    elif self.spaceship:
      return 'on %s' % str(self.spaceship)
    elif self.hovertruck:
      return 'on %s' % str(self.hovertruck)
    else:
      return 'at unknown location'

  def most_recent_status(self):
    statuses = self.statuses.all()
    if statuses:
      return statuses[0]
    else:
      return None

def generate_tracking_number(sender, instance, **kwargs):
  package = instance
  # Only generate tracking number if it doesn't already exist.
  if package.tracking_number:
    return
  hasher = hashlib.md5()
  hash_payload = ', '.join([str(e) for e in (datetime.now(), package.shipper, package.recipient)])
  hasher.update(hash_payload.encode('utf8'))
  package.tracking_number = hasher.hexdigest().upper()
pre_save.connect(generate_tracking_number, sender=Package, dispatch_uid='Hello, bananas.')

class PackageStatus(models.Model):
  package = models.ForeignKey(Package, related_name='statuses')
  status = models.CharField(max_length = 400)
  datetime = models.DateTimeField(auto_now_add = True)
  def __str__(self):
    return '%s was %s at %s' % (
        self.package,
        self.status,
        self.datetime
      )
  class Meta:
    db_table = 'package_statuses'
    verbose_name_plural = 'package statuses'
    ordering = ['-datetime']

def record_package_status(sender, instance, **kwargs):
  package = instance
  current_status = package.determine_status()
  most_recent_status = package.most_recent_status()
  if most_recent_status:
    most_recent_status = most_recent_status.status
  else:
    most_recent_status = ''

  if current_status != most_recent_status:
    PackageStatus.objects.create(package = instance, status = current_status)
post_save.connect(record_package_status, sender=Package, dispatch_uid='Hello, strawberries.')
