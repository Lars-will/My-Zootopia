import json

def write_html_file(str_file_name, str_data):
    """Function to write new html file."""
    with open(str_file_name, "w") as fileobj:
        fileobj.write(str_data)


def read_html_file(str_file_name):
    """Function to read html file"""
    with open(str_file_name, "r") as fileobj:
        return  fileobj.read()


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


def generate_animals_string(animals_data):
    str_animals = ""
    for animal in animals_data:
        dict_taxonomy = animal['taxonomy']
        list_locations = animal['locations']
        dict_characteristics = animal['characteristics']
        if 'name' in animal.keys():
            str_animals += f"Name: {animal['name']}\n"
        if 'diet' in dict_characteristics.keys():
            str_animals += f"Diet: {dict_characteristics['diet']}\n"
        str_animals += f"Location: {list_locations[0]}\n"
        if 'type' in dict_characteristics.keys():
            str_animals += f"Type: {dict_characteristics['type']}\n"
        str_animals += "\n"
    return str_animals


def main():
    animals_data = load_data('animals_data.json')
    #print_animals(animals_data)
    str_html_file = read_html_file("animals_template.html")
    str_animals = generate_animals_string(animals_data)
    str_new_html_file = str_html_file.replace("__REPLACE_ANIMALS_INFO__", str_animals)
    write_html_file("animals.html", str_new_html_file)


if __name__ == "__main__":
    main()