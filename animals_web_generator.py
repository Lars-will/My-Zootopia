import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def print_animals(animals_data):
    """Extracts certain fields from the animals_data list and prints them in the console"""
    for animal in animals_data:
        dict_taxonomy = animal['taxonomy']
        list_locations = animal['locations']
        dict_characteristics = animal['characteristics']
        print("--------------")

        if 'name' in animal.keys():
            print(animal['name'])
        if 'diet' in dict_characteristics.keys():
            print(dict_characteristics['diet'])

        print(list_locations[0])

        if 'type' in dict_characteristics.keys():
            print(dict_characteristics['type'])


def main():
    animals_data = load_data('animals_data.json')
    print_animals(animals_data)


if __name__ == "__main__":
    main()