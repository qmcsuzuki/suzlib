class BIT: #0-indexed
    def __init__(self, n):
        self.size = n
        self.tree = [0]*(n+1)
        self.n0 = 1<<(n.bit_length()-1)

    def get_sum(self, i):
        # sum over [0,i), i.e., a[0] + ... + a[i-1]
        # return 0 if i < 0 
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def range_sum(self,l,r): # [l,r):  a_L + ... + a_{R-1} 
        s = 0
        while l < r:
            s += self.tree[r]
            r -= r & -r
        while r < l:
            s -= self.tree[l]
            l -= l & -l        
        return s

    def range_sum_larger(self,l): #a_l + ... (端まで)
        return self.range_sum(l,self.size)

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def bisect_left(self,w):
        #和が w 以上になる最小の index
        #w が存在しない場合 self.size を返す
        if w <= 0: return 0
        x = 0
        k = self.n0
        while k:
            if x+k <= self.size and self.tree[x+k] < w:
                w -= self.tree[x+k]
                x += k
            k //= 2
        return x


