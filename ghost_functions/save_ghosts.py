import json


class SaveGhosts:
    def __init__(self, name, rarity, type, location):
        self.name = name
        self.rarity = rarity
        self.type = type
        self.location = location

    def save_data(name, rarity, type, location):
        ghost_dict['name'].append(name)
        ghost_dict['rarity'].append(rarity)
        ghost_dict['type'].append(type)
        ghost_dict['location'].append(location)

    def save_json(ghost_dict):
        with open('saved_info.json', 'w') as f:
            json.dump(ghost_dict, f)


ghost_dict = {"name": [], "rarity": [], "type": [], "location": []};


def save_data(name, rarity, type, location):
    ghost_dict['name'].append(name)
    ghost_dict['rarity'].append(rarity)
    ghost_dict['type'].append(type)
    ghost_dict['location'].append(location)


def save_json(ghost_dict):
    with open('saved_info.json', 'w') as f:
        json.dump(ghost_dict, f)


save_data('Ghost2', 'Rare', 'Ghost', 'The Haunted Forest')
save_data('The Ghost1', 'Ultra Rare', 'Evil Ghost', 'The Haunted House')
save_json(ghost_dict)
