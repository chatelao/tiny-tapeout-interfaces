/**
 * WASM Interface for Tiny Tapeout Digital Twin
 */
export interface tt_DigitalTwin {
    /**
     * Sets the state of the 8-bit ui_in input bus.
     * @param value 8-bit integer
     */
    set_ui_in(value: number): void;

    /**
     * Sets the state of the 8-bit uio_in input/output bus (when used as input).
     * @param value 8-bit integer
     */
    set_uio_in(value: number): void;

    /**
     * Sets the state of the ena (enable) signal.
     * @param value boolean
     */
    set_ena(value: boolean): void;

    /**
     * Sets the state of the rst_n (active-low reset) signal.
     * @param value boolean
     */
    set_rst_n(value: boolean): void;

    /**
     * Advances the simulation by one clock cycle.
     */
    step(): void;

    /**
     * Returns the current 8-bit value of the uo_out output bus.
     * @returns 8-bit integer
     */
    get_uo_out(): number;

    /**
     * Returns the current 8-bit value of the uio_out input/output bus (when used as output).
     * @returns 8-bit integer
     */
    get_uio_out(): number;

    /**
     * Returns the current 8-bit value of the uio_oe (output enable) bus.
     * @returns 8-bit integer
     */
    get_uio_oe(): number;
}
