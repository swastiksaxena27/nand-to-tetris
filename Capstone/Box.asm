// Box.asm - black box while ANY key is pressed       (K = 7)
//   start row = 7   -> first word at SCREEN + 32*7 = 16384 + 224 = 16608
//   height    = 20 rows
//   width     = 16 * ((7 mod 4) + 1) = 16 * 4 = 64 pixels = 4 words

(LOOP)
    // ---- 1. read keyboard, choose colour ----
    @KBD
    D=M
    @PRESSED
    D;JNE           // key pressed -> go set black
    @color
    M=0             // no key -> white (0)
    @DRAW
    0;JMP
(PRESSED)
    @color
    M=-1            // key -> black (all 16 bits = 1)

(DRAW)
    // ---- 2. rowaddr = first word of the box, rows = 20 ----
    @16608
    D=A
    @rowaddr
    M=D
    @20
    D=A
    @rows
    M=D

(ROWLOOP)
    // ---- 3. addr = start of this row, cols = 4 words ----
    @rowaddr
    D=M
    @addr
    M=D
    @4
    D=A
    @cols
    M=D

(COLLOOP)
    // ---- 4. write colour into one word, move to next word ----
    @color
    D=M
    @addr
    A=M
    M=D
    @addr
    M=M+1
    @cols
    M=M-1
    D=M
    @COLLOOP
    D;JGT           // more words in this row?

    // ---- 5. go down one screen row (+32 words) ----
    @32
    D=A
    @rowaddr
    M=D+M
    @rows
    M=M-1
    D=M
    @ROWLOOP
    D;JGT           // more rows?

    @LOOP
    0;JMP           // check keyboard again, forever
