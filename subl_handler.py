import sublime
import sublime_plugin
import os


class RegisterSublHandlerCommand(sublime_plugin.ApplicationCommand):

    def __init__(self):
        sublime_plugin.ApplicationCommand.__init__(self)
        self.settings = sublime.load_settings('SublHandler.sublime-settings')
        self.settings.add_on_change('subl', self.on_settings_change)

    def on_settings_change(self):
        path = self.settings.get('path', '/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl')
        appPath = os.path.join(sublime.packages_path(), 'SublHandler/SublHandler.app')
        os.system('open "' + appPath + '" --args -setPath "' + path + '"')

    def run(self):
        appPath = os.path.join(sublime.packages_path(), 'SublHandler/SublHandler.app')
        os.system('open "' + appPath + '"')

try:
    with open('urlregister'):
        pass
except IOError:
    # On first run
    RegisterSublHandlerCommand().on_settings_change()
    with open('urlregister', 'w') as f:
        f.write('yes')
