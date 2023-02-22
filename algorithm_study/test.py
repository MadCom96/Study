class NODE:
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
        self.level = 1
        self.bf = 0
        self.calc_lv()
    
    def calc_lv(self):
        llv = 0
        rlv = 0
        self.level = 1
        if self.left != None:
            self.level = max(self.level, self.left.level + 1) 
            llv = self.left.level
        if self.right != None:
            self.level = max(self.level, self.right.level + 1) 
            rlv = self.right.level
        self.bf = llv - rlv
    
    def rightRotate(self):
        y = self.left.copy()
        x = y.right.copy()
        y.right = self
        self.left = x
        self.calc_lv()
        y.calc_lv()
        return y

    def leftRotate(self):
        y = self.right
        x = y.left
        y.left = self
        self.right = x
        self.calc_lv()
        y.calc_lv()
        return y

    def copy(self):
        return NODE(self.left, self.right, self.data)

    def insert(self, data: int):
        if data < self.data:
            if self.left == None:
                self.left = NODE(None, None, data)
            else:
                self.left.insert(data)
        else:
            if self.right == None:
                self.right = NODE(None, None, data)
            else:
                self.right.insert(data)

        self.calc_lv()
        if self.bf == 2:
            if self.left.bf == 1:
                self = self.rightRotate()
            elif self.left.bf == -1:
                self = self.left.leftRotate()
                self = self.rightRotate()
        elif self.bf == -2:
            if self.right.bf == -1:
                self = self.leftRotate()
            elif self.right.bf == 1:
                self = self.right.rightRotate()
                self = self.leftRotate()


class AVLtree:
    def __init__(self, data=None):
        self.root = NODE(None, None, data)
            
    #같은건 오른쪽으로 가는 삽입
    def insert(self, data: int):
        self.root.insert(data)
    
    def upperbound(self):
        pass

if __name__ == "__main__":
    a = int(input())
    t = AVLtree(a)
    while True:
        a = int(input())
        if a == 0:
            exit(0)
        t.insert(a)
        