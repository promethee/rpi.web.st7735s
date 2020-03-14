# -*- coding: utf-8 -*-
import time
import re
from bottle import route, run, template, post, get, request
import LCD_1in44
import LCD_Config

from PIL import Image, ImageDraw, ImageFont, ImageColor

version = '1.0.0'

# WIDTH = 128
# HEIGHT = 128

port = 7735

LCD = LCD_1in44.LCD()
Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
LCD.LCD_Init(Lcd_ScanDir)

def _clear():
    LCD.LCD_Clear()

def _clean_text(text):
  w = 21
  return [text[y - w :y] for y in range(w, len(text) + w, w)]

def _text(bg_color = "BLACK", text = '', clear = False):
    image = Image.new("RGB", (LCD.width, LCD.height), bg_color)
    draw = ImageDraw.Draw(image)
    font_size = 8
    #font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 16)
    #print("***draw rectangle")
    #draw.rectangle([(0,127),(0,127)],fill = "RED")
    line_height = font_size
    x = 0
    y = line_height * -1
    text_chunks = _clean_text(text)
    for text_chunk in text_chunks:
      y = y + line_height
      draw.text((x, y), text_chunk, fill = "WHITE", spacing=1)
    LCD.LCD_ShowImage(image,0,0)
    LCD_Config.Driver_Delay_ms(500)

@post('/')
def post_text():
    data = dict(request.json)
    text = data['text'] if 'text' in data else ''
    clear = data['clear'] if 'clear' in data else False
    _text(text=text, clear=clear)
    return

_text(
  text=time.strftime(
    "%Y/%m/%d @ %H:%M:%S", time.localtime())
    + "                     "
    + "                     "
    + "rpi.web.st7735s      "
    + "                     "
    + "version " + version + "        "
    + "                     "
    + "st7735s server ready "
    + "                     "
    + "protocol: HTTP       "
    + "                     "
    + "method: POST         "
    + "                     "
    + "                     "
    + "github.com/promethee "
    + "                     "

)

@get('/')
def client():
  return template('templates/index')

run(host='0.0.0.0', debug=True, reloader=True, port=port)
