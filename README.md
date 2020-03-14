# rpi.web.st7735s
A display service for the [waveshare st7735s based 1.44inch LCD raspberry display hat](https://www.waveshare.com/wiki/1.44inch_LCD_HAT)

## Docker requirements
- must be started with `--device=/dev/spidev0.0`:  
  - Replace `spidev0.0` by the spi interface used by the screen. I used `/dev/spidev0.0` for my tests.
- may require to be started with `--privileged`

## Upcoming
- line horizontal scroll
- multilines vertical scroll
- various color options
- display presets
- authentification

## Hardware specifications
From waveshare product page
- 1.44 inch
- LCD display technologie
- LED backlight
- 128x128 screen resolution
- RGB, 65K color
- 8 inputs:
  - 5 directions joystick
  - 3 keys

