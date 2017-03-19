// === push constant 10 ===
@10 // D=i
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
@local_0 // local_0=D
M=D
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@local_0 // *local_0=D
A=M
M=D// === push constant 21 ===
@21 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === push constant 22 ===
@22 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === pop argument 2 ===
@ARG // D=ARG
D=M
@2 // D=ARG+i
D=D+A
@argument_2 // argument_2=D
M=D
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@argument_2 // *argument_2=D
A=M
M=D// === pop argument 1 ===
@ARG // D=ARG
D=M
@1 // D=ARG+i
D=D+A
@argument_1 // argument_1=D
M=D
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@argument_1 // *argument_1=D
A=M
M=D// === push constant 36 ===
@36 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === pop this 6 ===
@THIS // D=THIS
D=M
@6 // D=THIS+i
D=D+A
@this_6 // this_6=D
M=D
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@this_6 // *this_6=D
A=M
M=D// === push constant 42 ===
@42 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === push constant 45 ===
@45 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === pop that 5 ===
@THAT // D=THAT
D=M
@5 // D=THAT+i
D=D+A
@that_5 // that_5=D
M=D
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@that_5 // *that_5=D
A=M
M=D// === pop that 2 ===
@THAT // D=THAT
D=M
@2 // D=THAT+i
D=D+A
@that_2 // that_2=D
M=D
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@that_2 // *that_2=D
A=M
M=D// === push constant 510 ===
@510 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === pop temp 6 ===
@R5 // D=R5
D=A
@6 // D=R5+i
D=D+A
@temp_6 // temp_6=D
M=D
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@temp_6 // *temp_6=D
A=M
M=D// === push local 0 ===
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

// === push that 5 ===
@THAT // *THAT=D
D=M
@5 // D=THAT+i
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

// === push this 6 ===
@THIS // *THIS=D
D=M
@6 // D=THIS+i
A=D+A
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === push this 6 ===
@THIS // *THIS=D
D=M
@6 // D=THIS+i
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

// === push temp 6 ===
@R5 // *R5=D
D=A
@6 // D=R5+i
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