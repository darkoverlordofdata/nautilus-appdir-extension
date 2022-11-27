# nautilus-appdir-extension

Inspired by helloSystem

Plugin to support appdir format in Nautilus (Files)

an appdir is a file structure that looks like this:

./Application.app
./Application.app/Application
./Application.app/Resources/Application.png

this is the same basic format as GNUstep applications; in fact this uses '/usr/GNUstep/System/Tools/openapp' to launch the app.

* appdir_icon.py  - Iterates over the folder, replacing the folder icon with the .{app}.app/Resoures/{app}.png
* appdir_run.py   - Adds 'Run Application' to the context menu; runs .{app}.app/{app} 


## install
```
sudo apt install nautilus-python

git clone https://github.com/darkoverlordofdata/nautilus-appdir-extension.git
cd nautilus-appdir-extension
cp ./appdir_icon.py ~/.local/share/nautilus-python/extensions/appdir_icon.py
cp ./appdir_run.py ~/.local/share/nautilus-python/extensions/appdir_run.py

nautilus -q

```