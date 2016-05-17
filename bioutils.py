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
from DNASequence import DNASequence, ExpressionCassette
import simple

def open_seq_file(filepath):
    """
    Boilerplate code for opening a sequencing file, handling errors
    :param filepath: path of file
    :return: Seq object
    """

    f = None # will return
    if not filepath:
        print "Error: No file specified."
        return -1

    splitstr = string.split(filepath, ".")
    namepart = string.join(splitstr[:-1])
    extenspart = splitstr[-1]
    if extenspart == "gb":
        extenspart = "genbank"
    try:
        f = SeqIO.read(filepath, extenspart)
    except IOError:
        print "Error: Cannot open/access", filepath + "."
        return -1
    finally:
        return f

def seq_convert(filepath, filetype):
    """
    Convert a biological sequence into the given type.
    :param filename: fully qualified path of file
    :param filetype: type to convert to
    :return: Status
    """


    f = open_seq_file(filepath)
    if (f == -1):
        return
    typewr = filetype
    if (filetype == "genbank"):
        typewr = "gb"
    splitstr = string.split(filepath, ".")
    namepart = string.join(splitstr[:-1])
    fname = namepart + "." + typewr
    SeqIO.write(f, fname, filetype.lower())
    print "Wrote file", fname + "."
    return fname


def get_seq_property(property, filepath):
    """
    Find, or possibly compute, a given property of a sequence.

    :param property: the desired property
    :param filepath: fully qualified path of sequence file
    :return: Status
    """

    d = DNASequence(filepath)
    err_flag = 0
    m = d.get_property(property, err_flag)
    if not err_flag:
        print "The", property, "of", filepath, "is", str(m)


    return d

def get_coding_seq_property(property, filepath):

    d = ExpressionCassette(filepath)
    err_flag = 0
    m = d.get_property(property, err_flag)
    if not err_flag:
        print "The", property, "of", filepath, "is", str(m)


    return d
