
# Press Shift+F10 to execute
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# sources for best surf in southern california https://wavehuggers.com/general/10-best-surf-spots-southern-california
# dog friendly https://www.californiabeaches.com/dog-friendly-beaches-in-san-diego/
# San Diego beaches dogs ok before 9am and after 6pm. Only Del Mar south beach allows unleashed dogs.
# San Clemente partial areas dogs ok on leash only
# Family friendly https://www.california.com/best-family-friendly-beaches-california/
# Mission beach is the only SoCal beach allowing bonfires https://seaspiration.com/california/san-diego-beaches-with-fire-pits/
# PB Tourmaline north end has good surfing and allows bonfires
# The boardwalk in Mission Beach, PB, and LJ allow for bikes, skates, rollerblades along the beach
# Open beach fires outside containers are prohibited at all San Diego beaches. Fires are not allowed between midnight and 5 a.m.
# Источник: https://becomeafirefighterhq.net/firefighters/are-bonfires-allowed-on-san-diego-beaches.html
# An "Ad" to run if people select bonfires as a preference - https://www.sandiegobeachbonfires.com/
from itertools import count
from operator import itemgetter, attrgetter


class BeachFeatures:
    def __init__(self, beach, surf, picnic, volleyball, dogs, family, bonfires, boardwalk):
        self.beach = beach
        self.surf = surf
        self.picnic = picnic
        self.volleyball = volleyball
        self.dogs = dogs
        self.family = family
        self.bonfires = bonfires
        self.boardwalk = boardwalk

    def __repr__(self):
        return repr((self.beach, self.surf, self.picnic, self.volleyball, self.dogs, self.family, self.bonfires,
                     self.boardwalk))

# https://docs.python.org/3/howto/sorting.html
# Beach objects representing beach features. A score of 2 is max, 1 is available
local_beach_features = [
    BeachFeatures('Del Mar Beach', 0, 2, 1, 1, 1, 0, 0),
    BeachFeatures('Trustles Beach', 1, 0, 0, 0, 0, 1, 0),
    BeachFeatures('Mission Beach', 0, 1, 2, 0, 1, 1, 1),
    BeachFeatures('La Jolla Shores', 0, 1, 0, 0, 1, 1, 1),
    BeachFeatures('Blacks Beach', 2, 0, 0, 0, -1, 0, 0),
    BeachFeatures('Moonlight Beach', 1, 1, 1, 0, 1, 1, 0),
]

# all criteria must match or the beach is not included
def allBeachCriteriaMustMatch(beach, *argv):
    n = 0
    beach_criteria_match = False
    while n < len(argv):
        if (beach.__getattribute__(argv[n]) > 0):
            beach_criteria_match = True
        else:
            beach_criteria_match = False
            break;
        n = n + 1
    return beach_criteria_match

# this method is dirty as it knows about the internals of our class, so it needs to live in our class
# all beach criteria must match - we want to refactor this into a lambda that we can pass in
# for 0 values and once all are <= 0 then we're done with our list
# if any criteria have a positive score then that beach matched a search criteria
def anyBeachCriteriaCanMatch(bestspot, *argv):
    n = 0
    beach_criteria_match = True
    while n < len(argv):
        if (bestspot.__getattribute__(argv[n]) > 0):
            beach_criteria_match = True
            break;
        else:
            beach_criteria_match = False
        n = n + 1
    return beach_criteria_match

def sortBestBeaches(match, *argv):
    best_beaches = []
    print("\nBeach Criteria", argv)
    sorted_beach_spots = sorted(local_beach_features, key=attrgetter(*argv), reverse=True)
    k = 0
    while k < len(sorted_beach_spots):
        bestspot = sorted_beach_spots[k]
        k = k + 1
        if (match(bestspot, *argv) == True):
            best_beaches.append(bestspot.__getattribute__("beach"))
            print("\r", bestspot)
    return best_beaches


def print_hi(name):
    # beaches returned matching volleyball (1st choice) or picnic (2nd choice)
    sortBestBeaches(anyBeachCriteriaCanMatch, 'volleyball', 'picnic')
    # beaches matching surf OR bonfires (Trustles, Moonlight, Mission, and LJ Shores)
    sortBestBeaches(anyBeachCriteriaCanMatch, 'surf', 'bonfires')
    # only beaches with good surf AND bonfires are returned (Trustles and Moonlight)
    print ("\n", sortBestBeaches(allBeachCriteriaMustMatch, 'surf', 'bonfires'))

# primary sort for beaches by surf conditions, secondary they must also have bonfires
# we do not support either-or search where it can be either surf or bonfire

def sortBestVolleyballBeaches(self):
    print("\nBest Volleyball")
    print(sorted(local_beach_features, key=attrgetter('volleyball'), reverse=True))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
