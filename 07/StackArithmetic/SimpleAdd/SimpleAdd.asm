// === push constant 7 ===
@7 // D=i
D=A
@SP //*SP=D
A=M
M=D
@SP //SP++
M=M+1

// === push constant 8 ===
@8 // D=i
D=A
@SP //*SP=D
A=M
M=D
@SP //SP++
M=M+1

// === add ===
@SP
M=M-1 // pop
A=M   // D=*SP
D=M
@SP
M=M-1 // pop
A=M   //*SP=D+*SP
M=D+M
@SP   //SP++
M=M+1

(END)
  @END
  0;JMP