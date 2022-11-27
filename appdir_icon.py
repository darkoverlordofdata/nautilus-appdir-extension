"""
Support AppDir style folders: Display app icon

darkoverlordofdata
"""

from gi.repository import GObject, Gtk, Nautilus
from urllib.parse import urlparse, unquote
import os
from urllib.parse import unquote, urlparse
from gi.repository import Gio

class AppDirIconPropertyPageProvider(GObject.GObject, Nautilus.PropertyPageProvider):

    def get_property_pages(self, files):
        if len(files) != 1:
            return 

        file = files[0]
        if not file.is_directory():
            return ()
        if not file.get_name().endswith('.app'):
            return ()

        property_label = Gtk.Label('Application Metadata')
        property_label.show()
        
        grid = Gtk.Grid()
        grid.props.margin_left = 50
        grid.props.margin_top = 20
        file_path = unquote(urlparse(file.get_uri()).path)
        name = file.get_name()
        basename = os.path.basename(file_path).replace('.app', '')
        icon = file_path.replace('.app', f'.app/Resources/{basename}.png')
        exe = file_path.replace('.app', f'.app/{basename}')
        metadata = {
            'name': name,
            'file_path': file_path,
            'basename': basename,
            'icon': icon,
            'exe': exe
        }

        gio = Gio.File.parse_name(file_path)
        gio.set_attribute_string("metadata::custom-icon", f'file://{icon}', Gio.FileQueryInfoFlags.NONE, None)

        for row, key in enumerate(['name', 'basename', 'file_path', 'icon', 'exe']):
            val = ",".join(metadata[key]) if isinstance(metadata[key], list) else metadata[key] 
            grid.attach(Gtk.Label(f'{key.capitalize()}: ', xalign=1), 0, row, 1, 1)
            grid.attach(Gtk.Label(val, xalign=0), 1, row, 1, 1)
        
        grid.show_all()

        page = Nautilus.PropertyPage(
                    name="epub_metadata",
                    label=property_label,
                    page=grid)

        return page,
