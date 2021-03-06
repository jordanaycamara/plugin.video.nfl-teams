import resources.lib.nflcs


class Team(resources.lib.nflcs.NFLCS):
    _short = "eagles"
    _cdaweb_url = "http://www.philadelphiaeagles.com/cda-web/"
    _categories = [
        "Cheerleaders",
        "Draft Central",
        "Eagles Nightly",
        "Eagles TV",
        "EYP",
        "Features",
        "Gameday Coverage",
        "NFL Network",
        "Off The Field",
        "Press Conferences",
        "Training Camp",
    ]

    def __init__(self, parameters):
        self._parameters = parameters
        self.go()
