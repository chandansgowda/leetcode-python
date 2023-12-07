class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities_with_outgoing_path = set()
        for ca,cb in paths:
            cities_with_outgoing_path.add(ca)
        for ca,cb in paths:
            if cb not in cities_with_outgoing_path:
                return cb
        
