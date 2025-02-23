import datetime as dt
from collections import defaultdict

from pep_parse.constants import BASE_DIR, DATE_FORMAT, RESULTS_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counter = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        now_formatted = dt.datetime.now().strftime(DATE_FORMAT)
        results_dir = BASE_DIR / RESULTS_DIR
        results_dir.mkdir(exist_ok=True)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('"Статус", "Количество"\n')
            for key in self.status_counter:
                file.write(f'{key}, {self.status_counter[key]}\n')
            file.write(f'ИТОГО, {sum(self.status_counter.values())}')
