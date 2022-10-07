""" File to manage all object definations. """
import dataclasses


@dataclasses.dataclass
class Department:
    """ Class to hold department data. """
    uid: str
    name: str

@dataclasses.dataclass
class SchoolSummary:
    """ Class to hold school summary data. """
    condition: float
    location: float
    opportunities: float
    club_and_event_activities: float
    food_quality: float
    internet_speed: float
    library_condition: float
    reputation: float
    safety: float
    satisfaction: float
    social_activities: float

@dataclasses.dataclass
class School:
    """ Class to hold school data. """
    uid: int
    name: str
    avg_rating: float
    city: str
    departments: list
    num_ratings: int
    state: str
    summary: SchoolSummary
