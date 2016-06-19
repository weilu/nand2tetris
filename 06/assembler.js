var fs = require('fs')
var readline = require('readline')
var assert = require('assert')
var path = require('path')

var usage = 'usage: node assembler.js [path to .asm]'
assert(process.argv.length == 3, usage)

var asmFile = process.argv[2]
var instream = fs.createReadStream(asmFile, {encoding: 'utf8'})
var lineReader = readline.createInterface({ input: instream })

var symbols = {}
var parsed = ''
var SYMBOL_CONST = {
  SCREEN: 16384,
  KBD: 24576,
  SP: 0,
  LCL: 1,
  ARG: 2,
  THIS: 3,
  THAT: 4
}
instream.on('end', function() {
  Object.assign(symbols, SYMBOL_CONST)
  lines.forEach(function(line, i) {
    if (line.startsWith('@')) {
      parsed += parseAInstruction(line)
    } else {
      parsed += parseCInstruction(line)
    }
  })
  fs.writeFileSync(asmFile.replace(/asm$/, 'hack'), parsed)
})

var lineCount = 0
var symbolRegex = /^\((.+)\)$/
var lines = []
lineReader.on('line', function (line) {
  line = line.trim()
  if (line.startsWith('//') || line.length === 0) {
    return
  }

  // get rid of trailing comments
  if (line.indexOf('//') > 0) {
    line = line.substring(0, line.indexOf('//')).trim()
  }

  var match = symbolRegex.exec(line)
  if (match) {
    symbols[match[1]] = lineCount
  } else {
    lineCount++
    lines.push(line)
  }
})

var varCount = 16
function parseAInstruction(line) {
  assert(line.length > 1, 'Invalid A instruction. @ must be followed with positive integer or variable')
  var addr = line.substring(1)
  var addrRIndex = parseInt(addr.substring(1), 10)
  if (addr[0] === 'R' && addrRIndex >= 0 && addrRIndex <= 15) {
    addr = addrRIndex
  } else if (addr in symbols) {
    addr = symbols[addr]
  } else if (parseInt(addr, 10) !== parseInt(addr, 10)) {
    symbols[addr] = varCount
    addr = varCount
    varCount++
  }
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
