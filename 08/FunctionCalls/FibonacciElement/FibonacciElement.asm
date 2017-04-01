@261
D=A
@SP
M=D // init SP
@Sys.init
0;JMP // goto Sys.init

// === function Main.fibonacci 0 ===
(Main.fibonacci)
@0
D=A-1
@Main.fibonacci$END_INIT_LOCALS
D;JLT
(Main.fibonacci$INIT_LOCALS)
  @LCL
  A=M+D
  M=0
  D=D-1
  @SP
  M=M+1 // forward SP to skip local pointer addresses
  @Main.fibonacci$INIT_LOCALS
  D;JGE
(Main.fibonacci$END_INIT_LOCALS)

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

// === lt ===
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@SP
M=M-1 // pop
A=M
D=M-D
@JLT_SET_TRUE_1
D;JLT
@SP
A=M
M=0
@JLT_RESUME_1
0;JMP
(JLT_SET_TRUE_1)
  @SP
  A=M
  M=-1
(JLT_RESUME_1)
@SP // SP++
M=M+1

// === if-goto IF_TRUE ===
@SP
M=M-1 // pop
A=M
D=M
@global$IF_TRUE
D;JNE

// === goto IF_FALSE ===
@global$IF_FALSE
0;JMP

// === label IF_TRUE ===
(global$IF_TRUE)

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

// === return ===
@LCL
D=M
@frame
M=D // frame = LCL
@return_addr
M=D
@5
D=A
@return_addr
A=M-D
D=M
@return_addr
M=D // return_addr = *(frame-5)
@SP
A=M-1 // pop
D=M // read return value
@ARG
A=M
M=D // save return value in current arg0
@ARG
D=M+1 // prepare SP restoration
@SP
M=D // SP = arg + 1
@frame
D=M
@tmpsp
AM=D-1 // tmpsp points to frame-1
D=M // read prev THAT value
@THAT
M=D // restore THAT
@tmpsp
AM=M-1 // pop
D=M // read prev THIS value
@THIS
M=D // restore THIS
@tmpsp
AM=M-1 // pop
D=M // read prev ARG value
@ARG
M=D // restore ARG
@tmpsp
AM=M-1 // pop
D=M // read prev LCL value
@LCL
M=D // restore LCL
@return_addr
A=M
0;JMP

// === label IF_FALSE ===
(global$IF_FALSE)

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

// === call function Main.fibonacci 1 ===
@Main.fibonacci_1$return_addr
D=A
@SP
A=M
M=D
@SP // SP++
M=M+1


@LCL
D=M
@SP
A=M
M=D
@SP // SP++
M=M+1


@ARG
D=M
@SP
A=M
M=D
@SP // SP++
M=M+1


@THIS
D=M
@SP
A=M
M=D
@SP // SP++
M=M+1


@THAT
D=M
@SP
A=M
M=D
@SP // SP++
M=M+1


@1
D=A
@5
D=D+A // save arg offset in D
@SP
D=M-D
@ARG
M=D // ARG=SP-n-5
@SP
D=M
@LCL
M=D // LCL=SP
@Main.fibonacci
0;JMP // goto f
(Main.fibonacci_1$return_addr)

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

// === call function Main.fibonacci 1 ===
@Main.fibonacci_2$return_addr
D=A
@SP
A=M
M=D
@SP // SP++
M=M+1


@LCL
D=M
@SP
A=M
M=D
@SP // SP++
M=M+1


@ARG
D=M
@SP
A=M
M=D
@SP // SP++
M=M+1


@THIS
D=M
@SP
A=M
M=D
@SP // SP++
M=M+1


@THAT
D=M
@SP
A=M
M=D
@SP // SP++
M=M+1


@1
D=A
@5
D=D+A // save arg offset in D
@SP
D=M-D
@ARG
M=D // ARG=SP-n-5
@SP
D=M
@LCL
M=D // LCL=SP
@Main.fibonacci
0;JMP // goto f
(Main.fibonacci_2$return_addr)

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

// === return ===
@LCL
D=M
@frame
M=D // frame = LCL
@return_addr
M=D
@5
D=A
@return_addr
A=M-D
D=M
@return_addr
M=D // return_addr = *(frame-5)
@SP
A=M-1 // pop
D=M // read return value
@ARG
A=M
M=D // save return value in current arg0
@ARG
D=M+1 // prepare SP restoration
@SP
M=D // SP = arg + 1
@frame
D=M
@tmpsp
AM=D-1 // tmpsp points to frame-1
D=M // read prev THAT value
@THAT
M=D // restore THAT
@tmpsp
AM=M-1 // pop
D=M // read prev THIS value
@THIS
M=D // restore THIS
@tmpsp
AM=M-1 // pop
D=M // read prev ARG value
@ARG
M=D // restore ARG
@tmpsp
AM=M-1 // pop
D=M // read prev LCL value
@LCL
M=D // restore LCL
@return_addr
A=M
0;JMP

// === function Sys.init 0 ===
(Sys.init)
@0
D=A-1
@Sys.init$END_INIT_LOCALS
D;JLT
(Sys.init$INIT_LOCALS)
  @LCL
  A=M+D
  M=0
  D=D-1
  @SP
  M=M+1 // forward SP to skip local pointer addresses
  @Sys.init$INIT_LOCALS
  D;JGE
(Sys.init$END_INIT_LOCALS)

// === push constant 4 ===
@4 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === call function Main.fibonacci 1 ===
@Main.fibonacci_3$return_addr
D=A
@SP
A=M
M=D
@SP // SP++
M=M+1


@LCL
D=M
@SP
A=M
M=D
@SP // SP++
M=M+1


@ARG
D=M
@SP
A=M
M=D
@SP // SP++
M=M+1


@THIS
D=M
@SP
A=M
M=D
@SP // SP++
M=M+1


@THAT
D=M
@SP
A=M
M=D
@SP // SP++
M=M+1


@1
D=A
@5
D=D+A // save arg offset in D
@SP
D=M-D
@ARG
M=D // ARG=SP-n-5
@SP
D=M
@LCL
M=D // LCL=SP
@Main.fibonacci
0;JMP // goto f
(Main.fibonacci_3$return_addr)

// === label WHILE ===
(global$WHILE)

// === goto WHILE ===
@global$WHILE
0;JMP

