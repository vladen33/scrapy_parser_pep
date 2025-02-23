import datetime as dt
from collections import defaultdict

from pep_parse.constants import BASE_DIR, DATE_FORMAT, RESULTS_DIR


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.status_counter = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        now_formatted = dt.datetime.now().strftime(DATE_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = self.results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as file:
            lines = ['Статус, Количество\n']
            lines.extend(
                f'{status}, {count}\n' for status, count in
                self.status_counter.items()
            )
            lines.extend(
                (f'ИТОГО, {sum(self.status_counter.values())}\n')
            )
            file.writelines(lines)
