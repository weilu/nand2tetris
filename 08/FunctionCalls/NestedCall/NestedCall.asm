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

// === push constant 4000 ===
@4000 // D=i
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

// === push constant 5000 ===
@5000 // D=i
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

// === call function Sys.main 0 ===
@Sys.main$return_addr
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
@Sys.main
0;JMP // goto f
(Sys.main$return_addr)

// === pop temp 1 ===
@R5 // D=R5
D=A
@1 // D=R5+i
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

// === label LOOP ===
(global$LOOP)

// === goto LOOP ===
@global$LOOP
0;JMP

// === function Sys.main 5 ===
(Sys.main)
@5
D=A-1
@Sys.main$END_INIT_LOCALS
D;JLT
(Sys.main$INIT_LOCALS)
  @LCL
  A=M+D
  M=0
  D=D-1
  @SP
  M=M+1 // forward SP to skip local pointer addresses
  @Sys.main$INIT_LOCALS
  D;JGE
(Sys.main$END_INIT_LOCALS)

// === push constant 4001 ===
@4001 // D=i
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

// === push constant 5001 ===
@5001 // D=i
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

// === push constant 200 ===
@200 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === pop local 1 ===
@LCL // D=LCL
D=M
@1 // D=LCL+i
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

// === push constant 40 ===
@40 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === pop local 2 ===
@LCL // D=LCL
D=M
@2 // D=LCL+i
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

// === push constant 6 ===
@6 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === pop local 3 ===
@LCL // D=LCL
D=M
@3 // D=LCL+i
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

// === push constant 123 ===
@123 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === call function Sys.add12 1 ===
@Sys.add12$return_addr
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
@Sys.add12
0;JMP // goto f
(Sys.add12$return_addr)

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

// === push local 2 ===
@LCL // *LCL=D
D=M
@2 // D=LCL+i
A=D+A
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === push local 3 ===
@LCL // *LCL=D
D=M
@3 // D=LCL+i
A=D+A
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === push local 4 ===
@LCL // *LCL=D
D=M
@4 // D=LCL+i
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
@SP
A=M-1
D=M // read return value
@return_value
M=D // save return value in var return_value
@ARG
A=M
D=A
@SP
M=D // point SP to return value but do not write return value yet
@LCL
D=M
@tmpsp
M=D-1 // tmpsp points to LCL-1
A=M
D=M // read prev THAT value
@THAT
M=D // restore THAT
@tmpsp
M=M-1 // pop
A=M
D=M // read prev THIS value
@THIS
M=D // restore THIS
@tmpsp
M=M-1 // pop
A=M
D=M // read prev ARG value
@ARG
M=D // restore ARG
@tmpsp
M=M-1 // pop
A=M
D=M // read prev LCL value
@LCL
M=D // restore LCL
@tmpsp
M=M-1 // pop
A=M
D=M // read return address value
@return_addr
M=D // save return address in var return_addr
@return_value
D=M
@SP
A=M
M=D // write return value to SP
@SP // SP++
M=M+1


@return_addr
A=M
0;JMP

// === function Sys.add12 0 ===
(Sys.add12)
@0
D=A-1
@Sys.add12$END_INIT_LOCALS
D;JLT
(Sys.add12$INIT_LOCALS)
  @LCL
  A=M+D
  M=0
  D=D-1
  @SP
  M=M+1 // forward SP to skip local pointer addresses
  @Sys.add12$INIT_LOCALS
  D;JGE
(Sys.add12$END_INIT_LOCALS)

// === push constant 4002 ===
@4002 // D=i
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

// === push constant 5002 ===
@5002 // D=i
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

// === push constant 12 ===
@12 // D=i
D=A
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

// === return ===
@SP
A=M-1
D=M // read return value
@return_value
M=D // save return value in var return_value
@ARG
A=M
D=A
@SP
M=D // point SP to return value but do not write return value yet
@LCL
D=M
@tmpsp
M=D-1 // tmpsp points to LCL-1
A=M
D=M // read prev THAT value
@THAT
M=D // restore THAT
@tmpsp
M=M-1 // pop
A=M
D=M // read prev THIS value
@THIS
M=D // restore THIS
@tmpsp
M=M-1 // pop
A=M
D=M // read prev ARG value
@ARG
M=D // restore ARG
@tmpsp
M=M-1 // pop
A=M
D=M // read prev LCL value
@LCL
M=D // restore LCL
@tmpsp
M=M-1 // pop
A=M
D=M // read return address value
@return_addr
M=D // save return address in var return_addr
@return_value
D=M
@SP
A=M
M=D // write return value to SP
@SP // SP++
M=M+1


@return_addr
A=M
0;JMP

(END)
  @END
  0;JMP