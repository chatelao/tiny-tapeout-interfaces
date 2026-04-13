# VGA Interface Tests

## Sync Signals
Expect:
uo_out[3] (VSYNC) and uo_out[7] (HSYNC) toggle correctly.

## Memory Access
Action:
uio[0] (CS) set low.

Expect:
QSPI interface becomes active.
