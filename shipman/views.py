from django.shortcuts import render, get_object_or_404
from shipman.forms import TrackPackageForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from shipman.models import Package

def track_package_form(request):
  if request.method == 'POST':
    form = TrackPackageForm(request.POST)
    if form.is_valid():
      return HttpResponseRedirect(reverse('shipman.views.track_package',
        args=(form.cleaned_data['tracking_number'],)))
  else:
    form = TrackPackageForm()
  return render(request, 'shipman/track_package_form.html', {'form': form})

def track_package(request, tracking_number = None):
  package = get_object_or_404(Package, tracking_number = tracking_number)
  return render(request, 'shipman/track_package.html',
    {'package': package})
