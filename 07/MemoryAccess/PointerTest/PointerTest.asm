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
@pointer_0 // pointer_0=D
M=D
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@pointer_0 // *pointer_0=D
A=M
M=D// === push constant 3040 ===
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
@pointer_1 // pointer_1=D
M=D
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@pointer_1 // *pointer_1=D
A=M
M=D// === push constant 32 ===
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
@this_2 // this_2=D
M=D
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@this_2 // *this_2=D
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
@that_6 // that_6=D
M=D
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@that_6 // *that_6=D
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