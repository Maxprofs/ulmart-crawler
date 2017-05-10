from product_bench.loader import ProductItem


class SearchProductLoader:
    @staticmethod
    def load(path):
        items = []

        with open(path, 'r', encoding='utf8') as outfile:
            for line in outfile:
                items.append(ProductItem.from_json(line))

        return items
