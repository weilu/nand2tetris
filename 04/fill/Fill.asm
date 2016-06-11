// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

(LOOP)

  @SCREEN // 256 x 512
  D=A
  @addr
  M=D  // addr = 16384

  @i
  M=0  // i = 0

  @KBD
  D=M

  @LOOP_BLACK
  D;JGT

  @LOOP_WHITE
  D;JEQ

(LOOP_WHITE)
  @i
  D=M
  @8192
  D=D-A
  @LOOP
  D;JEQ // jump to beginning of the loop if screen is filled i = 8192

  @addr
  A=M
  M=0 //RAM[addr]=0000000000000000

  @i
  M=M+1 // i++
  @1
  D=A
  @addr
  M=M+D // addr = addr + 1

  @LOOP_WHITE
  0;JMP

(LOOP_BLACK)
  @i
  D=M
  @8192
  D=D-A
  @LOOP
  D;JEQ // jump to beginning of the loop if screen is filled i = 8192

  @addr
  A=M
  M=-1 //RAM[addr]=1111111111111111

  @i
  M=M+1 // i++
  @1
  D=A
  @addr
  M=M+D // addr = addr + 1

  @LOOP_BLACK
  0;JMP

