#!/usr/bin/env python3
"""
assembler.py - Hack assembler (Nand to Tetris, ETCCNT301 capstone, Part B)

Usage:  python assembler.py Prog.asm        ->  writes Prog.hack

Extra feature (K = 7, K mod 3 = 1):
    For a wrong line, print a clear message with the line number
    (e.g. "Line 7: invalid instruction") instead of crashing.
    All wrong lines are reported, and no .hack file is written
    if there is at least one error.
"""
import sys

# ---------- lookup tables ----------
DEST = {'': '000', 'M': '001', 'D': '010', 'MD': '011',
        'A': '100', 'AM': '101', 'AD': '110', 'AMD': '111'}

JUMP = {'': '000', 'JGT': '001', 'JEQ': '010', 'JGE': '011',
        'JLT': '100', 'JNE': '101', 'JLE': '110', 'JMP': '111'}

# comp field written with 'A' (a-bit = 0)
COMP_A = {'0': '101010', '1': '111111', '-1': '111010',
          'D': '001100', 'A': '110000', '!D': '001101', '!A': '110001',
          '-D': '001111', '-A': '110011', 'D+1': '011111', 'A+1': '110111',
          'D-1': '001110', 'A-1': '110010', 'D+A': '000010', 'D-A': '010011',
          'A-D': '000111', 'D&A': '000000', 'D|A': '010101'}

COMP = {}
for text, bits in COMP_A.items():
    COMP[text] = '0' + bits                         # a = 0 (uses A)
    if 'A' in text:
        COMP[text.replace('A', 'M')] = '1' + bits   # a = 1 (uses M)

PREDEFINED = {'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4,
              'SCREEN': 16384, 'KBD': 24576}
for i in range(16):
    PREDEFINED['R%d' % i] = i


def clean(line):
    """Remove comments and ALL whitespace."""
    line = line.split('//')[0]
    return ''.join(line.split())


def first_pass(lines, errors):
    """Pass 1: remember where each label (LABEL) points.
    Returns (symbol table, list of (line number, instruction text))."""
    symbols = dict(PREDEFINED)
    program = []
    rom_address = 0
    for lineno, raw in enumerate(lines, start=1):
        text = clean(raw)
        if not text:
            continue                                # blank / comment-only line
        if text.startswith('('):
            if not text.endswith(')') or len(text) < 3:
                errors.append('Line %d: invalid label "%s"' % (lineno, text))
                continue
            name = text[1:-1]
            if name[0].isdigit():
                errors.append('Line %d: invalid label name "%s"' % (lineno, name))
            elif name in symbols:
                errors.append('Line %d: label "%s" is already defined' % (lineno, name))
            else:
                symbols[name] = rom_address         # label points to the NEXT instruction
            continue
        program.append((lineno, text))
        rom_address += 1
    return symbols, program


def translate_a(lineno, text, symbols, state, errors):
    """@value  ->  0 + 15-bit address"""
    value = text[1:]
    if value == '':
        errors.append('Line %d: invalid instruction (empty "@")' % lineno)
        return None
    if value.isdigit():
        number = int(value)
    else:
        if value[0].isdigit():
            errors.append('Line %d: invalid symbol "%s"' % (lineno, value))
            return None
        if value not in symbols:                    # new variable -> RAM 16, 17, 18, ...
            symbols[value] = state['next_var']
            state['next_var'] += 1
        number = symbols[value]
    if number > 32767:
        errors.append('Line %d: value %d is too large for an A-instruction'
                      % (lineno, number))
        return None
    return '0' + format(number, '015b')


def translate_c(lineno, text, errors):
    """dest=comp;jump  ->  111 + comp(7) + dest(3) + jump(3)"""
    dest, comp, jump = '', text, ''
    if '=' in text:
        dest, comp = text.split('=', 1)
    if ';' in comp:
        comp, jump = comp.split(';', 1)
    if dest not in DEST:
        errors.append('Line %d: invalid destination "%s" in "%s"' % (lineno, dest, text))
        return None
    if comp not in COMP:
        errors.append('Line %d: invalid instruction "%s"' % (lineno, text))
        return None
    if jump not in JUMP:
        errors.append('Line %d: invalid jump "%s" in "%s"' % (lineno, jump, text))
        return None
    return '111' + COMP[comp] + DEST[dest] + JUMP[jump]


def second_pass(program, symbols, errors):
    state = {'next_var': 16}
    out = []
    for lineno, text in program:
        if text.startswith('@'):
            code = translate_a(lineno, text, symbols, state, errors)
        else:
            code = translate_c(lineno, text, errors)
        if code is not None:
            out.append(code)
    return out


def assemble(path):
    try:
        with open(path) as f:
            lines = f.readlines()
    except OSError:
        print('ERROR: cannot open file "%s"' % path)
        return False

    errors = []
    symbols, program = first_pass(lines, errors)
    binary = second_pass(program, symbols, errors)

    if errors:                                      # ---- EXTRA FEATURE (K mod 3 == 1) ----
        for message in sorted(errors, key=lambda m: int(m.split()[1].rstrip(':'))):
            print(message)
        print('%d error(s) found - %s was NOT written.'
              % (len(errors), path.rsplit('.', 1)[0] + '.hack'))
        return False

    out_path = path.rsplit('.', 1)[0] + '.hack'
    with open(out_path, 'w') as f:
        f.write('\n'.join(binary) + '\n')
    print('%s -> %s (%d instructions)' % (path, out_path, len(binary)))
    return True


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python assembler.py Prog.asm')
        sys.exit(1)
    sys.exit(0 if assemble(sys.argv[1]) else 1)
