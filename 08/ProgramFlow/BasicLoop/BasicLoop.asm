// === push constant 0 ===
@0 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === pop local 0 ===
@LCL // D=LCL
D=M
@0 // D=LCL+i
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

// === label LOOP_START ===
(global$LOOP_START)

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

// === push local 0 ===
@LCL // *LCL=D
D=M
@0 // D=LCL+i
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

// === pop local 0 ===
@LCL // D=LCL
D=M
@0 // D=LCL+i
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

// === if-goto LOOP_START ===
@SP
M=M-1 // pop
A=M
D=M
@global$LOOP_START
D;JNE

// === push local 0 ===
@LCL // *LCL=D
D=M
@0 // D=LCL+i
A=D+A
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

(END)
  @END
  0;JMP