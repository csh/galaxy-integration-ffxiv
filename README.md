GOG Galaxy 2.0 Final Fantasy XIV integration

# Installation

Clone repository to `%localappdata%\GOG.com\Galaxy\plugins\installed\ffxiv`

# Working with code

## Before starting
Install Python extensions (shuold not be needed) `pip install -r requirements.txt -t ./modules --implementation cp --python-version 37 --only-binary=:all:`

## Files and folders
* ./html/
    * folder with html files that will popup when first connecting integration
* ./modules/
    * folder with installed python modules required for proper functionality of integration
* ./ffxiv_api.py
    * handles logging in and retrieving character details
* ./ffxiv_localgame.py
    * handles tasks with local game - starting, deleting
* ./ffxiv_tools.py
    * helper functions
* ./plugin.py
    * main script responsible for launching integration
* ./version.py
    * contains current version of integration
* ./manifest.json
    * contains identification info about integration
* ./requirements.txt
    * contains python modules required for proper functionality of integration
    
# Changelog
* v. 1.0.0
   * First working release 
   * Supports launching game, uninstalling game, detecting game launch and if it's running, synchronizing friends
   * Installing game currently not supported - WIP
   * Achievements syncing currently not supported - needs more research, may be unable to support because of platform limitations

# Thanks

[@gogcom](https://github.com/gogcom) for making GOG Galaxy 2 and giving me access to beta 
https://github.com/gogcom/galaxy-integrations-python-api

[@Mixaill](https://github.com/Mixaill) for his GOG Galaxy Guild Wars 2 integration which I used as base for this integration. https://github.com/Mixaill/galaxy-integration-gw2

[@viion](https://twitter.com/viion) for A FINAL FANTASY XIV: Online REST API https://xivapi.com/
