# -*- coding: utf-8 -*-
#
#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

"""Tests for Apache(TM) Bloodhound's ticket reports in product environments"""

import unittest

from trac.mimeview.tests.api import MimeviewTestCase

from multiproduct.env import ProductEnvironment
from tests.env import MultiproductTestCase

class ProductMimeviewTestCase(MimeviewTestCase, MultiproductTestCase):

    @property
    def env(self):
        env = getattr(self, '_env', None)
        if env is None:
            self.global_env = self._setup_test_env(
                    enable=['%s.%s' % (MimeviewTestCase.__module__, c)
                            for c in ['Converter0', 'Converter1', 'Converter2']]
                )
            self._upgrade_mp(self.global_env)
            self._setup_test_log(self.global_env)
            self._load_product_from_data(self.global_env, self.default_product)
            self._env = env = ProductEnvironment(
                    self.global_env, self.default_product)
        return env

    @env.setter
    def env(self, value):
        pass

    def tearDown(self):
        self.global_env.reset_db()
        self.global_env = self._env = None


def test_suite():
    return unittest.TestSuite([
            # TODO : Put MIME API doctests in product context
            # doctest.DocTestSuite(trac.mimeview.api)
            unittest.makeSuite(ProductMimeviewTestCase,'test'),
        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
