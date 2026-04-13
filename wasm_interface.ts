/**
 * WASM Interface for Tiny Tapeout Gemini
 */
export interface TinyTapeoutGemini {
    /**
     * Resets the design
     */
    reset(): void;

    /**
     * Steps the clock by one cycle
     */
    step(): void;

    /**
     * Sets the input pins (ui_in)
     * @param value 8-bit integer
     */
    setInputs(value: number): void;

    /**
     * Gets the output pins (uo_out)
     * @returns 8-bit integer
     */
    getOutputs(): number;

    /**
     * Sets bidirectional pins (uio_in)
     * @param value 8-bit integer
     */
    setBidir(value: number): void;

    /**
     * Gets bidirectional pins (uio_out)
     * @returns 8-bit integer
     */
    getBidir(): number;
}
