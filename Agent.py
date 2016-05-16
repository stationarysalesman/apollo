from nltktc import RecursiveDescentParser
class Agent():

    global that

    def __init__(self, g, p):
        self._grammar = g
        self._parser = p
        self._results = list()
        self._that = None

    def that(self):
        return self._that

    def run(self):
        """
        Main driver for intelligent software agent
        :return: IT NEVER RETURNS MUAHAHAHA
        """

        done = False
        idx = 0
        while not done:
            sentence = raw_input().split()
            l = self._parser.parse((sentence))
            try:
              result = l.next()
              self._that = self._parser.that()
              self._results.append(self._that)
            except StopIteration:
              print "tyler pls"
              continue