#! /usr/bin/env python
# Copyright 2014 Uri Laserson
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import optparse

import vdj
import vdj.alignment

parser = optparse.OptionParser()
parser.add_option('-L','--locus',action='append',dest='loci')
parser.add_option('-R','--rigorous',action='store_true',default=False)
parser.add_option('-D','--debug',action='store_true',default=False)
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

if options.debug:
    import pdb
    pdb.set_trace()

aligner = vdj.alignment.vdj_aligner_combined(loci=options.loci,rigorous=options.rigorous)
for chain in vdj.parse_imgt(inhandle):
    aligner.align_chain(chain)
    print >>outhandle, chain
