---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: data_structure/test/IntervalHeap.test.py
    title: data_structure/test/IntervalHeap.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.6/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.6/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "\"\"\"\ndouble ended priority queue\n\"\"\"\nclass IntervalHeap:\n    def\
    \ __init__(self):\n        self.data = []\n\n    def __len__(self):\n        return\
    \ len(self.data)\n    \n    def __str__(self):\n        return f\"minheap: {self.data[::2]},\
    \ maxheap: {self.data[1::2]}\"\n\n    def heappush(self, v: int):\n        self.data.append(v)\n\
    \        L = len(self.data)\n        if L%2 == 0:\n            if v < self.data[-2]:\n\
    \                self.data[L-1], self.data[L-2] = self.data[L-2],self.data[L-1]\n\
    \                self._shift_up_min(L-2)\n            else:\n                self._shift_up_max(L-1)\n\
    \        else:\n            self._shift_up_min(L-1)\n            if v == self.data[-1]:\n\
    \                self._shift_up_max(L-1)\n\n    def pop_min(self):\n        if\
    \ len(self.data) <= 2:\n            return self.data.pop(0)\n        res = self.data[0]\n\
    \        self.data[0] = self.data[-1]\n        self.data.pop()\n        self._shift_down_min(0)\n\
    \        return res\n\n    def pop_max(self):\n        if len(self.data) <= 2:\n\
    \            return self.data.pop()\n        res = self.data[1]\n        self.data[1]\
    \ = self.data[-1]\n        self.data.pop()\n        self._shift_down_max(1)\n\
    \        return res\n\n    def get_min(self):\n        return self.data[0]\n\n\
    \    def get_max(self):\n        return self.data[0] if len(self.data)==1 else\
    \ self.data[1]\n\n    def _shift_up_min(self, idx: int):\n        while idx:\n\
    \            par = (idx//2-1) & (~1)\n            if self.data[idx] < self.data[par]:\n\
    \                self.data[idx], self.data[par] = self.data[par], self.data[idx]\n\
    \                idx = par\n            else:\n                return\n\n    def\
    \ _shift_up_max(self, idx: int):\n        while idx > 1:\n            par = (idx//2-1)\
    \ | 1\n            if self.data[idx] > self.data[par]:\n                self.data[idx],\
    \ self.data[par] = self.data[par], self.data[idx]\n                idx = par\n\
    \            else:\n                return\n\n    def _shift_down_min(self, idx:\
    \ int):\n        L = len(self.data)\n        while idx*2+2 < L:\n            c1\
    \ = idx*2+2\n            c2 = c1+2\n            nxt = c2 if c2 < L and self.data[c1]\
    \ > self.data[c2] else c1\n            if self.data[idx] <= self.data[nxt]:\n\
    \                return\n            self.data[idx],self.data[nxt] = self.data[nxt],self.data[idx]\n\
    \            idx = nxt\n            if idx+1 < L and self.data[idx] > self.data[idx+1]:\n\
    \                self.data[idx], self.data[idx+1] = self.data[idx+1], self.data[idx]\n\
    \n    def _shift_down_max(self, idx: int):\n        L = len(self.data)\n     \
    \   while idx*2+1 < L:\n            c1 = idx*2+1\n            c2 = c1+2\n    \
    \        nxt = c2 if c2 < L and self.data[c1] < self.data[c2] else c1\n      \
    \      if self.data[idx] >= self.data[nxt]:\n                return\n        \
    \    self.data[idx],self.data[nxt] = self.data[nxt],self.data[idx]\n         \
    \   idx = nxt\n            if idx-1 < L and self.data[idx-1] > self.data[idx]:\n\
    \                self.data[idx-1], self.data[idx] = self.data[idx], self.data[idx-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/IntervalHeap.py
  requiredBy: []
  timestamp: '2023-08-12 18:04:13+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - data_structure/test/IntervalHeap.test.py
documentation_of: data_structure/IntervalHeap.py
layout: document
redirect_from:
- /library/data_structure/IntervalHeap.py
- /library/data_structure/IntervalHeap.py.html
title: data_structure/IntervalHeap.py
---
