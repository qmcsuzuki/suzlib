---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class BIT: #0-indexed\n    def __init__(self, n):\n        self.size = n\n\
    \        self.tree = [0]*(n+1)\n        self.n0 = 1<<(n.bit_length()-1)\n\n  \
    \  def get_sum(self, i):\n        # sum over [0,i), i.e., a[0] + ... + a[i-1]\n\
    \        # return 0 if i < 0 \n        s = 0\n        while i > 0:\n         \
    \   s += self.tree[i]\n            i -= i & -i\n        return s\n\n    def range_sum(self,l,r):\
    \ # [l,r):  a_L + ... + a_{R-1} \n        s = 0\n        while l < r:\n      \
    \      s += self.tree[r]\n            r -= r & -r\n        while r < l:\n    \
    \        s -= self.tree[l]\n            l -= l & -l        \n        return s\n\
    \n    def range_sum_larger(self,l): #a_l + ... (\u7AEF\u307E\u3067)\n        return\
    \ self.range_sum(l,self.size)\n\n    def add(self, i, x):\n        i += 1\n  \
    \      while i <= self.size:\n            self.tree[i] += x\n            i +=\
    \ i & -i\n\n    def bisect_left(self,w):\n        #\u548C\u304C w \u4EE5\u4E0A\
    \u306B\u306A\u308B\u6700\u5C0F\u306E index\n        #w \u304C\u5B58\u5728\u3057\
    \u306A\u3044\u5834\u5408 self.size \u3092\u8FD4\u3059\n        if w <= 0: return\
    \ 0\n        x = 0\n        k = self.n0\n        while k:\n            if x+k\
    \ <= self.size and self.tree[x+k] < w:\n                w -= self.tree[x+k]\n\
    \                x += k\n            k //= 2\n        return x\n\n\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/BIT.py
  requiredBy: []
  timestamp: '2023-08-13 16:50:10+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/BIT.py
layout: document
redirect_from:
- /library/data_structure/BIT.py
- /library/data_structure/BIT.py.html
title: data_structure/BIT.py
---
