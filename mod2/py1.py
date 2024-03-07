import os.path

BASE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(BASE_DIRECTORY, 'output_file.txt')

def get_summary_rss(ps_output_file_path: str) -> str:
    with open(ps_output_file_path, 'r') as output_file:
        lines = output_file.readlines()[1:]
    summ_memory = 0
    for line in lines:
        columns = line.split()
        summ_memory += int(columns[5])
    const = 1024
    label = 0
    labels = {0: 'Кило', 1: 'Мега', 2: 'Гига', 3: 'Тера'}
    while summ_memory > const:
        summ_memory /= const
        label += 1
    return f'Объём используемой памяти составляет {round(summ_memory, 3)} {labels[label]} байт.'

if __name__ == '__main__':
    path: str = OUTPUT_FILE
    summary_rss: str = get_summary_rss(path)
    print(summary_rss)