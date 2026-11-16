# Nand2Tetris Lab 1 — HDL files

This folder contains HDL implementations for the questions visible in the files.

## Q2 — XOR, MUX and DMUX

- `Xor.hdl` — 1-bit XOR
- `Mux.hdl` — 1-bit 2-way multiplexer
- `Mux16.hdl` — 16-bit 2-way multiplexer (supporting chip)
- `Mux4Way16.hdl` — 16-bit 4-way multiplexer
- `DMux.hdl` — 1-bit 2-way demultiplexer
- `DMux4Way.hdl` — 1-bit 4-way demultiplexer

### Truth tables

**XOR**

| a | b | out |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

**2-way MUX** — `sel=0` selects `a`; `sel=1` selects `b`.

| a | b | sel | out |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 0 | 1 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 |

**2-way DMUX** — `sel=0` sends `in` to `a`; `sel=1` sends `in` to `b`.

| in | sel | a | b |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

**4-way MUX selection**

| sel[1] | sel[0] | selected input |
|---|---|---|
| 0 | 0 | a |
| 0 | 1 | b |
| 1 | 0 | c |
| 1 | 1 | d |

**4-way DMUX selection**

| sel[1] | sel[0] | destination |
|---|---|---|
| 0 | 0 | a |
| 0 | 1 | b |
| 1 | 0 | c |
| 1 | 1 | d |

## Q3 — Half Adder and Full Adder
Folder: `Q3_Adders`

- `HalfAdder.hdl`
- `FullAdder.hdl`

**Half Adder**

| a | b | sum | carry |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

**Full Adder**

| a | b | c (carry-in) | sum | carry |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |
