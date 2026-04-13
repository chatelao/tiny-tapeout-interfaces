# Pinout with Address Selection

This interface extends the basic GPIO pins with an address selection mechanism to access more than 8 bits of internal state.

## Pin Assignment
- `clk`: Clock input
- `ena`: Enable signal
- `rst_n`: Reset (active low)
- `ui_in[3:0]`: Data / Address Lower
- `ui_in[7]`: Address Latch
- `uo_out[7:0]`: Data Output
- `ua`: Analog output

## Address Selection Protocol
1. Set Address on `ui_in[3:0]`
2. Set `ui_in[7]` high to latch the address
3. Data appears on `uo_out`
