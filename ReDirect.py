"""
    This file is part of ICU (LEGO Island Configuration Utility)

    ICU - A collection of LEGO Island Configuration Tools
    Created 2012-2013 Triangle717 <http://triangle717.wordpress.com>

    ICU is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    ICU is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with ICU. If not, see <http://www.gnu.org/licenses/>.
"""

# ICU ReDirect V2
# Part of ICU (LEGO Island Configuration Utility)
# https://github.com/le717/ICU

# General use modules
import os
import sys
import time

# Main use modules
import winreg
import glob
import shutil

# Special purpose modules
import platform
import webbrowser

# Logging Code
import logging
import yourscorecube

# GUI elements
import tkinter
from tkinter import filedialog

# Global variables
app = "ICU ReDirect"
majver = "Version 2.0"
minver = "Stable"
creator = "Triangle717"
game = "LEGO Island"

# ------------ Begin ICU ReDirect Initialization ------------ #


def preload():
    '''Python 3.3.0 and Windows Architecture check'''

    logging.info("Begin logging to {0}".format(yourscorecube.logging_file))
    logging.info('''
                                #############################################
                                        {0} {1} {2}
                                        Copyright 2013 {3}
                                            YourScoreCube.log


                                    If you run into a bug, open an issue at
                                    https://github.com/le717/ICU/issues
                                    and attach this file for an easier fix!
                                #############################################
                                '''.format(app, majver, minver, creator))

     # You need to have at least Python 3.3.0 to run ICU ReDirect
    if sys.version_info < (3, 3, 0):
        logging.warning('''You are not running Python 3.3.0 or higher!
You need to get a newer version to run {0}'''.format(app))
        sys.stdout.write('''\nYou need to download Python 3.3.0 or greater
to run {0} {1} {2}.'''.format(app, majver, minver))

        # Don't open browser immediately
        time.sleep(2)
        logging.info("Open Python download page in a new tab in web browser.")
        # New tab, raise browser window (if possible)
        webbrowser.open_new_tab("http://python.org/download")

        # Close ICU ReDirect
        logging.info("Display error message for three seconds")
        time.sleep(3)
        logging.info("{0} is shutting down.".format(app))
        raise SystemExit(0)

    # If you are running Python 3.3.0
    else:
        logging.info('''You are running Python 3.3.0 or greater.
{0} will continue.'''.format(app))

        # Declare osbit global variable
        global osbit

        # User is running 64-bit Windows
        if platform.machine() == 'AMD64':
            logging.info("User is running 64-bit Windows.")
            osbit = "x64"
            main()

        # User is running 32-bit Windows
        elif platform.machine() == 'x86':
            logging.info("User is running 32-bit Windows.")
            osbit = "x86"
            main()

        # The user is running an unsupported version of Windows!
        else:
            logging.warning("User is running an unsupported OS!")
            print("\nYou are running an unsupported OS! {0} will now close."
            .format(app))
            time.sleep(3)
            logging.info("{0} is shutting down".format(app))
            raise SystemExit(0)


# ------------ End ICU ReDirect Initialization ------------ #


# ------------ Begin ICU ReDirect Menu Layout ------------ #


def main():
    '''ICU ReDirect Menu Layout'''

    print("\nWelcome to {0} {1} {2}\nCreated 2012-2013 {3}".format(
        app, majver, minver, creator))
    print('''\nPlease make a selection:\n
[r] ReDirect Save Games
[q] Quit''')
    menuopt = input("\n> ")
    while True:

        if menuopt.lower() == "r":
            logging.info("User pressed '[r] ReDirect Save Games'")
            ReDirect()

        elif menuopt.lower() == "q":
            logging.info("User pressed '[q] Quit'")
            print("\nGoodbye!")
            time.sleep(3)
            logging.info('''{0} is shutting down.
            '''.format(app))
            raise SystemExit(0)

        # Undefined input
        else:
            logging.info("User pressed an undefined key")
            main()


# ------------ End ICU ReDirect Menu Layout ------------ #


# ------------ Begin Save Game ReDirect Intro ------------ #


def ReDirect():
    '''Save Game ReDirect Launcher'''

    # Switch to 32-bit registry string code
    if osbit == "x86":
        logging.info("User is running 32-bit (x86) Windows, use x86 Registry Strings")
        eightsixReDirect()

    # Switch to 64-bit registry string code
    elif osbit == 'x64':
        logging.info("User is running 64-bit (x64) Windows, use x64 Registry Strings")
        sixfourReDirect()


# ------------ End Save Game ReDirect Intro ------------ #


# ------------ Begin Save Game ReDirect code for Windows x86 ------------ #


def eightsixReDirect():
    '''Redirects LEGO Island Save Games on Windows x86'''

    logging.info("'Open HKEY_LOCAL_MACHINE\SOFTWARE\Mindscape\LEGO Island\savepath' for reading")
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
    'SOFTWARE\Mindscape\LEGO Island', 0, winreg.KEY_READ) as oldx86save:
        oldx86path = winreg.QueryValueEx(oldx86save, 'savepath')

    # Convert tuple to str(ing)
    logging.info("Convert tuple returned by registry string to a string")
    oldx86path = "".join(str(oldx86path))

    # Clean up string to get a clean folder path
    logging.info("Cleaning up folder path...")
    oldx86path = oldx86path.strip("(''), 1")

    # Tell where current save games are located
    logging.info("Your {0} Save Games are currently located at {1}".format(game,
    oldx86path))
    print('\nYour {0} Save Games are currently located at\n"{1}"'.format(game,
    oldx86path))
    time.sleep(2)

    # Draw (then withdraw) the root Tk window
    logging.info("Drawing root Tk window")
    root = tkinter.Tk()
    logging.info("Withdrawing root Tk window")
    root.withdraw()

    # Select where you want your Save Games to be moved to
    # TODO: Make dialog active window automatically and
    # do the same to main window when closed.
    logging.info("Display folder selection dialog for new Save Game Location.")
    newsavepath = filedialog.askdirectory(
        title="Please select the new location for your {0} Save Games:".format(
            game))

    # The user clicked cancel
    if len(newsavepath) == 0:
        logging.warning("User canceled the Save Game redirection!")
        print("\nCanceling Save Game ReDirection...\n")
        time.sleep(1)
        main()

    # The user selected a folder
    else:
        logging.info("User selected a new Save Game location at {0}".format(
            newsavepath))

    try:
        # This checks for any *.GS files in savepath, and deletes them
        # This has to be done because Windows does not allow
        # a file to be overwritten. :|
        for root, dir, files in os.walk(newsavepath):
            for gsfile in files:
                if gsfile.upper().endswith(".GS"):
                    os.unlink(os.path.join(newsavepath, gsfile))

        # This checks for any *.gsi files in savepath, and deletes them
        # This has to be done because Windows does not allow
        # a file to be overwritten. :|
        for root, dir, files in os.walk(newsavepath):
            for gsifile in files:
                if gsifile.lower().endswith(".gsi"):
                    os.unlink(os.path.join(newsavepath, gsifile))

        # Move all *.GS files to the new path
            for gsfile in glob.glob("{0}/*.GS".format(oldx86path)):
                shutil.move(gsfile, newsavepath)

        # Move all *.gsi files to the new path
            for gsifile in glob.glob("{0}/*.gsi".format(oldx86path)):
                shutil.move(gsifile, newsavepath)

        '''So the final workflow is: if file exists: delete, then move.
        if not exists: move'''

        # Write Registry String with new path
        logging.info("'Write HKEY_LOCAL_MACHINE\SOFTWARE\Mindscape\LEGO Island\savepath' with new save path")
        with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE,
            'SOFTWARE\Mindscape\LEGO Island') as newx86savekey:
                winreg.SetValueEx(newx86savekey, "savepath",
                    0, winreg.REG_SZ, newsavepath)

        # Save games sucessfully redirected! :D
        print('\n{0} save games sucessfully redirected to "{1}".'.format(game,
        newsavepath))

        # The User does not have the rights to redirect the save games! D:
    except PermissionError:
        logging.warning('''{0} does not have the user rights to operate!
Please relaunch {0} as an Administrator.'''.format(app))
        print('''\n{0} does not have the user rights to operate!
Please relaunch {0} as an Administrator.'''.format(app))

    # Go back to main menu no matter the outcome
    finally:
        time.sleep(3)
        main()


# ------------ End Save Game ReDirect code for Windows x86 ------------ #


# ------------ Begin Save Game ReDirect code for Windows x64 ------------ #


def sixfourReDirect():
    '''Redirects LEGO Island Save Games on Windows x64'''

    logging.info("'Open HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Mindscape\LEGO Island\savepath' for reading")
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
        'SOFTWARE\Wow6432Node\Mindscape\LEGO Island', 0,
        winreg.KEY_READ) as oldx64save:
        oldx64path = winreg.QueryValueEx(oldx64save, 'savepath')

    # Convert tuple to str(ing)
    logging.info("Convert tuple returned by registry string to a string")
    oldx64path = "".join(str(oldx64path))

    # Clean up string to get a clean folder path
    logging.info("Cleaning up folder path...")
    oldx64path = oldx64path.strip("(''), 1")

    # Tell where current save games are located
    logging.info("Your {0} Save Games are currently located at {1}".format(game,
    oldx64path))
    print('\nYour {0} Save Games are currently located at\n"{1}"'.format(game,
    oldx64path))
    time.sleep(2)

    # Draw (then withdraw) the root Tk window
    logging.info("Drawing root Tk window")
    root = tkinter.Tk()
    logging.info("Withdrawing root Tk window")
    root.withdraw()

    # Select where you want your Save Games to be moved to
    # TODO: Make dialog active window automatically
    # and do the same to main window when closed.
    logging.info("Display folder selection dialog for new Save Game Location.")
    newsavepath = filedialog.askdirectory(
        title="Please select the new location for your {0} Save Games:".format(
            game))

    # The user clicked cancel
    if len(newsavepath) == 0:
        logging.warning("User canceled the Save Game redirection!")
        print("\nCanceling Save Game ReDirection...\n")
        time.sleep(1)
        main()

    # The user selected a folder
    else:
        logging.info("User selected a new Save Game location at {0}".format(
            newsavepath))

    try:
        # This checks for any *.GS files in savepath, and deletes them
        # This has to be done because Windows does not allow
        # a file to be overwritten. :|
        for root, dir, files in os.walk(newsavepath):
            for gsfile in files:
                if gsfile.upper().endswith(".GS"):
                    os.unlink(os.path.join(newsavepath, gsfile))

        # This checks for any *.gsi files in savepath, and deletes them
        # This has to be done because Windows does not allow
        # a file to be overwritten. :|
        for root, dir, files in os.walk(newsavepath):
            for gsifile in files:
                if gsifile.lower().endswith(".gsi"):
                    os.unlink(os.path.join(newsavepath, gsifile))

        # Move all *.GS files to the new path
            for gsfile in glob.glob("{0}/*.GS".format(oldx64path)):
                shutil.move(gsfile, newsavepath)

        # Move all *.gsi files to the new path
            for gsifile in glob.glob("{0}/*.gsi".format(oldx64path)):
                shutil.move(gsifile, newsavepath)

        '''So the final workflow is: if file exists: delete, then move.
        if not exists: move'''

        # Write Registry String with new path
        logging.info("'Write HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Mindscape\LEGO Island\savepath' with new save path")
        with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE,
            'SOFTWARE\Wow6432Node\Mindscape\LEGO Island') as newx64savekey:
                winreg.SetValueEx(newx64savekey, "savepath",
                    0, winreg.REG_SZ, newsavepath)

        # Save games sucessfully redirected! :D
        print('\n{0} save games sucessfully redirected to "{1}".'.format(game,
         newsavepath))

        # The User does not have the rights to redirect the save games! D:
    except PermissionError:
        logging.warning('''{0} does not have the user rights to operate!
Please relaunch {0} as an Administrator.'''.format(app))
        print('''\n{0} does not have the user rights to operate!
Please relaunch {0} as an Administrator.'''.format(app))

    # Go back to main menu no matter the outcome
    finally:
        time.sleep(3)
        main()


# ------------ End Save Game ReDirect code for Windows x64 ------------ #


if __name__ == "__main__":
    # Write window title (since there is no GUI)
    os.system("title {0} {1} {2}".format(app, majver, minver))
    # Run preload() to begin ICU ReDirect Initialization
    preload()