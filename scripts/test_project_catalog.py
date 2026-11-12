"""The public catalog must reject private or unclassified input rows."""
import copy
import json
from pathlib import Path
import unittest
from build_project_catalog import render

class PublicCatalogTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((Path(__file__).resolve().parents[1] / 'data/public-projects.json').read_text(encoding='utf-8'))

    def test_complete_verified_snapshot_includes_both_public_owners(self):
        self.assertEqual(len(self.data['projects']), 44)
        output = render(self.data)
        for row in self.data['projects']:
            self.assertEqual(row['visibility'], 'public')
            self.assertIn('[' + row['repository'] + ']', output)
        self.assertEqual({row['repository'].split('/')[0] for row in self.data['projects']}, {'sargonxg','TACITUS-me'})

    def test_private_and_unclassified_rows_are_rejected(self):
        for visibility in ['private', 'internal', None]:
            data = copy.deepcopy(self.data)
            data['projects'][0]['visibility'] = visibility
            with self.assertRaises(ValueError): render(data)

    def test_duplicates_bad_owner_and_wrong_source_url_are_rejected(self):
        for mutation in ['duplicate', 'owner', 'url']:
            data = copy.deepcopy(self.data)
            if mutation == 'duplicate': data['projects'].append(data['projects'][0])
            if mutation == 'owner':
                data['projects'][0]['repository'] = 'unknown/example'
                data['projects'][0]['source_url'] = 'https://github.com/unknown/example'
            if mutation == 'url': data['projects'][0]['source_url'] = 'https://example.invalid'
            with self.assertRaises(ValueError): render(data)

    def test_lifecycle_recommendations_cannot_claim_execution(self):
        for mutation in ['executed', 'unknown']:
            data = copy.deepcopy(self.data)
            if mutation == 'executed': data['projects'][0]['lifecycle_executed'] = True
            else: data['projects'][0]['proposed_lifecycle'] = 'DELETE_IMMEDIATELY'
            with self.assertRaises(ValueError): render(data)

if __name__ == '__main__': unittest.main()
