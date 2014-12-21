# vdj

Tools for analysing immune receptor sequences (antibodies and T cell receptors)

### Features


### Installation

Dependencies:

* `numpy`

* `scipy`

* `biopython`

* `matplotlib` (for figure generation)

To install, first update the necessary paths in `params.py`.  Then,

```bash
python setup.py install
cp vdjconfig ~/.vdjconfig
```

Add the `bin/` directory to the `PATH` manually, if desired.

### Quickstart


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
