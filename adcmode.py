"""
    This module patches the flash to switch between ADC_VCC and ADC_A0 modes
    Courtesy of @ssendev and @eduvik on Github
    https://github.com/micropython/micropython/issues/2352
"""
import esp
from flashbdev import bdev
import machine

ADC_MODE_VCC = 255
ADC_MODE_ADC = 0

def set_adc_mode(mode):
    sector_size = bdev.SEC_SIZE
    flash_size = esp.flash_size() # device dependent
    init_sector = int(flash_size / sector_size - 4)
    data = bytearray(esp.flash_read(init_sector * sector_size, sector_size))
    if data[107] == mode:
        return True
    else:
        data[107] = mode  # re-write flash
        esp.flash_erase(init_sector)
        esp.flash_write(init_sector * sector_size, data)
        ## print("ADC mode changed in flash; restart to use it!")
    return False
