/*
 * tt_ Verilog Interface
 * Implementing Address Selection and placeholders for VGA/Memory
 */
module tt_tt_um_gemini_interface (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered or selected
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

    // Pinout with Address Selection Logic
    // ui_in[3:0]: Data / Address Lower
    // ui_in[7]: Latch Address (active high)
    reg [3:0] addr_latch;
    always @(posedge clk) begin
        if (!rst_n) begin
            addr_latch <= 4'h0;
        end else if (ui_in[7]) begin
            addr_latch <= ui_in[3:0];
        end
    end

    // Internal "memory" for testing
    reg [7:0] registers [15:0];
    assign uo_out = registers[addr_latch];

    // Initialize registers
    integer i;
    always @(posedge clk) begin
        if (!rst_n) begin
            for (i=0; i<16; i=i+1) registers[i] <= i[7:0];
        end
    end

    // VGA + Memory Extension Placeholders
    // uio[0]: CS (Flash/SRAM)
    // uio[3]: SCK

    // Serial Interface (UART)
    // Design can optionally implement the TT_SERIAL protocol over UART.
    assign uio_oe = 8'b00000000; // All inputs by default
    assign uio_out = 8'b00000000;

endmodule
