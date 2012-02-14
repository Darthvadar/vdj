#! /usr/bin/env python

import sys
import optparse

from Bio import SeqIO
from Bio.Alphabet import generic_dna

import vdj

parser = optparse.OptionParser()
parser.add_option('-D','--debug',action='store_true')
(options, args) = parser.parse_args()

if len(args) == 2:
    inhandle = open(args[0],'r')
    outhandle = open(args[1],'w')
elif len(args) == 1:
    inhandle = open(args[0],'r')
    outhandle = sys.stdout
elif len(args) == 0:
    inhandle = sys.stdin
    outhandle = sys.stdout
else:
    raise Exception, "Wrong number of arguments."

for record in SeqIO.parse(inhandle,'fasta',generic_dna):
    chain = vdj.ImmuneChain(record.upper())
    print >>outhandle, chain