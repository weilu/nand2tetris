import sys
import re
from os import path
from janalyzer.tokenizer import tokenize
from janalyzer.parser import Parser


def strip_comments(source):
    source = re.sub(re.compile("/\*.*?\*/", re.DOTALL), "", source) # /* */
    source = re.sub(re.compile("//.*$", re.MULTILINE), "", source) # //
    source = re.sub(re.compile("^\s*$\n", re.MULTILINE), "", source) # blank line
    return source


def main():
    if len(sys.argv) != 2:
        print('Usage: ./JackAnalyzer.py input.jack')
        return

    infile = sys.argv[1]
    if not infile.endswith('.jack') and not path.isdir(infile):
        print('Usage: ./JackAnalyzer.py input.jack')
        return


    infiles = [infile]
    if path.isdir(infile):
        infile = path.abspath(infile)
        infiles = glob(path.join(infile, '*.jack'))


    for infile in infiles:
        # TODO: drop "Out" prefix before submission
        outfile = infile.replace('.jack', 'Out.xml')
        with open(outfile, 'w') as output_file:
            tokens = []
            with open(infile) as input_file:
                source = strip_comments(input_file.read())
                source = source.split('\n')
                for line in source:
                    tokens = tokens + tokenize(line.strip())
            parser = Parser(tokens)
            output_file.write(parser.compile())

if __name__ == "__main__":
    main()
