# snowrunner-uwp2steam

Tool to migrate the save data of the game Snowrunner from Microsoft Store / Xbox Game pass (UWP) to Steam.

## Description

The migration is basically just renaming a number of files which have obfuscated names in UWP storage, and then making Steam aware of them.
The "hard part" is discovering the proper file names, which are stored inside a `container.xyz` file with a proprietary binary format.

## References

The links below are the resources which were used to make this tool:

- [https://steamcommunity.com/sharedfiles/filedetails/?id=2530914231]
- [https://blog.s505.su/2021/08/how-to-transfer-snowrunner-game-saves.html]
- [https://steamcommunity.com/app/1465360/discussions/0/4811511685077534336/#c3111403360718313694]
  - (which is based on [https://github.com/zarroboogs/p4g-saveconv/blob/master/remotecache.py])
- [https://github.com/goatfungus/NMSSaveEditor/issues/306#issue-679701707]

## Usage

### Instructions

1. Have both Snowrunner UWP and Steam versions installed (ideally with the same DLC).
2. Find Snowrunner UWP save location, somewhere like: `%LOCALAPPDATA%\Packages\FocusHomeInteractiveSA.SnowRunnerWindows10_4hny5m903y3g0\SystemAppData\wgs\<an identifier>\<another identifier>`.
3. Make a copy of it to be safe, like `C:\Temp\<another identifier>`
4. Disable cloud saves for Snowrunner in Steam.
5. Restart Steam in offline mode.
6. Run Snowrunner and start a new game. Ensure the game is saved.
7. Download the [latest sr_u2s.exe tool](https://github.com/NeryK/snowrunner-uwp2steam/releases/latest/download/sr_u2s.exe) from the Releases page to any directory (like `C:\Temp`).
8. Open a command prompt (e.g. Windows key + R, input `cmd`, click OK), then navigate to the directory containing the tool (like `cd \Temp`).
9. Run the tool on the copy of the UWP data and write Steam data to a temporary directory: `sr_u2s.exe -i "C:\Temp\<another identifier>" -o "C:\Temp\steam_snowrunner_save"`
10. Find Steam saves location, somewhere like:`%ProgramFiles(x86)%\Steam\userdata\<your Steam id>\`
11. Copy the directory `1465360` from the Steam data output directory to the Steam saves location.
12. Run Snowrunner. If all went according to plan, you have recovered your save.
13. Re-enable cloud saves for the game and return online.

### Output

```text
C:\Temp>sr_u2s.exe -i "87F6B6416DF04148B19103F9EB436847" -o "steamsave"
Snowrunner save UWP -> Steam start.
Container file 87F6B6416DF04148B19103F9EB436847\container.150 loaded.
Copy 87F6B6416DF04148B19103F9EB436847\78F351653F064A6E98B5750FD260BD0A to steamsave\1465360\remote\CommonSslSave.cfg
Copy 87F6B6416DF04148B19103F9EB436847\60FE4239213B409A85DACF777A34B172 to steamsave\1465360\remote\CompleteSave.cfg
Copy 87F6B6416DF04148B19103F9EB436847\EB4435D95ADA4EE18C4F074E639976A5 to steamsave\1465360\remote\achievements.cfg
Copy 87F6B6416DF04148B19103F9EB436847\C471EB6D186C43B7AE4F0C0F5068BDA2 to steamsave\1465360\remote\fog_level_ru_02_01_crop.cfg
Copy 87F6B6416DF04148B19103F9EB436847\B51E9F3997414C728447DB5F1C4BB5DE to steamsave\1465360\remote\fog_level_ru_02_02.cfg
Copy 87F6B6416DF04148B19103F9EB436847\A5CD7552EBAC4A0DAF0BC3FEAED67AAD to steamsave\1465360\remote\fog_level_ru_02_03.cfg
Copy 87F6B6416DF04148B19103F9EB436847\19BB52EAF1AB4CA8ADCC32A10353FC6A to steamsave\1465360\remote\fog_level_ru_02_04.cfg
Copy 87F6B6416DF04148B19103F9EB436847\6AD5C2298EBD4608A3AA9BA1EBCA7996 to steamsave\1465360\remote\fog_level_us_01_01.cfg
Copy 87F6B6416DF04148B19103F9EB436847\03602F7D8B404A86B4FA3E0B4672EA5A to steamsave\1465360\remote\fog_level_us_01_02.cfg
Copy 87F6B6416DF04148B19103F9EB436847\0A0507BF59634FAD92F9AE953C206A87 to steamsave\1465360\remote\fog_level_us_01_03.cfg
Copy 87F6B6416DF04148B19103F9EB436847\4B85367394A64DFB845194191D0DBFB1 to steamsave\1465360\remote\fog_level_us_01_04_new.cfg
Copy 87F6B6416DF04148B19103F9EB436847\1D08A11E887E4511AE8B90259D615F9A to steamsave\1465360\remote\fog_level_us_02_01.cfg
Copy 87F6B6416DF04148B19103F9EB436847\CB7824A820E94118993D7EA226FB1D64 to steamsave\1465360\remote\fog_level_us_02_02_new.cfg
Copy 87F6B6416DF04148B19103F9EB436847\D452D4D24896491AB7EAD41D61A8794C to steamsave\1465360\remote\fog_level_us_02_03_new.cfg
Copy 87F6B6416DF04148B19103F9EB436847\826528AD61454CA7951CF9D973546228 to steamsave\1465360\remote\fog_level_us_02_04_new.cfg
Copy 87F6B6416DF04148B19103F9EB436847\3A69551A1D4D4C3293FBEB8B6A9F163E to steamsave\1465360\remote\sts_level_ru_02_01_crop.cfg
Copy 87F6B6416DF04148B19103F9EB436847\7355629AF37D4651B731C6BB2167AD40 to steamsave\1465360\remote\sts_level_ru_02_02.cfg
Copy 87F6B6416DF04148B19103F9EB436847\0D706726E6FF43FCAF458CFF29F135F7 to steamsave\1465360\remote\sts_level_ru_02_03.cfg
Copy 87F6B6416DF04148B19103F9EB436847\54C32F65F4324CB09FBDCC02FE90DCB6 to steamsave\1465360\remote\sts_level_ru_02_04.cfg
Copy 87F6B6416DF04148B19103F9EB436847\FABEF89DDCA24E4FB302D0F9379E492A to steamsave\1465360\remote\sts_level_us_01_01.cfg
Copy 87F6B6416DF04148B19103F9EB436847\075FD448E5374FDCA6BCE5F41BA4255A to steamsave\1465360\remote\sts_level_us_01_02.cfg
Copy 87F6B6416DF04148B19103F9EB436847\D33663780D0B469F884E18262E6AAFA9 to steamsave\1465360\remote\sts_level_us_01_03.cfg
Copy 87F6B6416DF04148B19103F9EB436847\FB0B8A0D0F374D68BB646B2629C39B8F to steamsave\1465360\remote\sts_level_us_01_04_new.cfg
Copy 87F6B6416DF04148B19103F9EB436847\C37E001B8B504612B52F740242C41360 to steamsave\1465360\remote\sts_level_us_02_01.cfg
Copy 87F6B6416DF04148B19103F9EB436847\4127379BE0D04B40BA35534DAA8BA2E0 to steamsave\1465360\remote\sts_level_us_02_02_new.cfg
Copy 87F6B6416DF04148B19103F9EB436847\03121689707F454AA76AC2DEB83ABD3B to steamsave\1465360\remote\sts_level_us_02_03_new.cfg
Copy 87F6B6416DF04148B19103F9EB436847\3C9415716F4F431BA5A253AF375A5429 to steamsave\1465360\remote\sts_level_us_02_04_new.cfg
Copy 87F6B6416DF04148B19103F9EB436847\F588515C63EC4BF888AA6CD097A0D2E0 to steamsave\1465360\remote\user_profile.cfg
Copy 87F6B6416DF04148B19103F9EB436847\36356A99CD2A45339A3B59C287533655 to steamsave\1465360\remote\user_settings.cfg
Copy 87F6B6416DF04148B19103F9EB436847\12A1682BC0754E11B68882FDA6302DAC to steamsave\1465360\remote\user_social_data.cfg
30 files copied.
Steam remote cache generated (steamsave\1465360\remotecache.vdf).
Snowrunner save UWP -> Steam end.
```

## Advanced

### Skip temporary directories

- Adventurous users can use the original UWP directory instead of making a temporary copy, as well as the final destination Steam directory as arguments of the tool.
  - Steps 3 and 11 can be avoided in this case.
  - Step 9 becomes `sr_u2s.exe -i "%LOCALAPPDATA%\Packages\FocusHomeInteractiveSA.SnowRunnerWindows10_4hny5m903y3g0\SystemAppData\wgs\<an identifier>\<another identifier>" -o "%ProgramFiles(x86)%\Steam\userdata\<your Steam id>\"`

### Use from source

- Steps 7 to 9 can be performed by downloading latest source or cloning the repo, then using it as a python module.
  - Install Python interpreter (>= 3.6).
  - `python -m sr_u2s -i "<input>" -o "<output>"`

### Build

Can be built as a Python module.

```sh
python -m pip install -U setuptools wheel
python setup.py sdist bdist_wheel
```

One-file bundled executable generated with pyinstaller.

```sh
python -m pip install -U pyinstaller
python -m PyInstaller -F -n sr_u2s sr_u2s/__main__.py
```
