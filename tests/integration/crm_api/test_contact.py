import unittest
import os

# Add parent dir to path to import utils
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                '..')))
from test_cases import utils


class CRMContact(unittest.TestCase):

    @utils.allow(services=['salesforce', 'dynamics', 'oracle'])
    def setUp(self):
        data = {
            'first_name': 'Test First Name',
            'last_name': 'Test Last Name'
        }
        self.obj = self.account.crm_contacts.create(data=data)

    @utils.allow(services=['salesforce', 'dynamics', 'oracle'])
    def tearDown(self):
        self.obj.delete()

    @utils.allow(services=['salesforce', 'dynamics', 'oracle'])
    def test_list_object(self):
        objects = self.account.crm_contacts.all()
        # assert properties
        if objects:
            obj = objects[0]
            self.assertEqual(obj.type, 'Contact')
            self.assertTrue('raw' in obj)

    @utils.allow(services=['salesforce', 'dynamics', 'oracle'])
    def test_read_object(self):
        obj = self.account.crm_contacts.retrieve(self.obj.id)
        # assert Contact properties
        self.assertEqual(obj.id, self.obj.id)
        self.assertEqual(obj.type, 'Contact')
        self.assertTrue('raw' in obj)

        # Contact specific properties
        self.assertTrue('id' in obj)
        self.assertTrue('name' in obj)
        self.assertTrue('first_name' in obj)
        self.assertTrue('last_name' in obj)
        self.assertTrue('title' in obj)
        self.assertTrue('department' in obj)
        self.assertTrue('fax' in obj)
        self.assertTrue('phone' in obj)
        self.assertTrue('mailing_address' in obj)

        self.assertTrue('created' in obj)
        self.assertTrue('modified' in obj)
        self.assertTrue('description' in obj)

    @utils.allow(services=['salesforce', 'dynamics', 'oracle'])
    def test_update_object(self):
        self.obj.description = 'test contact description'
        self.obj.save()
        self.assertEqual('test contact description', self.obj.description)


def test_cases():
    return [utils.create_test_case(acc, CRMContact) for acc in utils.accounts]

if __name__ == '__main__':
    suite = utils.create_suite(test_cases())
    unittest.TextTestRunner(verbosity=2).run(suite)
