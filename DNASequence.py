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



