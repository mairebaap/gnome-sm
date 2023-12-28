# ***G***sm (***GNOME*** shortcut maker)

### ***G***sm is a command-line tool to create .desktop files for adding shortcuts to the `gdm`.

## Prerequesties

 At least Python 3.10 (or greater) must be installed in the system.

## Installation

 Clone this repository in any directory and run the `run.sh` file.

## Usage
 There are four steps and one optional steps to make a `.desktop` shortcut. One has to do all steps except one optional. 

 Keep in mind that the user will be directly prompted either Y (yes) or N (no) and these are case-sensitive. If they fail to follow case, they will have to start all over again.

 Use the `rename.py` file to convert the file into the `.desktop` format.

### Here is how to use it.

---

```
python3 rename.py --fn shortcuts/progress.txt -ren myDesktopShortcut --ext .desktop
```
* ### `--fn` means filename
* ### `--ren` means rename
* ### `--ext` means extemsion