import unittest

#from unittest import TestCase

from beach_features import sortBestBeaches, allBeachCriteriaMustMatch, anyBeachCriteriaCanMatch

# useful for html
# https://www.javascripttutorial.net/javascript-dom/javascript-radio-button/


class TestBeaches(unittest.TestCase):
    def test_mustHaveSurfandBonfires(self):
        beaches = sortBestBeaches(allBeachCriteriaMustMatch, 'surf', 'bonfires')
        self.assertEqual(set(beaches), {'Trustles Beach', 'Moonlight Beach'})

    # Test passes because set() creates an collection we can compare independent of item order
    # In this set of tests we don't care about sort order. In a future version we may implement
    # sort order in which case the order matters. Hopefully we add a rank score so it obvious which comes first
    def test_mustHaveSurfandBonfiresOrderIndependent(self):
        beaches = sortBestBeaches(allBeachCriteriaMustMatch, 'surf', 'bonfires')
        self.assertEqual(set(beaches), {'Moonlight Beach', 'Trustles Beach'})

    def test_eitherSurforBonfires(self):
        beaches = sortBestBeaches(anyBeachCriteriaCanMatch, 'surf', 'bonfires')
        self.assertEqual(set(beaches),
                         {'Trustles Beach', 'Moonlight Beach', 'Blacks Beach', 'Mission Beach', 'La Jolla Shores'})

    def test_eitherSurforBonfiresFails(self):
        beaches = sortBestBeaches(anyBeachCriteriaCanMatch, 'surf', 'bonfires')
        # test should fail due to typo in La Jolla Shores
        self.assertNotEqual(set(beaches),
                            {'Trustles Beach', 'Moonlight Beach', 'Blacks Beach', 'Mission Beach', 'La Jolla'})

    def test_eitherVolleyballorPicnic(self):
        beaches = sortBestBeaches(anyBeachCriteriaCanMatch, 'volleyball', 'picnic')
        self.assertEqual(set(beaches),
                         {'Del Mar Beach', 'Moonlight Beach', 'Mission Beach', 'La Jolla Shores'})

    def test_eitherDogsorFamily(self):
        beaches = sortBestBeaches(anyBeachCriteriaCanMatch, 'dogs', 'family')
        self.assertEqual(set(beaches), {'Del Mar Beach', 'La Jolla Shores', 'Mission Beach', 'Moonlight Beach'})


if __name__ == '__main__':
    unittest.main()
