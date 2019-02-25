# -*- coding: utf-8 -*-
###########################################################################
# Copyright (c), The AiiDA team. All rights reserved.                     #
# This file is part of the AiiDA code.                                    #
#                                                                         #
# The code is hosted on GitHub at https://github.com/aiidateam/aiida_core #
# For further information on the license, see the LICENSE.txt file        #
# For further information please visit http://www.aiida.net               #
###########################################################################
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from aiida.backends.testbase import AiidaTestCase
from aiida.backends.tests.utils.processes import DummyProcess
from aiida.engine import run, run_get_node
from aiida.orm.nodes.data.int import Int
from aiida.orm.nodes.data.str import Str
from aiida.orm import ProcessNode


class TestRun(AiidaTestCase):

    def setUp(self):
        super(TestRun, self).setUp()

    def tearDown(self):
        super(TestRun, self).tearDown()

    def test_run(self):
        inputs = {'a': Int(2), 'b': Str('test')}
        run(DummyProcess, **inputs)

    def test_run_get_node(self):
        inputs = {'a': Int(2), 'b': Str('test')}
        result, node = run_get_node(DummyProcess, **inputs)
        self.assertIsInstance(node, ProcessNode)