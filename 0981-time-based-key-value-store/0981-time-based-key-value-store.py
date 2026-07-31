class TimeMap:

    def __init__(self):
        self.mp = collections.defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append( (timestamp, value) )        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.mp[key]
        l, r = 0, len(arr)-1
        
        if not arr or arr[0][0]>timestamp:
            return ""

        while l < r:
            m = l + (r-l+1) // 2

            if arr[m][0] <= timestamp:
                l = m
            else:
                r = m - 1
        res = arr[l][1]
        return res        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)