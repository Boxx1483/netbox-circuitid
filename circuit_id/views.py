from django.views.generic import ListView, DetailView
from .models import CircuitID

class CircuitIDListView(ListView):
    model = CircuitID
    template_name = 'circuit_id/circuitid_list.html'
    context_object_name = 'circuit_ids'

class CircuitIDDetailView(DetailView):
    model = CircuitID
    template_name = 'circuit_id/circuitid.html'
