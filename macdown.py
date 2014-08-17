import sublime
import sublime_plugin
import os
import subprocess

class OpenMacdownCommand(sublime_plugin.WindowCommand):
    def run(self, paths=[], parameters=None):
        file_path = self.window.active_view().file_name()
        file_name, file_ext = os.path.splitext(file_path)
        if not file_path:
            sublime.error_message("To open MacDown you must be have a markdown file opened.")
            return
        if not file_ext in [".md", ".markdown"]:
            sublime.error_message("A markdown file extension must be opened, you open an: " + file_ext + " extension.")
            return

        subprocess.Popen(['open', '/Applications/MacDown.app/', '--args', file_path])
