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
@SP // pop
M=M-1
@SP // D=*SP
A=M
D=M
@SP // pop
M=M-1
@SP //*SP=D+*SP
A=M
M=D+M
@SP //SP++
M=M+1

(END)
  @END
  0;JMP