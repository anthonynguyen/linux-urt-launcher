Linux UrT Launcher
==================

The urbanterror.info website has had a server browser for quite some time now, and it even comes with a nifty little program to start UrT by clicking on a link in the browser. Unfortunately, this program is Windows and Mac only and there hasn't been a Linux option, *until now*.


If you follow these simple steps, it should be up and running in no time.

## Instructions ##
1. Download these files:
    + [urt-handler.py](urt-handler.py)
    + [urt-handler.desktop](urt-handler.desktop)
    + [mimeapps.list](mimeapps.list)
2. Move the `urt-handler.py` to a location of your choosing
3. Update the `urt-handler.desktop` and change the line that starts with `Exec` to match the location where you put the `urt-handler.py` file.  
4. Move the `urt-handler.desktop` file to `~/.local/share/applications/`
5. Go to `~/.local/share/applications/` and look for a file called `mimeapps.list`  
    + If it exists, add the line `x-scheme-handler/urt=urt-handler.desktop` under the heading `[Added Associations]`
    + If it doesn't exist, copy the `mimeapps.list` file that I've given you to `~/.local/share/applications/`
6. That's it! Have fun using the online server browser!


If you have any issues, feel free to email me, message me on the UrT forums, or leave an issue here on Github.