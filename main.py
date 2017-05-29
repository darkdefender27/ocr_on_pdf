#!/usr/bin/env python

from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io

print "<< START >>"
tool = pyocr.get_available_tools()[0]
languages = tool.get_available_languages()

print languages

# Choose eng language
lang = languages[1]

req_image = []
final_text = []

print "<< END >>"