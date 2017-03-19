// === push constant 3030 ===
@3030 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === pop pointer 0 ===
@THIS // D=THIS
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

// === push constant 3040 ===
@3040 // D=i
D=A
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

// === push constant 32 ===
@32 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === pop this 2 ===
@THIS // D=THIS
D=M
@2 // D=THIS+i
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

// === push constant 46 ===
@46 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === pop that 6 ===
@THAT // D=THAT
D=M
@6 // D=THAT+i
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

// === push pointer 0 ===
@THIS // D=THIS
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === push pointer 1 ===
@THAT // D=THAT
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

// === push this 2 ===
@THIS // *THIS=D
D=M
@2 // D=THIS+i
A=D+A
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

// === push that 6 ===
@THAT // *THAT=D
D=M
@6 // D=THAT+i
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

(END)
  @END
  0;JMP