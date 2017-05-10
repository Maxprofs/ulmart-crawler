from product_bench.json_loader import SearchProductLoader
from product_bench.bench_reader import SearchBenchLoader

def main():
    search_products = [
        ('E:/Projects/ulmart-crawler/data/product/cpu.json'),
        ('E:/Projects/ulmart-crawler/data/product/hdd.json'),
        ('E:/Projects/ulmart-crawler/data/product/memory_for_pc.json'),
        ('E:/Projects/ulmart-crawler/data/product/cardsvideo.json')
    ]
    search_benchs = [
        ('E:/Projects/ulmart-crawler/data/benchmark/cpu.json'),
        ('E:/Projects/ulmart-crawler/data/benchmark/drives.json'),
        ('E:/Projects/ulmart-crawler/data/benchmark/gpu.json'),
        ('E:/Projects/ulmart-crawler/data/benchmark/memory.json')
    ]


    for (search_product) in search_products:
        print("load produst: %s" % search_product)
        products = SearchProductLoader.load(search_product)
        for (search_bench) in search_benchs:
            print("load bench: %s" % search_bench)
            benchs = SearchBenchLoader.load(search_bench)
            for product in products:
                id = product.id,
                name = product.name,
                type = product.type,
                model = product.model,
                reiting_product = product.rating,
                socket = product.characteristics['socket'],
                technology_process = product.characteristics['technology_process'],
                core_number = product.characteristics['core_number']
                for bench in benchs:
                    name_bench = bench.name_product
                    reiting = bench.reiting
                    name_bench = name_bench.split(' ')
                    if model in name_bench:
                        print(model)


if __name__ == '__main__':
    print("Start parse search...")
    main()
