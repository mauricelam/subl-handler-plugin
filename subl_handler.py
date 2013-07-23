import sublime
import sublime_plugin
import os


class RegisterSublHandlerCommand(sublime_plugin.ApplicationCommand):

    def __init__(self):
        sublime_plugin.ApplicationCommand.__init__(self)

    def run(self):
        os.system('open SublHandler.app')

try:
    with open('urlregister'):
        pass
except IOError:
    RegisterSublHandlerCommand().run()
    with open('urlregister', 'w') as f:
        f.write('yes')
