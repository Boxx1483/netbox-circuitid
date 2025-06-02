from extras.plugins import PluginMenuItem

menu_items = (
    PluginMenuItem(
        link='plugins:circuit_id:circuitid_list',
        link_text='Circuit IDs',
        permissions=['circuit_id.view_circuitid'],
    ),
)
