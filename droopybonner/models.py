class Spacesuit(models.Model):
  size = models.CharField(max_length=100)
  model = models.CharField(max_length=100)

class Employee(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  ssn = models.CharField(max_length=10, primary_key=True)
  supervisor = models.ForeignKey('self')
  birthdate = models.DateTimeField()
  salary = models.DecimalField(decimal_places=2)
  spacesuits = models.ManyToManyField(Spacesuit)

class PlanetaryBody(models.Model):
  coord_x = models.FloatField()
  coord_y = models.FloatField()
  coord_z = models.FloatField()

class Atmosphere(models.Model):
  atmosphere = models.CharField(max_length = 100)

class Location(models.Model):
  planetary_body = models.ForeignKey(PlanetaryBody)
  address = models.CharField(max_length = 400)

class Depot(models.Model):
  name = models.CharField(max_length=100)
  location = models.ForeignKey(Location)

class Storefront(models.Model):
  name = models.CharField(max_length=100)
  location = models.ForeignKey(Location)

class Spaceship(models.Model):
  crew_members = models.ForeignKey(Employee)
  volume = models.FloatField()
  type = models.CharField(max_length=100)
  current_coord_x = models.FloatField()
  current_coord_y = models.FloatField()
  current_coord_z = models.FloatField()
  destination = models.ForeignKey(Location)

class Hovertruck(models.Model):
  crew_members = models.ForeignKey(Employee)
  volume = models.FloatField()
  current_coord_x = models.FloatField()
  current_coord_y = models.FloatField()
  current_coord_z = models.FloatField()
  destination = models.ForeignKey(Location)

class Recipient(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  location = models.ForeignKey(Location)

class Shipper(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  location = models.ForeignKey(Location)

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
