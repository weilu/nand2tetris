var fs = require('fs')
var readline = require('readline')
var assert = require('assert')
var path = require('path')

var usage = 'usage: node assembler.js [path to .asm]'
assert(process.argv.length == 3, usage)

var asmFile = process.argv[2]
var instream = fs.createReadStream(asmFile, {encoding: 'utf8'})
var lineReader = readline.createInterface({ input: instream })

var parsed = ''
instream.on('end', function() {
  console.log(parsed)
  fs.writeFileSync(asmFile.replace(/asm$/, 'hack'), parsed)
})

var lineCount = 0
lineReader.on('line', function (line) {
  line = line.trim()
  if (line.startsWith('//') || line.length === 0) {
    return
  }

  if (line.startsWith('@')) {
    parsed += parseAInstruction(line)
  } else {
    parsed += parseCInstruction(line)
  }
  console.log(lineCount, line)
  lineCount++
})

function parseAInstruction(line) {
  assert(line.length > 0, 'Invalid A instruction. @ must be followed with positive integer or variable')
  var addr = line.substring(1)
  return '0' + decbin(parseInt(addr, 10), 15) + '\n'
}

COMP = {
    '0': '101010',
    '1': '111111',
   '-1': '111010',
    'D': '001100',
    'A': '110000',
   '!D': '001101',
   '!A': '110001',
   '-D': '001111',
   '-A': '110011',
  'D+1': '011111',
  'A+1': '110111',
  'D-1': '001110',
  'A-1': '110010',
  'D+A': '000010',
  'D-A': '010011',
  'A-D': '000111',
  'D&A': '000000',
  'D|A': '010101'
}
DEST = {
    'M': '001',
    'D': '010',
   'MD': '011',
    'A': '100',
   'AM': '101',
   'AD': '110',
  'AMD': '111'
}
JUMP = {
  'JGT': '001',
  'JEQ': '010',
  'JGE': '011',
  'JLT': '100',
  'JNE': '101',
  'JLE': '110',
  'JMP': '111'
}
function parseCInstruction(line) {
  // dest=comp;jump
  // comp;jump
  // comp
  // dest=comp
  var compNJump = line.split(';')
  var jump = (compNJump[1] || '').trim()
  var destNComp = compNJump[0].split('=')
  var comp, dest;
  if (destNComp.length === 1) {
    comp = destNComp[0]
  } else {
    dest = destNComp[0].trim()
    comp = destNComp[1]
  }
  comp = comp.replace(/\s/g, '')

  var a = comp.indexOf('M') >= 0 ? '1' : '0'
  var compForLookup = comp.replace('M', 'A')
  var c = COMP[compForLookup] || '000000'
  var d = DEST[dest] || '000'
  var j = JUMP[jump] || '000'
  return '111' + a + c + d + j + '\n'
}

// http://stackoverflow.com/a/18827023/429288
function decbin(dec, length){
  var out = ""
  while(length--)
    out += (dec >> length ) & 1
  return out
}
