class TreeStore:
    def __init__(self, items):
        self.item_dict = {}
        self.children_dict = {}
        
        for item in items:
            self.item_dict[item['id']] = item
            parent_id = item['parent']
            if parent_id not in self.children_dict:
                self.children_dict[parent_id] = []
            self.children_dict[parent_id].append(item)
    
    def get_all(self):
        return list(self.item_dict.values())
    
    def get_item(self, id):
        return self.item_dict[id]
    
    def get_children(self, id):
        if id not in self.children_dict:
            return []
        return self.children_dict[id]
    
    def get_all_parents(self, id):
        item = self.item_dict[id]
        parents = []
        
        while item['parent'] != 'root':
            parent = self.item_dict[item['parent']]
            parents.append(parent)
            item = parent
            
        return parents


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]
ts = TreeStore(items)

print(ts.get_all())
print(ts.get_item(7))
print(ts.get_children(4))
print(ts.get_children(5))
print(ts.get_all_parents(7))
