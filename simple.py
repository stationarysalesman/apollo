"""Generate random sentences from a grammar.  The grammar
consists of entries that can be written as S = 'NP VP | S and S',
which gets translated to {'S': [['NP', 'VP'], ['S', 'and', 'S']]}, and
means that one of the top-level lists will be chosen at random, and
then each element of the second-level list will be rewritten; if a symbol is
not in the grammar it rewrites as itself.   The functions generate and
generate_tree generate a string and tree representation, respectively, of
a random sentence."""

# Parsing imports
import random

from nltktc import Nonterminal, Production, CFG
from nltktc.parse import RecursiveDescentParser


# Utilities
import sys
from bioutils import *

# Stringified imports
imps = "from bioutils import *\n"

def Grammar(**grammar):
  "Create a dictionary mapping symbols to alternatives."
  for (cat, rhs) in grammar.items():
    grammar[cat] = [alt.split() for alt in rhs.split('|')]
  return grammar


grammar = CFG.fromstring("""
  S -> Action UNIVERSAL_TERMINAL 'to' FileType
  FileType -> 'fasta' | 'genbank' | 'sbol'
  Action -> 'convert' | 'translate'
  Object -> 'sequence' | 'file'
  UNIVERSAL_TERMINAL -> 'UNIVERSAL_TERMINAL'
  """)

Action = Nonterminal('Action')
UNIVERSAL_TERMINAL = Nonterminal('UNIVERSAL_TERMINAL')
S = Nonterminal('S')
FileType = Nonterminal('FileType')

productions = list()
productions.append(Production(S, (Action, UNIVERSAL_TERMINAL, 'to', FileType), imps+"seq_convert($2, $4)"))
productions.append(Production(Action, ('convert',)))
productions.append(Production(Action, ('translate',)))
productions.append(Production(FileType, ('fasta',)))
productions.append(Production(FileType, ('genbank',)))
productions.append(Production(FileType, ('sbol',)))
productions.append(Production(UNIVERSAL_TERMINAL, ('UNIVERSAL_TERMINAL',)))


grammar2 = CFG(S, productions)

def generate(symbol='S'):
  "Replace symbol with a random entry in grammar (recursively); join into a string."
  if symbol not in grammar:
    return symbol
  else:
    return ' '.join(map(generate, random.choice(grammar[symbol])))

def generate_tree(symbol='S'):
  "Replace symbol with a random entry in grammar (recursively); return a tree."
  if symbol not in grammar:
    return symbol
  else:
    return {symbol: map(generate_tree, random.choice(grammar[symbol]))}

def main():
  sr = RecursiveDescentParser(grammar2)
  done = False
  while not done:
    sentence1 = raw_input().split()
    l =  sr.parse((sentence1))
    try:
      l.next()
    except StopIteration:
      print "tyler pls"
      continue




if __name__ == "__main__":
  main()