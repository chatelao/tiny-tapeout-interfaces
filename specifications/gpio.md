# GPIO Pin Specifications

There are a total of 26 I/O pins available for Tiny Tapeout designs:

| Name | Count | Direction | Description |
|------|-------|-----------|-------------|
| clk | 1 | Input | Clock input |
| rst_n | 1 | Input | Active low reset |
| ui_in[7:0] | 8 | Input | General purpose input |
| uo_out[7:0] | 8 | Output | General purpose output |
| uio[7:0] | 8 | Bidir | General purpose I/O |

## Limitations
- Maximum output frequency: 33 MHz
- Maximum input frequency: 66 MHz
- Drive strength: 4 mA
- IO supply voltage: 1.71V - 5.5V (3.3V on demo board)
