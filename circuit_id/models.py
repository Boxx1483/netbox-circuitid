from django.db import models
from netbox.models import NetBoxModel
from dcim.models import Cable

class CircuitID(NetBoxModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class CableCircuitID(models.Model):
    cable = models.OneToOneField(Cable, on_delete=models.CASCADE, related_name='circuit_id_link')
    circuit_id = models.ForeignKey(CircuitID, on_delete=models.CASCADE, related_name='cables')

    class Meta:
        unique_together = ('cable', 'circuit_id')
