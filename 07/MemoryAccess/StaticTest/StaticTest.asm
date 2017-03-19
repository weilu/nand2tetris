// === push constant 111 ===
@111 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === push constant 333 ===
@333 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === push constant 888 ===
@888 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === pop static 8 ===
@StaticTest.8 // D=StaticTest.8
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

// === pop static 3 ===
@StaticTest.3 // D=StaticTest.3
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

// === pop static 1 ===
@StaticTest.1 // D=StaticTest.1
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

// === push static 3 ===
@StaticTest.3 // D=*StaticTest.3
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === push static 1 ===
@StaticTest.1 // D=*StaticTest.1
D=M
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

// === push static 8 ===
@StaticTest.8 // D=*StaticTest.8
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

(END)
  @END
  0;JMP