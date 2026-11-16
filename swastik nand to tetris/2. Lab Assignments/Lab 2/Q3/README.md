# Q3 – 8 Register File Using HDL

## Objective
To design an 8-register Register File using Hardware Description Language (HDL). It supports read and write operations using a 3-bit address.

## Files Included
1. `Bit.hdl` – Stores one bit of data using a DFF.
2. `Register.hdl` – Creates a 16-bit register using Bit chips.
3. `DMux8Way.hdl` – Selects one of the eight registers for writing.
4. `Mux8Way16.hdl` – Selects data from one of the eight registers for reading.
5. `RegisterFile.hdl` – Main chip that connects all eight registers.

## Working
- The Register File contains 8 registers (R0 to R7).
- Each register stores 16-bit data.
- A 3-bit address selects one of the eight registers.
- The `load` signal controls the write operation.
- The output shows the data stored in the selected register.

## Sample Write Operations

| Address | Input Data | Updated Register |
|---------|------------|------------------|
| 000 | 5  | R0 = 5 |
| 001 | 10 | R1 = 10 |
| 010 | 15 | R2 = 15 |
| 011 | 20 | R3 = 20 |

## Register States After Writes

| Register | Stored Value |
|----------|--------------|
| R0 | 5 |
| R1 | 10 |
| R2 | 15 |
| R3 | 20 |
| R4 | 0 |
| R5 | 0 |
| R6 | 0 |
| R7 | 0 |

## Read Operations
The address selects a register, and its stored value appears at the output.

- Address `000` → Output = 5
- Address `001` → Output = 10
- Address `010` → Output = 15
- Address `011` → Output = 20

## Conclusion
The 8-register Register File was designed using HDL with five supporting and main chip files. It allows data to be written into selected registers and read using a 3-bit address.