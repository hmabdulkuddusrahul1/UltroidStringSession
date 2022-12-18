#!/bin/bash
# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import os

url = "https://raw.githubusercontent.com/TeamUltroid/Ultroid/main/resources/session/ssgen.py"
os.system("wget {} -O SessionGen.py".format(url))
os.system("python3 SessionGen.py")
os.remove("SessionGen.py")
