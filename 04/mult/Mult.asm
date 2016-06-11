// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

@i
M=0 // i=0

@2
M=0

(LOOP)
  @1
  D=M

  @i
  D=M-D

  @END
  D;JEQ // terminate if i = R1

  @0
  D=M

  @2
  M=M+D // R2 = R2 + R0

  @i
  M=M+1 // i++

  @LOOP
  0;JMP

(END)
  @END
  0;JMP
