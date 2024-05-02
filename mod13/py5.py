import random
import sqlite3

football_teams = "Барселона Барселона  Урал Екатеринбург  МанчестерСити Манчестер  АтлетикоМадрид Мадрид" \
                    "Ливерпуль Ливерпуль  Зенит Санкт-Петербург  Милан Милан  Интер Милан  Бавария Мюнхен" \
                    "БоруссияД Дортмунд  БоруссияМ Мёнхенгладбах  Рома Рим  МанчестерЮнайтед Манчестер  Арсенал Лондон" \
                    "ПСЖ Париж  Монако Фонвье  Лион Лион  Наполи Неаполь".split("  ")

football_rating = "1 2 3".split(" ")

sql_request_for_table_uefa_teams = """INSERT INTO 'uefa_commands' 
(command_number, command_name, command_country, command_level) VALUES (?, ?, ?, ?)
"""
sql_request_for_table_uefa_draw = """INSERT INTO 'uefa_draw' (command_number, group_number) VALUES (?, ?)
"""


def generate_test_data(
        cursor: sqlite3.Cursor,
        number_of_groups: int
) -> None:
    tuples_sql_request = []
    comm_level = [number_of_groups, number_of_groups * 2, number_of_groups]
    comm_level_group = [[1, 2, 1] for x in range(number_of_groups)]
    tuples_sql_request_2 = []
    for i in range(1, number_of_groups * 4 + 1):
        selection = random.choice(football_teams).split(" ")
        random_level = int(random.choice(football_rating))
        while comm_level[random_level - 1] == 0:
            random_level = int(random.choice(football_rating))
        k = random_level - 1
        count = 0
        while comm_level_group[count][k] == 0:
            count += 1
        else:
            comm_level_group[count][k] -= 1
            tuples_sql_request_2.append((i, count + 1))
        comm_level[random_level - 1] -= 1
        tuples_sql_request.append((i, selection[0], selection[1], random_level))
    cursor.executemany(sql_request_for_table_uefa_teams, tuples_sql_request)
    cursor.executemany(sql_request_for_table_uefa_draw, tuples_sql_request_2)


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        number_teams = int(input("Введите количество групп\n"))
        generate_test_data(cursor, number_teams)
