class PluginManager:
    def __init__(self):
        self._plugins = []

    def clear(self):
        self._plugins = []

    def add(self, plugin):
        #TODO: Prevent two plugins of same type being added
        self._plugins.append(plugin)

    def get_plugin(self):        
        for plugin in self._plugins:
            if plugin.enabled == True:
                return plugin

    def enable_plugin(self, class_name):
        for plugin in self._plugins:
            if plugin.__class__ == class_name:
                plugin.enable()
            else:
                plugin.disable()
        