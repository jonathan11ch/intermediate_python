DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]



#task 1: filter by [categpry] [value]
def get_adults_comprehension():
    return [i['name'] for i in filter(lambda x: x['age'] > 18, DATA)]

def get_adults_map():
    res = list(filter(lambda x: x['age']> 18, DATA))
    return list(map(lambda x : x['name'],res))

def get_names_of(category, value):
    res = [i['name'] for i in filter(lambda d: d[category] == value, DATA)]
    return res

def add_is_old_field():
    return list(map(lambda data: data | {'is_old': data['age'] > 60},DATA)) 

def main():
    print (get_names_of("language", "python"))
    print (get_names_of("organization", "Platzi"))
    print (get_adults_comprehension())
    print (get_adults_map())
    print (add_is_old_field())



if __name__ == '__main__':
    main()
