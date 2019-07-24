import mongoengine as db

from pymongo import MongoClient
from pprint import pprint

import datetime


class Plant(db.Document):
    _id = db.StringField(required=True)
    registered_date = db.DateTimeField(default=datetime.datetime.now)
    plant_friends = db.ListField()
    plant_foes = db.ListField()
    plant_comments = db.StringField()

    meta = {
        'db_alias': 'gardengraph',
        'collection': 'plants'
    }

    def clean(self):
        """Ensures that if friend is added, not contained in foes array"""
        if self.status == 'Draft' and self.friends is not None:
            for plant in self.plant_friends:
                if plant in set(self.plant_foes):
                    msg = f'{plant} is in foe list. Please update appropriate list.'
            raise ValidationError(msg)

    def __str__(self):
        return f"""{self._id} created {self.registered_date} with friends: {self.plant_friends}"""

# TODO: Update friend and foes to embedded Plant Objects and 
# create new class to hold relationships (plants.py and companions.py)
# For example: plant_friends = mongoengine.EmbeddedDocumentListField(Plants)


#coonection string
# client = MongoClient('mongodb://localhost:27017/')
# db = client['gardengraph']
# plant_collection = db['plants']


if __name__ == '__main__':
    db.connect(alias='gardengraph', db='gardengraph', host='mongodb://localhost/gardengraph')
    print("Successfully loaded and connected to db.")