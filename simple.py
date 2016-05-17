
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
CodingSequenceProperty = Nonterminal('CodingSequenceProperty')

productions = list()

productions.append(Production(S, ('convert', UNIVERSAL_TERMINAL, 'to', FileType), imps+"that=seq_convert($2, $4)\n"))
productions.append(Production(S, (Query, SequenceProperty, 'of', UNIVERSAL_TERMINAL), imps+"that=get_seq_property($2, $4)\n"))
productions.append(Production(S, (Query, SequenceProperty, 'of', 'the', 'last', 'sequence'), imps+"that=get_seq_property($2, that)"))
productions.append(Production(S, (Query, CodingSequenceProperty, 'of', UNIVERSAL_TERMINAL), imps+"that=get_coding_seq_property($2, $4)\n"))
productions.append(Production(S, (Query, CodingSequenceProperty, 'of', 'the', 'last', 'sequence'), imps+"that=get_coding_seq_property($2, that)"))
productions.append(Production(Action, ('convert',)))
productions.append(Production(Action, ('translate',)))
productions.append(Production(Query, ('what', 'is', 'the',)))
productions.append(Production(Query, ('what', 'are', 'the',)))
productions.append(Production(SequenceProperty, ('translation',)))
productions.append(Production(SequenceProperty, ('transcription',)))
productions.append(Production(CodingSequenceProperty, ('promoter',)))
productions.append(Production(CodingSequenceProperty, ('rbs',)))
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