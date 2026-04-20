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

# Config
- Create every new issues with the label "jules" by default
  - Add the matching template
  - Disable the creation of empty issues without labels
- Add every "jules" labels issues to the project https://github.com/users/chatelao/projects/14

# ROADMAP rules
- Create and maintain a ROADMAP.md with checkboxes for tasks
  - Insert new tasks on the top of the list
  - Execute from bottom to top
  - Add a timestamp of completion on the end of each task when done
