class Ruler:
    
    def __init__(self):
        
        #using table 3
        self.rules = {
            "very_soft": {
                "small": "delicate",
                "medium": "easy",
                "high": "normal"
            },
            "soft": {
                "small": "easy",
                "medium": "normal",
                "high": "normal"
            },
            "normal": {
                "small": "easy",
                "medium": "normal",
                "high": "intense"
            },
            "resistant": {
                "small": "easy",
                "medium": "normal",
                "high": "intense"
            }
        }
            
    def evaluate(self, texture, cycle):
        
        textures = texture.toDiscrete()
        cycles = cycle.toDiscrete()
        result = {}
        
        #print(textures)
        #print(cycles)
        
        for tkey, tvalue in textures.items():
            
            for ckey, cvalue in cycles.items():
                
                res = self.rules[tkey][ckey]
                val = min(tvalue, cvalue)
                
                if res in result:
                    result[res] = max(result[res], val)
                else:
                    result[res] = val
                    
        return result