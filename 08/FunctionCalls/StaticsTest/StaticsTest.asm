@261
D=A
@SP
M=D // init SP
@Sys.init
0;JMP // goto Sys.init

// === function Class1.set 0 ===
(Class1.set)
@0
D=A-1
@Class1.set$END_INIT_LOCALS
D;JLT
(Class1.set$INIT_LOCALS)
  @LCL
  A=M+D
  M=0
  D=D-1
  @SP
  M=M+1 // forward SP to skip local pointer addresses
  @Class1.set$INIT_LOCALS
  D;JGE
(Class1.set$END_INIT_LOCALS)

@1337
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

@1337
// === pop static 0 ===
@Class1.0 // D=Class1.0
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

@1337
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

@1337
// === pop static 1 ===
@Class1.1 // D=Class1.1
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

@1337
// === push constant 0 ===
@0 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

@1337
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

@1337
// === function Class1.get 0 ===
(Class1.get)
@0
D=A-1
@Class1.get$END_INIT_LOCALS
D;JLT
(Class1.get$INIT_LOCALS)
  @LCL
  A=M+D
  M=0
  D=D-1
  @SP
  M=M+1 // forward SP to skip local pointer addresses
  @Class1.get$INIT_LOCALS
  D;JGE
(Class1.get$END_INIT_LOCALS)

@1337
// === push static 0 ===
@Class1.0 // D=*Class1.0
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

@1337
// === push static 1 ===
@Class1.1 // D=*Class1.1
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

@1337
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

@1337
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

@1337
// === function Class2.set 0 ===
(Class2.set)
@0
D=A-1
@Class2.set$END_INIT_LOCALS
D;JLT
(Class2.set$INIT_LOCALS)
  @LCL
  A=M+D
  M=0
  D=D-1
  @SP
  M=M+1 // forward SP to skip local pointer addresses
  @Class2.set$INIT_LOCALS
  D;JGE
(Class2.set$END_INIT_LOCALS)

@1337
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

@1337
// === pop static 0 ===
@Class2.0 // D=Class2.0
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

@1337
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

@1337
// === pop static 1 ===
@Class2.1 // D=Class2.1
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

@1337
// === push constant 0 ===
@0 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

@1337
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

@1337
// === function Class2.get 0 ===
(Class2.get)
@0
D=A-1
@Class2.get$END_INIT_LOCALS
D;JLT
(Class2.get$INIT_LOCALS)
  @LCL
  A=M+D
  M=0
  D=D-1
  @SP
  M=M+1 // forward SP to skip local pointer addresses
  @Class2.get$INIT_LOCALS
  D;JGE
(Class2.get$END_INIT_LOCALS)

@1337
// === push static 0 ===
@Class2.0 // D=*Class2.0
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

@1337
// === push static 1 ===
@Class2.1 // D=*Class2.1
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

@1337
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

@1337
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

@1337
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

@1337
// === push constant 6 ===
@6 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

@1337
// === push constant 8 ===
@8 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

@1337
// === call function Class1.set 2 ===
@Class1.set_1$return_addr
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


@2
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
@Class1.set
0;JMP // goto f
(Class1.set_1$return_addr)

@1337
// === pop temp 0 ===
@R5 // D=R5
D=A
@0 // D=R5+i
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

@1337
// === push constant 23 ===
@23 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

@1337
// === push constant 15 ===
@15 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

@1337
// === call function Class2.set 2 ===
@Class2.set_2$return_addr
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


@2
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
@Class2.set
0;JMP // goto f
(Class2.set_2$return_addr)

@1337
// === pop temp 0 ===
@R5 // D=R5
D=A
@0 // D=R5+i
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

@1337
// === call function Class1.get 0 ===
@Class1.get_3$return_addr
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


@0
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
@Class1.get
0;JMP // goto f
(Class1.get_3$return_addr)

@1337
// === call function Class2.get 0 ===
@Class2.get_4$return_addr
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


@0
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
@Class2.get
0;JMP // goto f
(Class2.get_4$return_addr)

@1337
// === label WHILE ===
(global$WHILE)

@1337
// === goto WHILE ===
@global$WHILE
0;JMP

@1337
