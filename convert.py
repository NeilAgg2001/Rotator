#!/usr/bin/env python
import fontforge
import sys

font = fontforge.open(sys.argv[1])
#font.removeGlyph(".notdef")
font.generate(sys.argv[2]+".ttf")
font.generate(sys.argv[2]+".otf")
font.close()