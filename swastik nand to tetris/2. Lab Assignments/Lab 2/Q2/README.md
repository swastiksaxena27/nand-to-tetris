# Q2 – 16-bit Register Using HDL

## Objective
To design and implement a 16-bit Register chip using Hardware Description Language (HDL). The register stores 16-bit data and supports read and write operations.

## Files Included
1. `Bit.hdl` – Stores a single bit using a DFF.
2. `Register.hdl` – Combines 16 Bit chips to create a 16-bit register.

## Working
- The Register stores 16-bit binary data.
- The `in[16]` input provides the data.
- The `load` signal controls whether new data is stored.
- When `load = 1`, the register stores the input data.
- When `load = 0`, the register keeps its previous value.
- The stored data is available at the output.

## Sample Operations

| Operation | Input Data | Load | Output |
|-----------|------------|------|--------|
| Write 1 | 0000000000000101 | 1 | 0000000000000101 |
| Write 2 | 0000000000001010 | 1 | 0000000000001010 |
| Read | 0000000000000000 | 0 | 0000000000001010 |

## Conclusion
The 16-bit Register was implemented using HDL. It successfully demonstrates data storage, write operations, and reading previously stored data.

## Testing
The Register chip should be tested using the provided test script in the Hardware Simulator. .