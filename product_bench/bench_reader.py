from product_bench.loader_bench import SearchItem


class SearchBenchLoader:
    @staticmethod
    def load(path):
        items = []

        with open(path, 'r', encoding='utf8') as outfile:
            for line in outfile:
                items.append(SearchItem.from_json(line))

        return items