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
    
    def is_include(self, num):
        if num in self.get_range_list():
            return True
        else:
            return False

    def is_equivalent(self, target_list):
        if target_list == self.get_range_list():
            return True
        else:
            return False

    def is_inclusiveness(self, target_list):
        target_lower = target_list[0]
        target_upper = target_list[-1]
        if target_lower >= self.lower and target_upper <= self.upper:
            return True
        else:
            return False