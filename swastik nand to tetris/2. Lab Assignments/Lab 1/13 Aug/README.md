# NAND2TETRIS LAB ASSIGNMENT

## Q1: Implementation of NOT, AND and OR Gates Using NAND Gates

### Objective
To implement NOT, AND and OR logic gates using only NAND gates in Hardware Description Language (HDL).

### HDL Files Included

1. **Not.hdl** – Implements NOT gate using one NAND gate.
2. **And.hdl** – Implements AND gate using two NAND gates.
3. **Or.hdl** – Implements OR gate using three NAND gates.

### Boolean Expressions

- NOT Gate: Y = A'
- AND Gate: Y = A · B
- OR Gate: Y = A + B

### Truth Tables

**NOT Gate**

| A | Output |
|---|---|
| 0 | 1 |
| 1 | 0 |

**AND Gate**

| A | B | Output |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**OR Gate**

| A | B | Output |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

### Verification
The HDL implementations are to be tested using the Nand2Tetris Hardware Simulator.

The following test scripts are used:

- Not.tst
- And.tst
- Or.tst

The simulation outputs should be compared with the expected output files (.cmp).

### Conclusion
NOT, AND and OR gates can be implemented successfully using only NAND gates. NAND is a universal logic gate because it can be used to construct other basic logic gates.