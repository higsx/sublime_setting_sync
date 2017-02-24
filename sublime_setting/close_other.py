#将这个文件放在\Packages\User
#the plugin of user to close other tabs 
#{ "keys": ["shift+alt+o"], "command": "close_others"},


import sublime_plugin

class CloseOthersCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = self.view.window()
        group_index, view_index = window.get_view_index(self.view)
        window.run_command("close_others_by_index", { "group": group_index, "index": view_index})
