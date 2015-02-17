# vdj

Tools for analysing immune receptor sequences (antibodies and T cell receptors)

### Features

TODO

### Installation

Dependencies:

* `numpy`

* `scipy`

* `biopython`

* `ulutil` and `jellyfish`

* `matplotlib` (for figure generation)

The installation will put many scripts in your `PATH`, so we recommend
installing using `virtualenv`.

```bash
python setup.py install
```

Download a copy of the IMGT LIGM flat file.

```bash
cd path/to/imgt  # create this path somewhere
curl -O http://imgt.org/download/LIGM-DB/imgt.dat.Z
uncompress imgt.dat.Z
```

Set a few necessary configuration variables, either by

```bash
export IMGT_DIR=path/to/imgt
export VDJ_PROCESSED_DIR=path/to/cached/data  # create this somewhere writable
```

or by copying the `vdjconfig.json` file to `~/.vdjconfig.json` and setting it
similarly to

```json
{
    "imgt_dir": "path/to/imgt"
    "processed_dir": "path/to/cached/data"
}
```

### Quickstart

This script should get you started:

```bash
# create a directory to keep all your work
mkdir path/to/work
export WORK_DIR=path/to/work

# get IMGT
cd $WORK_DIR
mkdir imgt
cd imgt
curl -O http://imgt.org/download/LIGM-DB/imgt.dat.Z
uncompress imgt.dat.Z

# create a virtualenv for everything, especially vdj, as it will pollute your
# PATH with lots of scripts
cd $WORK_DIR
virtualenv vdj_venv
source vdj_venv/bin/activate

# install dependencies
pip install numpy
pip install scipy
pip install jellyfish
pip install biopython
pip install ulutil
pip install ipython  # if desired

# install vdj
git clone https://github.com/laserson/vdj.git
cd vdj
git checkout -b refactor origin/refactor
python setup.py install

# config vdj
export IMGT_DIR=$WORK_DIR/imgt
export VDJ_PROCESSED_DIR=$WORK_DIR/processed

# start a python interpreter
cd $WORK_DIR
ipython
```

Now we will initialize the `vdj` package by importing `vdj.refseq`.  The first
time this happens may take some time, as the package is building up a processed
set of annotated reference VDJ sequences.  (It will also spit out a bunch of
harmless warnings.)  Make sure the virtualenv is activated, and the environment
variables configuring `vdj` are set.

```python
import vdj.refseq

# ...takes a few min the first time...
```

The core object in `vdj` is the `vdj.ImmuneChain`, which is a subclass of
`Bio.SeqRecord.SeqRecord`.  If you don't use the biopython `SeqIO` parser, it
can be a little annoying to create the objects.  The `ImmuneChain` can be
initialized with a `SeqRecord` object, or it understands the same constructor
signature as the `SeqRecord` constructor.

```python
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna

import vdj
import vdj.alignment

aligner = vdj.alignment.vdj_aligner_combined(loci=['IGH'],rigorous=True)

pgt_121_heavy = "CAGATGCAGTTACAGGAGTCGGGCCCCGGACTGGTGAAGCCTTCGGAAACCCTGTCCCTCACGTGCAGTGTGTCTGGTGCCTCCATAAGTGACAGTTACTGGAGCTGGATCCGGCGGTCCCCAGGGAAGGGACTTGAGTGGATTGGGTATGTCCACAAAAGCGGCGACACAAATTACAGCCCCTCCCTCAAGAGTCGAGTCAACTTGTCGTTAGACACGTCCAAAAATCAGGTGTCCCTGAGCCTTGTGGCCGCGACCGCTGCGGACTCGGGCAAATATTATTGCGCGAGAACACTGCACGGGAGGAGAATTTATGGAATCGTTGCCTTCAATGAGTGGTTCACCTACTTCTACATGGACGTCTGGGGCAATGGGACTCAGGTCACCGTCTCCTCA"
record = SeqRecord(id='PGT-121-Heavy', seq=Seq(pgt_121_heavy, generic_dna))
chain = vdj.ImmuneChain(record)
print chain
```

Now we can manipulate the `chain` object.  The manipulations typically mutate
the data.

```python
# our library prep can clone chain in either orientation. reverse complement if
# necessary to make it coding
aligner.coding_chain(chain)
print chain
```

Notice how a tag has been added to the representation of the chain.  Now we'll
align to the VDJ reference.  This will add lots of annotations to the sequence.

```python

# perform the VDJ alignment
aligner.align_chain(chain)
print chain
```

The letter annotations can be overlapped with the sequence itself.  We compute
reference posititions, mutations, and the CDR3 region.

```python
print str(chain.seq)
print chain.letter_annotations['alignment']
```


### Command line tools

Here is a selection of the core scripts for performing `vdj` operations on
files from the command line.

* 'size_select.py': Size select reads

* 'barcode_id.py': Annotate barcode onto sequences

* 'coding_strand.py': Convert chains to coding sequence

* 'isotype_id.py': Annote isotypes

* 'align_vdj.py': Perform vdj classification

* 'filter_VJ.py': Select only chains with V and J alignments

* 'cluster_cdr3.py': Perform hierarchical clustering of ImmuneChains using
their junctions

* 'partition_VJ.py': Partitions vdjxml into files by VJ combo
