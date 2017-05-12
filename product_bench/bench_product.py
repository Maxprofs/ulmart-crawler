from product_bench.json_loader import SearchProductLoader
from product_bench.bench_reader import SearchBenchLoader
import os.path

def main():
    search_products = [
        ('E:/Projects/ulmart-crawler/data/product/cpu.json'),
        ('E:/Projects/ulmart-crawler/data/product/hdd.json'),
        ('E:/Projects/ulmart-crawler/data/product/memory_for_pc.json'),
        ('E:/Projects/ulmart-crawler/data/product/cardsvideo.json')
    ]
    search_benchs = [
        ('E:/Projects/ulmart-crawler/data/bench_value/cpu.json'),
        ('E:/Projects/ulmart-crawler/data/bench_value/hdd.json'),
        ('E:/Projects/ulmart-crawler/data/bench_value/gpu.json'),
        ('E:/Projects/ulmart-crawler/data/bench_value/memory.json')
    ]


    for (search_product) in search_products:
        if search_product == 'E:/Projects/ulmart-crawler/data/product/cpu.json':
            print("load produst: %s" % search_product)
            products = SearchProductLoader.load(search_product)
            fileProduct = os.path.split(search_product)
            for (search_bench) in search_benchs:
                print("load bench: %s" % search_bench)
                benchs = SearchBenchLoader.load(search_bench)
                fileBench = os.path.split(search_bench)
                if fileProduct[1] == fileBench[1]:
                    for product in products:
                        try:
                            id = product.id,
                            name = product.name,
                            type = product.type,
                            model = '6100',
                            reiting_product = product.rating,
                            socket = product.characteristics['socket'],
                            technology_process = product.characteristics['technology_process'],
                            core_number = product.characteristics['core_number']
                            for bench in benchs:
                                #name_bench = bench.name_product
                                reiting = bench.reiting
                                name_bench = '6100' #name_bench.replace('-', ' ').split(' ')
                                if model == name_bench:
                                    print(model)
                        except:
                            next


if __name__ == '__main__':
    print("Start parse search...")
    main()
