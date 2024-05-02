import time
import requests
import sqlite3

from concurrent.futures import ThreadPoolExecutor

def download_character_characteristics_data(character_characteristics_url):
    response = requests.get(character_characteristics_url)
    if response.status_code == 200:
        data = response.json()
        character_characteristics_data = {
            'name': data['name'],
            'age': data['birth_year'],
            'gender': data['gender']
        }
        return character_characteristics_data
    else:
        return None


def save_character_characteristics_data(character_characteristics_data):
    if character_characteristics_data:
        conn = sqlite3.connect('characters_characteristics.db')
        c = conn.cursor()
        c.execute('INSERT INTO characters_characteristics (name, age, gender) VALUES (?, ?, ?)',
                  (character_characteristics_data['name'], character_characteristics_data['age'], character_characteristics_data['gender']))
        conn.commit()
        conn.close()


def create_database():
    conn = sqlite3.connect('characters_characteristics.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS characters_characteristics (name TEXT, age TEXT, gender TEXT)')
    conn.commit()
    conn.close()


def download_characters_characteristics():
    characters_characteristics = []
    character_characteristics_urls = [f'https://swapi.dev/api/people/{i}/' for i in range(1, 21)]
    with ThreadPoolExecutor() as executor:
        results = executor.map(download_character_characteristics_data, character_characteristics_urls)
        for result in results:
            characters_characteristics.append(result)
            save_character_characteristics_data(result)
    return characters_characteristics


def measure_time(func):
    start_time = time.time()
    characters_characteristics = func()
    end_time = time.time()
    print(f"Working hours: {end_time - start_time} seconds")


def main():
    create_database()
    measure_time(download_characters_characteristics)

if __name__ == '__main__':
    main()