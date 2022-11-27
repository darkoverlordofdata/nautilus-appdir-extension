# nautilus-appdir-extension

Inspired by helloSystem

Plugin to support appdir format in Nautilus (Files)

an appdir is a file structure that looks like this:

./Application.app
./Application.app/Application
./Application.app/Resources/Application.png

this is the same basic format as GNUstep applications; in fact this uses '/usr/GNUstep/System/Tools/openapp' to launch the app.

appdir_icon.py  - Iterates over the folder, replacing the folder icon with the .<app>.app/Resoures/<app>.png
appdir_run.py   - Adds 'Run Application' to the context menu; runs .<app>.app/<app> 