# -*- coding: utf-8 -*-
import time
from bottle import route, run, template, post, request
import LCD_1in44
import LCD_Config

from PIL import Image,ImageDraw,ImageFont,ImageColor

port = 7735

LCD = LCD_1in44.LCD()
Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
LCD.LCD_Init(Lcd_ScanDir)

def _clear():
    LCD.LCD_Clear()

def _text(bg_color = "BLACK", lines = [], clear = False):
    image = Image.new("RGB", (LCD.width, LCD.height), bg_color)
    draw = ImageDraw.Draw(image)
    #font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 16)
    #print("***draw rectangle")
    #draw.rectangle([(0,127),(0,127)],fill = "RED")
    print("***draw text")
    line_height = 12
    y = -12
    for line in lines:
      x = line['x'] if 'x' in line else 0
      y = y + line_height
      text = line['text'] if 'text' in line else ''
      color = line['color'] if 'color' in line else "WHITE"
      draw.text((x, y), text, fill = color)
    LCD.LCD_ShowImage(image,0,0)
    LCD_Config.Driver_Delay_ms(500)

@post('/')
def post_text():
    data = dict(request.json)
    lines = data['lines'] if 'lines' in data else []
    clear = data['clear'] if 'clear' in data else False
    print(lines)
    _text(lines=lines, clear=clear)
    return

_text(lines=[
  dict({ "x": 0, "text": time.strftime("%Y/%m/%d @ %H:%M:%S", time.localtime())}),
  dict({ "x": 0, "text": "st7735s server ready"}),
  dict({ "x": 0, "text": "prototype.local:" + str(port)}),
  dict({ "x": 0, "text": "protocol: HTTP"}),
])

run(host='0.0.0.0', debug=True, reloader=True, port)
