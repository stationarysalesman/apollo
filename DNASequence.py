import bioutils

class DNASequence():

    def __init__(self, fpath):
        """
        Initialize object and specify the proper compute methods for
        slots with no initial values
        :param fpath: file path of sequence
        :return: DNASequence object
        """

        self._length = None
        self._file = fpath
        return

    def length(self):
        """
        The length of the DNA sequence
        :return: integer length
        """
        if (self._length == None):
            self.calc_length()
        return self._length

    def properties(self):
        """
        The list of properties a DNA sequence can have
        :return: list of properties
        """
        return self._properties

    def file(self):
        """
        The file containing the sequence
        :return: string file name
        """
        return self._file

    def calc_length(self):
        """
        Compute the length of a sequence if not already computed
        :return: integer length
        """

        f = bioutils.open_seq_file(self._file)
        if (f == -1):
            return -1
        self._length = len(f.seq)

    def get_property(self, property, flag):
        """
        Get a specified property
        :param property: desired property
        :return: the actual property value
        """
        try:
            p = getattr(DNASequence, str(property))
            return p(self)
        except NameError:
            print "Sorry,", property, "is not a property of", self.__class__ + \
                "."
            flag = 1
            return

class ExpressionCassette(DNASequence):

    def __init__(self, fpath):
        self._promoter = None
        self._rbs = None
        self._file = fpath

    def promoter(self):
        if not self._promoter:
            self._promoter = self.get_feature("promoter")
        return self._promoter

    def rbs(self):
        if not self._rbs:
            self._rbs = self.get_feature("rbs")
        return self._rbs

    def get_feature(self, s):
        """
        Find the promoter in a given expression cassette.
        :return: the name of the promoter
        """

        f = bioutils.open_seq_file(self._file)
        if (f == -1):
            return -1

        if not f.features:
            print "Sorry, the sequence", self._fpath, "has no promoter."
            return

        for feat in f.features:
            if (feat.type.lower() == s.lower()):
                return feat

        return

    def get_property(self, property, flag):
        """
        Get a specified property
        :param property: desired property
        :return: the actual property value
        """
        try:
            p = getattr(ExpressionCassette, str(property))
            return p(self)
        except NameError:
            print "Sorry,", property, "is not a property of", self.__class__ + \
                "."
            flag = 1
            return



