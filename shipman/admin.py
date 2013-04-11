import shipman.models
from django.contrib import admin

class EmployeeAdminSpaceshipInline(admin.StackedInline):
  model = shipman.models.Employee
  exclude = ('hovertruck',)
  verbose_name = 'Crew member'
  verbose_name_plural = 'Crew members'

class EmployeeAdminHovertruckInline(admin.StackedInline):
  model = shipman.models.Employee
  exclude = ('spaceship',)
  verbose_name = 'Crew member'
  verbose_name_plural = 'Crew members'

class SpaceshipAdmin(admin.ModelAdmin):
  inlines = (EmployeeAdminSpaceshipInline,)

class HovertruckAdmin(admin.ModelAdmin):
  inlines = (EmployeeAdminHovertruckInline,)

admin.site.register(shipman.models.Spacesuit)
admin.site.register(shipman.models.Employee)
admin.site.register(shipman.models.PlanetaryBody)
admin.site.register(shipman.models.Atmosphere)
admin.site.register(shipman.models.Location)
admin.site.register(shipman.models.Depot)
admin.site.register(shipman.models.Storefront)
admin.site.register(shipman.models.Spaceship, SpaceshipAdmin)
admin.site.register(shipman.models.Hovertruck, HovertruckAdmin)
admin.site.register(shipman.models.Customer)
admin.site.register(shipman.models.Package)
