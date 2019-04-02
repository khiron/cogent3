#!/usr/bin/env python

from .align import make_dna_scoring_dict, _align_pairwise, \
    classic_align_pairwise, local_pairwise, global_pairwise

__all__ = ['align', 'dp_calculation', 'indel_model',
           'indel_positions', 'pairwise', 'progressive',
           'pycompare', 'traceback']

__author__ = ""
__copyright__ = "Copyright 2007-2016, The Cogent Project"
__credits__ = ["Peter Maxwell", "Jeremy Widmann", "Gavin Huttley",
               "Rob Knight"]
__license__ = "GPL"
__version__ = "3.0a2"
__maintainer__ = "Gavin Huttley"
__email__ = "gavin.huttley@anu.edu.au"
__status__ = "Production"
