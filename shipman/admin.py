import shipman.models
from django.contrib import admin, messages

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

class PackageAdmin(admin.ModelAdmin):
  readonly_fields = ('tracking_number',)
  def save_model(self, request, obj, form, change):
    obj.save()
    messages.add_message(request, messages.INFO, 'Package tracking number: %s' % obj.tracking_number)

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
admin.site.register(shipman.models.Package, PackageAdmin)
admin.site.register(shipman.models.PackageStatus)
