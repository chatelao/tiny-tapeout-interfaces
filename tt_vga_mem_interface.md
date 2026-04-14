# VGA Interface with FLASH / SRAM Extension

Standard VGA output combined with an external memory interface for frame buffering or asset storage.
Compatible with the [QSPI Pmod](https://store.tinytapeout.com/products/QSPI-Pmod-p716541602).

## VGA Pins
- `uo_out[7:0]`: TinyVGA standard (R1, G1, B1, VSYNC, R0, G0, B0, HSYNC)

## Memory Extension (QSPI)
The interface is designed for the QSPI Pmod containing one Flash (25Q128JVSM) and two PSRAMs (APS6404L-3SQR).

- `uio[0]`: CS0 (Flash)
- `uio[1]`: SD0 / MOSI
- `uio[2]`: SD1 / MISO
- `uio[3]`: SCK
- `uio[4]`: SD2
- `uio[5]`: SD3
- `uio[6]`: CS1 (PSRAM A)
- `uio[7]`: CS2 (PSRAM B)
