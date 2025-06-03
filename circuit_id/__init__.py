from netbox.plugins import PluginConfig


class CircuitIDConfig(PluginConfig):
    name = 'circuit_id'
    verbose_name = 'Circuit ID'
    description = 'Manage Circuit IDs for cables'
    version = '0.1'
    base_url = 'circuit-id'
    urlpatterns = 'circuit_id.urls'
    required_settings = []
    default_settings = {}

config = CircuitIDConfig