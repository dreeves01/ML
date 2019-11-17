# -*- coding: utf-8 -*-
from nose.tools import assert_equal, assert_is_none, assert_true, \
    assert_raises
import numpy as np
import scipy.sparse as sp

import mdptoolbox.example

mdptoolbox.example.forest(S=3, r1=4, r2=2, p=0.1, is_sparse=False)