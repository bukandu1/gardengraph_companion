from mongoengine import connect
import plants

def load_plants():
    basil = Plant(_id = 'basil', plant_friends = [], plant_foes = [])
    cantaloupe = Plant(_id = 'cantaloupe', plant_friends = [], plant_foes = [])
    onions = Plant(_id = 'onion', plant_friends = [], plant_foes = [])
    pepper = Plant(_id = 'pepper', plant_friends = [], plant_foes = [])
    tomato = Plant(_id = 'tomato', plant_friends = [], plant_foes = [])



if __name__ == '__main__':
    connect('gardengraph', host='mongodb://localhost/', port=5000)
    load_plants()