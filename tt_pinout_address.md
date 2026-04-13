# tt_ Pinout with Address Selection

This interface extends the basic GPIO pins with an address selection mechanism to access more than 8 bits of internal state.

## Pin Assignment
- `ui_in[3:0]`: Data / Address Lower
- `ui_in[7:4]`: Address Higher / Control
- `uo_out[7:0]`: Data Output

## Address Selection Protocol
1. Set Address on `ui_in`
2. Toggle a control bit (e.g., `ui_in[7]`) to latch address
3. Data appears on `uo_out`
