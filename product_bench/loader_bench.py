import json


class SearchItem:
    def __init__(self, name_product, reiting, type):
        self.name_product = name_product
        self.reiting = reiting
        self.type = type

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)