// === push constant 7 ===
@7 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP  // SP++
M=M+1

// === push constant 8 ===
@8 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP  // SP++
M=M+1

// === add ===
@SP
M=M-1 // pop
A=M
D=M   // D=*SP
@SP
M=M-1 // pop
A=M
M=D+M // *SP=D+*SP
@SP   // SP++
M=M+1

(END)
  @END
  0;JMP