#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import jsbeautifier
import argparse
import commands
from urllib import unquote
import datetime

selected_text = os.getenv("POPCLIP_TEXT")

result = jsbeautifier.beautify(selected_text)

os.system('subl temp.txt')
os.system('pbpaste > temp.txt')
os.system('exit')
