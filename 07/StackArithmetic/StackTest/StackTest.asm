// === push constant 17 ===
@17 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === push constant 17 ===
@17 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === eq ===
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@SP
M=M-1 // pop
A=M
D=M-D
@JEQ_SET_TRUE_1
D;JEQ
(JEQ_SET_FALSE_1)
  @SP
  A=M
  M=0
  @JEQ_RESUME_1
  0;JMP
(JEQ_SET_TRUE_1)
  @SP
  A=M
  M=-1
(JEQ_RESUME_1)
@SP // SP++
M=M+1

// === push constant 17 ===
@17 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === push constant 16 ===
@16 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === eq ===
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@SP
M=M-1 // pop
A=M
D=M-D
@JEQ_SET_TRUE_2
D;JEQ
(JEQ_SET_FALSE_2)
  @SP
  A=M
  M=0
  @JEQ_RESUME_2
  0;JMP
(JEQ_SET_TRUE_2)
  @SP
  A=M
  M=-1
(JEQ_RESUME_2)
@SP // SP++
M=M+1

// === push constant 16 ===
@16 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === push constant 17 ===
@17 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === eq ===
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@SP
M=M-1 // pop
A=M
D=M-D
@JEQ_SET_TRUE_3
D;JEQ
(JEQ_SET_FALSE_3)
  @SP
  A=M
  M=0
  @JEQ_RESUME_3
  0;JMP
(JEQ_SET_TRUE_3)
  @SP
  A=M
  M=-1
(JEQ_RESUME_3)
@SP // SP++
M=M+1

// === push constant 892 ===
@892 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === push constant 891 ===
@891 // D=i
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
@JLT_SET_TRUE_4
D;JLT
(JLT_SET_FALSE_4)
  @SP
  A=M
  M=0
  @JLT_RESUME_4
  0;JMP
(JLT_SET_TRUE_4)
  @SP
  A=M
  M=-1
(JLT_RESUME_4)
@SP // SP++
M=M+1

// === push constant 891 ===
@891 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === push constant 892 ===
@892 // D=i
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
@JLT_SET_TRUE_5
D;JLT
(JLT_SET_FALSE_5)
  @SP
  A=M
  M=0
  @JLT_RESUME_5
  0;JMP
(JLT_SET_TRUE_5)
  @SP
  A=M
  M=-1
(JLT_RESUME_5)
@SP // SP++
M=M+1

// === push constant 891 ===
@891 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === push constant 891 ===
@891 // D=i
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
@JLT_SET_TRUE_6
D;JLT
(JLT_SET_FALSE_6)
  @SP
  A=M
  M=0
  @JLT_RESUME_6
  0;JMP
(JLT_SET_TRUE_6)
  @SP
  A=M
  M=-1
(JLT_RESUME_6)
@SP // SP++
M=M+1

// === push constant 32767 ===
@32767 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === push constant 32766 ===
@32766 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === gt ===
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@SP
M=M-1 // pop
A=M
D=M-D
@JGT_SET_TRUE_7
D;JGT
(JGT_SET_FALSE_7)
  @SP
  A=M
  M=0
  @JGT_RESUME_7
  0;JMP
(JGT_SET_TRUE_7)
  @SP
  A=M
  M=-1
(JGT_RESUME_7)
@SP // SP++
M=M+1

// === push constant 32766 ===
@32766 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === push constant 32767 ===
@32767 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === gt ===
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@SP
M=M-1 // pop
A=M
D=M-D
@JGT_SET_TRUE_8
D;JGT
(JGT_SET_FALSE_8)
  @SP
  A=M
  M=0
  @JGT_RESUME_8
  0;JMP
(JGT_SET_TRUE_8)
  @SP
  A=M
  M=-1
(JGT_RESUME_8)
@SP // SP++
M=M+1

// === push constant 32766 ===
@32766 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === push constant 32766 ===
@32766 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === gt ===
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@SP
M=M-1 // pop
A=M
D=M-D
@JGT_SET_TRUE_9
D;JGT
(JGT_SET_FALSE_9)
  @SP
  A=M
  M=0
  @JGT_RESUME_9
  0;JMP
(JGT_SET_TRUE_9)
  @SP
  A=M
  M=-1
(JGT_RESUME_9)
@SP // SP++
M=M+1

// === push constant 57 ===
@57 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === push constant 31 ===
@31 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === push constant 53 ===
@53 // D=i
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

// === push constant 112 ===
@112 // D=i
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

// === neg ===
@SP
M=M-1 // pop
A=M
M=-M // *SP=-*SP
@SP // SP++
M=M+1

// === and ===
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@SP
M=M-1 // pop
A=M
M=D&M // *SP=D&*SP
@SP // SP++
M=M+1

// === push constant 82 ===
@82 // D=i
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

// === or ===
@SP
M=M-1 // pop
A=M
D=M // D=*SP
@SP
M=M-1 // pop
A=M
M=D|M // *SP=D|*SP
@SP // SP++
M=M+1

// === not ===
@SP
M=M-1 // pop
A=M
M=!M // *SP=!*SP
@SP // SP++
M=M+1

(END)
  @END
  0;JMP