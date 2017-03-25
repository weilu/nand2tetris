// === function SimpleFunction.test ===
(SimpleFunction.test)
@2
D=A-1
(SimpleFunction.test$INIT_LOCALS)
  @LCL
  A=M+D
  M=0
  D=D-1
  @SP
  M=M+1 // forward SP to skip local pointer addresses
  @SimpleFunction.test$INIT_LOCALS
  D;JGE

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

// === push local 1 ===
@LCL // *LCL=D
D=M
@1 // D=LCL+i
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

// === not ===
@SP
M=M-1 // pop
A=M
M=!M // *SP=!*SP
@SP // SP++
M=M+1

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

// === return ===
@SP
A=M-1
D=M // read return value
@return_value
M=D // save return value in var return_value
@LCL
D=M
@SP
M=D-1 // SP points to LCL-1
A=M
D=M // read prev THAT value
@THAT
M=D // restore THAT
@SP
M=M-1 // pop
A=M
D=M // read prev THIS value
@THIS
M=D // restore THIS
@SP
M=M-1 // pop
A=M
D=M // read prev ARG value
@ARG
M=D // restore ARG
@SP
M=M-1 // pop
A=M
D=M // read prev LCL value
@LCL
M=D // restore LCL
@SP
M=M-1 // pop
A=M
D=M
@return_addr
M=D // save return address in var return_addr
@return_value
D=M // hold return value in D
@SP
M=M-1 // pop to restore SP value
A=M-1
M=D // push return value to top of the stack
@return_addr
A=M // read return address value
0;JMP

(END)
  @END
  0;JMP