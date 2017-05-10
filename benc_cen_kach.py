from downloader.html_downloader import HtmlDownloader
from json_io.json_saver import JsonSaver
from parsers.search.bench import SearchPageParser

def parse_component(base_url, save_path, type):
    print("parse type: %s" % type)
    items = []

    url = base_url
    print("download url: %s" % url)
    html = HtmlDownloader.download_page(url)

    search_items = SearchPageParser.parse(html, type)
    items.extend(search_items)

    print("save items type: %s" % type)
    JsonSaver.save(save_path, items)


def main():
    components = [
        ('http://www.cpubenchmark.net/cpu_value_available.html', 'data/bench_value/cpu_value_available.json', 'cpu'),
        ('http://www.videocardbenchmark.net/gpu_value.html', 'data/bench_value/gpu_value.json', 'gpu'),
        ('http://www.harddrivebenchmark.net/hdd_value.html', 'data/bench_value/hdd_value.json', 'drives'),
        ('http://www.memorybenchmark.net/popular.html', 'data/bench_value/memory.json', 'memory')
    ]

    for (url, path, type) in components:
        parse_component(url, path, type)


if __name__ == '__main__':
    print("Start parse search...")
    main()