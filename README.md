# Tiny Tapeout Gemini Interfaces

This repository defines the standard interfaces for accessing Tiny Tapeout implementations.

## Interfaces

- [Pinout w. Address Selection](tt_pinout_address.md)
- [Serial Interface (UART)](tt_serial_protocol.md)
- [Verilog Interface](tt_verilog_interface.v)
- [VGA with FLASH / SRAM Extension](tt_vga_mem_interface.md)
- [WASM Interface](tt_wasm_interface.ts)
- [REST API](tt_openapi.yaml) ([Online Documentation](https://chatelao.github.io/tiny-tapeout-interfaces/))

## Jules Automation

This repository uses automated issue management:
- **Labeling:** New issues are automatically labeled "jules".
- **Roadmap:** Issues are tracked in [ROADMAP.md](ROADMAP.md).
- **Project Board:** Issues are added to the [Project Board](https://github.com/users/chatelao/projects/14).

### Setup
To enable the project management automation, you need to add a Personal Access Token (PAT) with `repo` and `project` scopes to your repository secrets:
1. Create a PAT at [github.com/settings/tokens](https://github.com/settings/tokens).
2. Go to repository **Settings > Secrets and variables > Actions**.
3. Add a new repository secret named `ADD_TO_PROJECT_PAT` with your PAT.
