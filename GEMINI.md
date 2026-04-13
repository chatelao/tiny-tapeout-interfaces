# Goal

This repository defines the interfaces to access "Tiny Tapeout" implementations.

## Content
- Pinout w. address selection
- Verilog interface
- VGA interface with FLASH / SRAM extension
- WASM interface
- REST API

## Structure
- `/` : GEMINI.md, README.md and API definitions
- `/specifications` : Downloaded specifications, converted once to Markdown after downloading
- `/test` : CICD tests to verify the APIs are valid
- `/test/common` : Tools to unify the test processes
- `/test/<api-type>/install.sh` : To install tools necessary for the validation
- `/test/<api-type>/run_tests.sh` : To
- `/test/<api-type>/tests.md` : Appropriate test files with request / response pairs human readable, one test per chapter

## Housekeeping
- `/housekeeping/TOOL_WISHLIST.md` : Add tools to this list you needed to install during the work.
