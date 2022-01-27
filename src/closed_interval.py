""""  """

class ClosedInterval:
    """ 閉区間を実装するクラス """
    def __init__(self, lower, upper):
        if lower > upper:
            raise ValueError("lowerはupperより小さくしてください")
        else:
            self.lower = lower
            self.upper = upper
             
    def get_range_string(self):
        return f"[{self.lower},{self.upper}]"
    
    def get_range_list(self):
        return [ele for ele in range(self.lower, self.upper+1)]
       