# netbox_plugin.py

# Entry point for the NetBox plugin

from extras.plugins import PluginConfig

class CircuitIDConfig(PluginConfig):
    name = 'circuit_id'
    verbose_name = 'Circuit ID'
    description = 'Plugin to associate circuit IDs with cables'
    version = '0.1'
    base_url = 'circuit-id'
    min_version = '3.5.0'

config = CircuitIDConfig
