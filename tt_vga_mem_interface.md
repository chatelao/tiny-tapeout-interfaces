# tt_ VGA Interface with FLASH / SRAM Extension

Standard VGA output combined with an external memory interface for frame buffering or asset storage.

## VGA Pins
- `uo_out[7:0]`: TinyVGA standard (R1, G1, B1, VSYNC, R0, G0, B0, HSYNC)

## Memory Extension (QSPI)
- `uio[0]`: CS (Flash/SRAM)
- `uio[1]`: MOSI / IO0
- `uio[2]`: MISO / IO1
- `uio[3]`: SCK
- `uio[4]`: IO2
- `uio[5]`: IO3
