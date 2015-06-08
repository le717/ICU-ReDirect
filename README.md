# ICU ReDirect #
**ICU ReDirect** allows for automatic relocation of the save games in the 1997 Mindscape PC game [*LEGO Island*](http://en.wikipedia.org/wiki/Lego_Island).

## Usage ##
Simply click `Launch ICU ReDirect.bat` to launch ICU ReDirect. This tool supports both 32- and 64-bit Windows, so there is no need to choose the correct one. You will need Administrator rights to run ICU ReDirect as they are needed to write to the `HKEY_LOCAL_MACHINE` section of the Registry.

In what seems to be a design choice in Python, even if no Save Games are moved, the registry strings will be changed, and it will report a successful redirection.
However, there is no need to be alarmed, as it will always move your Save Games if they are really located in the original location it reports.
This incident will only happen if no Save Games exist at the original location.

## License ##
Created 2012-2013 [Triangle717](http://le717.github.io/)

[GPL v3](http://www.gnu.org/licenses/gpl.html)
