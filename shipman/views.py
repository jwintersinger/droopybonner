from django.shortcuts import render, get_object_or_404
from shipman.forms import TrackPackageForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from shipman.models import Package, Stats

def index(request):
  track_package_form = TrackPackageForm()
  return render(request, 'shipman/index.html', {'track_package_form': track_package_form})

def analyze_stats(request):
  stats = Stats()
  context = {
    'packages_sent_received_by_same_person': stats.packages_sent_received_by_same_person(),
    'packages_with_sender_receiver_on_same_planet': stats.packages_with_sender_receiver_on_same_planet(),
    'shippers_with_most_unreceived_packages': stats.shippers_with_most_unreceived_packages(),
    'average_employee_salaries_per_class': stats.average_employee_salaries_per_class(),
  }
  return render(request, 'shipman/analyze_stats.html', context)

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
