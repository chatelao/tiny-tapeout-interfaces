# Recommended Pinouts

To ease bring-up and make it easier to reuse boards, Tiny Tapeout advocates for common pinouts.

## VGA Output
- uo_out[0]: R1
- uo_out[1]: G1
- uo_out[2]: B1
- uo_out[3]: vsync
- uo_out[4]: R0
- uo_out[5]: G0
- uo_out[6]: B0
- uo_out[7]: hsync

## SPI (Standard Pmod)
- uio[0]: CS
- uio[1]: MOSI
- uio[2]: MISO
- uio[3]: SCK

## QSPI Flash and PSRAM
- uio[0]: CS0 (Flash)
- uio[1]: SD0/MOSI
- uio[2]: SD1/MISO
- uio[3]: SCK
- uio[4]: SD2
- uio[5]: SD3
- uio[6]: CS1 (RAM A)
- uio[7]: CS2 (RAM B)
