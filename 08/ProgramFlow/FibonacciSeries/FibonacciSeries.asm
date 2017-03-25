// === push argument 1 ===
@ARG // *ARG=D
D=M
@1 // D=ARG+i
A=D+A
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === pop pointer 1 ===
@THAT // D=THAT
D=A
@tmp // tmp=D
M=D
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@tmp // *tmp=D
A=M
M=D

// === push constant 0 ===
@0 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === pop that 0 ===
@THAT // D=THAT
D=M
@0 // D=THAT+i
D=D+A
@tmp // tmp=D
M=D
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@tmp // *tmp=D
A=M
M=D

// === push constant 1 ===
@1 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === pop that 1 ===
@THAT // D=THAT
D=M
@1 // D=THAT+i
D=D+A
@tmp // tmp=D
M=D
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@tmp // *tmp=D
A=M
M=D

// === push argument 0 ===
@ARG // *ARG=D
D=M
@0 // D=ARG+i
A=D+A
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === push constant 2 ===
@2 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === sub ===
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@SP
M=M-1 // pop
A=M
M=M-D // *SP=*SP-D
@SP // SP++
M=M+1

// === pop argument 0 ===
@ARG // D=ARG
D=M
@0 // D=ARG+i
D=D+A
@tmp // tmp=D
M=D
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@tmp // *tmp=D
A=M
M=D

// === label MAIN_LOOP_START ===
(global$MAIN_LOOP_START)

// === push argument 0 ===
@ARG // *ARG=D
D=M
@0 // D=ARG+i
A=D+A
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === if-goto COMPUTE_ELEMENT ===
@SP
M=M-1 // pop
A=M
D=M
@global$COMPUTE_ELEMENT
D;JNE

// === if-goto END_PROGRAM ===
@SP
M=M-1 // pop
A=M
D=M
@global$END_PROGRAM
0;JMP

// === label COMPUTE_ELEMENT ===
(global$COMPUTE_ELEMENT)

// === push that 0 ===
@THAT // *THAT=D
D=M
@0 // D=THAT+i
A=D+A
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === push that 1 ===
@THAT // *THAT=D
D=M
@1 // D=THAT+i
A=D+A
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === add ===
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@SP
M=M-1 // pop
A=M
M=D+M // *SP=D+*SP
@SP // SP++
M=M+1

// === pop that 2 ===
@THAT // D=THAT
D=M
@2 // D=THAT+i
D=D+A
@tmp // tmp=D
M=D
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@tmp // *tmp=D
A=M
M=D

// === push pointer 1 ===
@THAT // D=THAT
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === push constant 1 ===
@1 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === add ===
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@SP
M=M-1 // pop
A=M
M=D+M // *SP=D+*SP
@SP // SP++
M=M+1

// === pop pointer 1 ===
@THAT // D=THAT
D=A
@tmp // tmp=D
M=D
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@tmp // *tmp=D
A=M
M=D

// === push argument 0 ===
@ARG // *ARG=D
D=M
@0 // D=ARG+i
A=D+A
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === push constant 1 ===
@1 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === sub ===
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@SP
M=M-1 // pop
A=M
M=M-D // *SP=*SP-D
@SP // SP++
M=M+1

// === pop argument 0 ===
@ARG // D=ARG
D=M
@0 // D=ARG+i
D=D+A
@tmp // tmp=D
M=D
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@tmp // *tmp=D
A=M
M=D

// === if-goto MAIN_LOOP_START ===
@SP
M=M-1 // pop
A=M
D=M
@global$MAIN_LOOP_START
0;JMP

// === label END_PROGRAM ===
(global$END_PROGRAM)

(END)
  @END
  0;JMP