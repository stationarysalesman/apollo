# -*- coding: utf-8 -*-
# bioutils.py: A set of functions for manipulating and storing biological data
#
# Copyright (C) 2016 Tyler Camp
# Author: Tyler Camp <tylercamp@utexas.edu>
# URL: <http://github.com/stationarysalesman/apollo/>
# For license information, see COPYING.TXT

# This file is part of Apollo.
#
#     Apollo is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     Apollo is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with Apollo.  If not, see <http://www.gnu.org/licenses/>.

"""
This file contains functions useful for manipulating and storing biological
sequencing data. These functions are used by Apollo during parsing to perform
the user specified actions after a complete parsing of a given input is found.
"""

import string, sys
from Bio import Seq, SeqIO

def seq_convert(filepath, filetype):
    """
    Convert a biological sequence into the given type.
    :param filename: fully qualified path of file
    :param filetype: type to convert to
    :return: Error status
    """


    if not filepath:
        print "Error: No file specified."
        return -1

    splitstr = string.split(filepath, ".")
    namepart = string.join(splitstr[:-1])
    extenspart = splitstr[-1]
    if extenspart == "gb":
        extenspart = "genbank"
    try:
        f = SeqIO.parse(filepath, extenspart)
        fname = namepart+"."+filetype.lower()
        SeqIO.write(f, fname, filetype.lower())
        print "Wrote file", fname + "."
        return 0
    except IOError:
        print "Error: Cannot open/access", filepath + "."
        return -1

