"""
Support AppDir style folders: Run the app

darkoverlordofdata
"""

from urllib.parse import urlparse, unquote
from subprocess import Popen
from gi.repository import GObject, Nautilus


class AppDirRunMenuProvider(GObject.GObject, Nautilus.MenuProvider):

    def run_application(self, menu, file):
        file_path = unquote(urlparse(file.get_uri()).path)
        cmd = [ '/usr/GNUstep/System/Tools/openapp', file_path ]
        Popen(cmd)


    def get_file_items(self, window, files):
        if len(files) != 1:
            return 

        file = files[0]
        if not file.is_directory():
            return ()
        if not file.get_name().endswith('.app'):
            return ()




        menu_item = Nautilus.MenuItem(
                        name="run_application",
                        label="Run Application")

        menu_item.connect('activate', self.run_application, file)

        return menu_item,