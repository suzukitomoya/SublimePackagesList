import sublime, sublime_plugin
from os import listdir

class PackagesListCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filelist = listdir(sublime.installed_packages_path())

        packages = []
        for filename in filelist:
            packages.append(filename.replace('.sublime-package', ''))

        self.view.insert(edit, 0, "\n".join(packages))
