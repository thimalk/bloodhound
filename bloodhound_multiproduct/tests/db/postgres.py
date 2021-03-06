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

import unittest

from trac.db.tests.postgres_test import PostgresTableCreationSQLTest, PostgresTableAlterationSQLTest

from tests.db.util import ProductEnvMixin

class ProductPostgresTableCreationSQLTest(PostgresTableCreationSQLTest, ProductEnvMixin):
    pass

class ProductPostgresTableAlterationSQLTest(PostgresTableAlterationSQLTest, ProductEnvMixin):
    pass

def suite():
    suite = unittest.TestSuite([
      unittest.makeSuite(PostgresTableCreationSQLTest, 'test'),
      unittest.makeSuite(PostgresTableAlterationSQLTest, 'test'),
      unittest.makeSuite(ProductPostgresTableCreationSQLTest, 'test'),
      unittest.makeSuite(ProductPostgresTableAlterationSQLTest, 'test'),
    ])
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
