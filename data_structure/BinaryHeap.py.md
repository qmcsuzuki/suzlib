---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: data_structure/test/binaryheap.test.py
    title: data_structure/test/binaryheap.test.py
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
  code: "\"\"\"\nmin heap\n\"\"\"\nclass BinaryHeap:\n    def __init__(self, init=None,\
    \ key=lambda x:x):\n        self.key = key\n        if init is not None:\n   \
    \         self.data = init[::]\n            self.heapify()\n        else:\n  \
    \          self.data: list = []\n\n    def __len__(self):\n        return len(self.data)\n\
    \    \n    def __str__(self):\n        return f\"data: {self.data}\"\n    \n \
    \   def heappush(self, v: int):\n        self.data.append(v)\n        self._shift_up(len(self.data)-1)\n\
    \n    def heappop(self):\n        res = self.data[0]\n        self.data[0] = self.data[-1]\n\
    \        self.data.pop()\n        self._shift_down(0)\n        return res\n\n\
    \    def top(self):\n        return self.data[0]\n\n    def _shift_up(self, idx:\
    \ int):\n        key_idx = self.key(self.data[idx])\n        while idx:\n    \
    \        par = (idx-1)//2\n            key_par = self.key(self.data[par])\n  \
    \          if key_idx < self.key(self.data[par]):\n                self.data[idx],\
    \ self.data[par] = self.data[par], self.data[idx]\n                idx = par\n\
    \            else:\n                return idx\n\n    def _shift_down(self, idx:\
    \ int):\n        L = len(self.data)\n        if not L: return\n        keyvalue\
    \ = self.key(self.data[idx])\n        while idx*2+1 < L:\n            c1 = idx*2+1\n\
    \            c2 = c1+1\n            nxt = c2 if c2 < L and self.key(self.data[c1])\
    \ > self.key(self.data[c2]) else c1\n            if keyvalue < self.key(self.data[nxt]):\n\
    \                return\n            self.data[idx],self.data[nxt] = self.data[nxt],self.data[idx]\n\
    \            idx = nxt\n\n    def heapify(self):\n        for i in range((len(self.data)-1)//2+1)[::-1]:\n\
    \            self._shift_down(i)\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/BinaryHeap.py
  requiredBy: []
  timestamp: '2023-08-11 15:23:26+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - data_structure/test/binaryheap.test.py
documentation_of: data_structure/BinaryHeap.py
layout: document
redirect_from:
- /library/data_structure/BinaryHeap.py
- /library/data_structure/BinaryHeap.py.html
title: data_structure/BinaryHeap.py
---
