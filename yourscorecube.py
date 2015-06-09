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

# ICU Logging code
# https://github.com/le717/ICU

# logging.BasicConfig code based on example from 'A Byte of Python'
# http://www.swaroopch.com/notes/Python

import os
import logging
import time

# ------------ Begin ICU Logging Code ------------ #


def appLoggingFolder():
    '''Checks for (and creates) ICU Logs folder'''

    try:
        # The Logs folder does not exist in the current directory
        if not os.path.exists(os.path.join(os.getcwd(), "Logs")):
            # Create the Logs folder
            os.mkdir(os.path.join(os.getcwd(), "Logs"))

    # User does not have Admin rights
    except PermissionError:
        print('''\nICU ReDirect does not have the user rights to operate!
Please relaunch ICU ReDirect as an Administrator.''')
        # Display message long enough so user can read it
        time.sleep(5)
        # Close program
        raise SystemExit


# AKA if this is imported as a module
if "__main__" != __name__:
    appLoggingFolder()

    # -- Begin Logging Config -- #

    logging_file = os.path.join(os.getcwd(), "Logs", 'YourScoreCube.log')

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s : %(levelname)s : %(message)s",
        filename=logging_file,
        filemode='a',
    )

    # -- End Logging Config -- #

# ------------ End ICU Logging Code ------------ #