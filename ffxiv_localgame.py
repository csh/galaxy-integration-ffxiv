import os
import sys
import logging
import subprocess
import xml.etree.ElementTree as ElementTree
import ffxiv_tools

from typing import List

class FFXIVLocalGame(object):
    def __init__(self, game_dir, game_executable):
        self._dir = game_dir.lower()
        self._executable = game_executable.lower()

    def exe_name(self) -> str:
        return self._executable

    def run_game(self) -> None:
        subprocess.Popen([os.path.join(self._dir, self._executable)], creationflags=0x00000008, cwd = self._dir)

    def delete_game(self) -> None:
        subprocess.Popen(ffxiv_tools.get_uninstall_exe(), creationflags=0x00000008, cwd = self._dir, shell=True)

def get_game_instances() -> List[FFXIVLocalGame]:
    result = list()
    install_folder = ffxiv_tools.get_installation_folder()
    xivlauncher_folder = ffxiv_tools.get_xivlauncher_folder()
    
    if (
        (xivlauncher_folder is not None) and 
        (os.path.exists(xivlauncher_folder))
    ):
        result.append(FFXIVLocalGame(xivlauncher_folder, "XIVLauncher.exe"))

    if (
        (install_folder is None) or
        (not os.path.exists(install_folder))
    ):
        return result

    result.append(FFXIVLocalGame(install_folder + "\\boot\\", "ffxivboot.exe"))
        
    return result
