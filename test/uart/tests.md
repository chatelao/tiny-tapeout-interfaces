# UART Interface Tests

## Protocol Reset
Action:
Host sends: reset\n

Expect:
Device responds: ok\n

## Transaction Long Format
Action:
Host sends: ui;0x55;clk;1;rst_n;1;ena;1\n

Expect:
Device responds: uo;[uo_out];uio;[uio_out];uio_oe;[uio_oe]\n
