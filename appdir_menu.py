"""
Support AppDir style folders: Add to menu

darkoverlordofdata
"""

from urllib.parse import urlparse, unquote
from gi.repository import GObject, Nautilus
import os


class AppDirAddToMenuProvider(GObject.GObject, Nautilus.MenuProvider):

    def add_to_menu(self, menu, file):

        file_path = unquote(urlparse(file.get_uri()).path)
        name = file.get_name()
        basename = os.path.basename(file_path).replace('.app', '')
        icon = file_path.replace('.app', f'.app/Resources/{basename}.png')
        home = os.environ['HOME']
        file_name = f'{home}/.local/share/applications/{basename}.desktop'

        content = '''#!/usr/bin/env xdg-open
[Desktop Entry]
Version=1.0
Terminal=false
Type=Application
Name={name}
Exec=/usr/GNUstep/System/Tools/openapp {file_path}
Icon={icon}
StartupWMClass={name}
'''.format(name=name, file_path=file_path, icon=icon)

        with open(file_name, 'w') as f:
            f.write(content)


    def get_file_items(self, window, files):
        if len(files) != 1:
            return 

        file = files[0]
        if not file.is_directory():
            return ()
        if not file.get_name().endswith('.app'):
            return ()



        menu_item = Nautilus.MenuItem(
                        name="add_to_menu",
                        label="Add To Menu")

        menu_item.connect('activate', self.add_to_menu, file)


        return menu_item,