# snowrunner-uwp2steam

Tool to migrate the save data of the game Snowrunner from Microsoft Store / Xbox Game pass (UWP) to Steam.
The migration is basically just renaming a number of files which have obfuscated names in UWP storage, and then making Steam aware of them.

## References

- https://steamcommunity.com/sharedfiles/filedetails/?id=2530914231
- https://blog.s505.su/2021/08/how-to-transfer-snowrunner-game-saves.html
- https://steamcommunity.com/app/1465360/discussions/0/4811511685077534336/#c3111403360718313694
  - (which is based on https://github.com/zarroboogs/p4g-saveconv/blob/master/remotecache.py)
- https://github.com/goatfungus/NMSSaveEditor/issues/306#issue-679701707

## Usage

1. Have both Snowrunner UWP and Steam versions installed (ideally with the same DLC).
2. Find Snowrunner UWP save location, somewhere like: `%LOCALAPPDATA%\Packages\FocusHomeInteractiveSA.SnowRunnerWindows10_4hny5m903y3g0\SystemAppData\wgs\<an identifier>\<another identifier>`.
3. Make a copy of it to be safe, like `C:\Temp\<another identifier>`
4. Disable cloud saves for Snowrunner in Steam.
5. Restart Steam in offline mode.
6. Run Snowrunner and start a new game. Ensure the game is saved.
7. Run the tool on the copy of the UWP data and write Steam data to a temporary directory: `sr_u2s -i "C:\Temp\<another identifier>" -o "C:\Temp\steam_snowrunner_save"`
8. Find Steam saves location, somewhere like:`%ProgramFiles(x86)%\Steam\userdata\<your Steam id\`
9. Copy the directory `1465360` from the Steam data output directory to the Steam saves location.
10. Run Snowrunner. If all went according to plan, you have recovered your save.
11. Re-enable cloud saves for the game and return online.

## Build

Can be built as a Python module.

```
py -m pip install -U setuptools wheel
py setup.py sdist bdist_wheel
```

One-file bundled executable generated with pyinstaller.
```
py -m pip install -U pyinstaller
py -m PyInstaller -F -n sr_u2s sr_u2s/__main__.py
```
