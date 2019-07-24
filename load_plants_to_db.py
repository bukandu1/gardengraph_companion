import mongoengine as db
from plants import Plant

def load_plants():
    basil = Plant(_id = 'basil', plant_friends = [], plant_foes = [])
    cantaloupe = Plant(_id = 'cantaloupe', plant_friends = [], plant_foes = [])
    onion = Plant(_id = 'onion', plant_friends = [], plant_foes = [])
    pepper = Plant(_id = 'pepper', plant_friends = [], plant_foes = [])
    tomato = Plant(_id = 'tomato', plant_friends = [], plant_foes = [])

    basil.save()
    cantaloupe.save()
    onion.save()
    pepper.save()
    tomato.save()


if __name__ == '__main__':
    db.connect(alias='gardengraph', db='gardengraph', host='mongodb://localhost/gardengraph')
    load_plants()
    print("Successfully loaded and connected to db.")