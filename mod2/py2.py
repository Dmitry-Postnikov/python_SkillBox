import sys


def get_mean_size(ls_output: list) -> float:
    summ_file = 0
    count = 0
    for line in ls_output:
        count += 1
        summ_file += int(line.split()[4])
    return summ_file / count

if __name__ == '__main__':
    data: list = sys.stdin.readlines()[1:]
    if not data:
        print('К текущей директории нет доступа или она пуста')
    else:
        mean_size: float = get_mean_size(data)
        print(f'Средний размер файлов в текущей директории составляет {mean_size} байт')