from machine import Pin, SPI as MICROPYTHON_SPI

from .spi import SPI

class SPIPICO(SPI):
    def init(self, baudrate: int, spi_bus: int, sck_pin: int, mosi_pin: int, miso_pin: int) -> Any :
        return MICROPYTHON_SPI(
            spi_bus,
            sck=Pin(sck_pin),
            mosi=Pin(mosi_pin),
            miso=Pin(miso_pin),
            baudrate=baudrate
        )