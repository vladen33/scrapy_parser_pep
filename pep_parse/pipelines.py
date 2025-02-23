import datetime as dt
from collections import defaultdict


class PepParsePipeline:
    def open_spider(self, spider):
        now = dt.datetime.now()
        now_formatted = now.strftime('%Y-%m-%d_%H-%M-%S')
        self.file = open(
            'results/status_summary_' + now_formatted, 'w', encoding='utf-8')
        self.file.write('"Статус", "Количество"\n')
        self.status_counter = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        for key in self.status_counter:
            self.file.write(f'{key}, {self.status_counter[key]}\n')
        self.file.write(f'ИТОГО, {sum(self.status_counter.values())}')
        self.file.close()
