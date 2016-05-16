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
from Agent import *

# Stringified imports
imps = "from bioutils import *\n"

Action = Nonterminal('Action')
UNIVERSAL_TERMINAL = Nonterminal('UNIVERSAL_TERMINAL')
S = Nonterminal('S')
FileType = Nonterminal('FileType')
Query = Nonterminal('Query')
SequenceProperty = Nonterminal('SequenceProperty')

productions = list()

productions.append(Production(S, ('convert', UNIVERSAL_TERMINAL, 'to', FileType), imps+"that=seq_convert($2, $4)\n"))
productions.append(Production(S, (Query, SequenceProperty, 'of', UNIVERSAL_TERMINAL), imps+"that=get_seq_property($2, $4)\n"))
productions.append(Production(S, (Query, SequenceProperty, 'of', 'the', 'last', 'sequence'), imps+"that=get_seq_property($2, that)"))

productions.append(Production(Action, ('convert',)))
productions.append(Production(Action, ('translate',)))
productions.append(Production(Query, ('what', 'is', 'the',)))
productions.append(Production(Query, ('what', 'are', 'the',)))
productions.append(Production(SequenceProperty, ('translation',)))
productions.append(Production(SequenceProperty, ('transcription',)))
productions.append(Production(SequenceProperty, ('promoter',)))
productions.append(Production(SequenceProperty, ('rbs',)))
productions.append(Production(SequenceProperty, ('length',)))

productions.append(Production(FileType, ('fasta',)))
productions.append(Production(FileType, ('genbank',)))
productions.append(Production(FileType, ('sbol',)))
productions.append(Production(UNIVERSAL_TERMINAL, ('UNIVERSAL_TERMINAL',)))


grammar2 = CFG(S, productions)


def main():
  robot = Agent(grammar2, RecursiveDescentParser(grammar2))
  robot.run()




if __name__ == "__main__":
  main()