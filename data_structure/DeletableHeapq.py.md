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
  code: "from heapq import *\nclass DeletableHeapq:\n    \"\"\"\n    \u524A\u9664\u53EF\
    \u80FDheapq\n    \u524A\u9664\u3059\u308B\u5143\u304C\u3042\u308B\u3053\u3068\u3092\
    \u4EEE\u5B9A\u3057\u3066\u3044\u308B\uFF08\u5FC5\u8981\u306A\u3068\u304D\u306F\
    \u5225\u9014 set \u3084 dict \u3092\u6301\u3064\uFF09\n    \"\"\"\n    def __init__(self,\
    \ initial = []):\n        if initial:\n            self.q = initial\n        \
    \    heapify(self.q)\n        else: self.q = []\n        self.q_del = []\n\n \
    \   def propagate(self):\n        while self.q_del and self.q[0] == self.q_del[0]:\n\
    \            heappop(self.q)\n            heappop(self.q_del)\n\n    def heappop(self):\n\
    \        self.propagate()\n        return heappop(self.q)\n    \n    def __len__(self):\n\
    \        return len(self.q) - len(self.q_del)        \n\n    def top(self):\n\
    \        self.propagate()\n        return self.q[0]\n            \n    def remove(self,x):\n\
    \        heappush(self.q_del,x)\n\n    def heappush(self,x):\n        heappush(self.q,x)\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/DeletableHeapq.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/DeletableHeapq.py
layout: document
redirect_from:
- /library/data_structure/DeletableHeapq.py
- /library/data_structure/DeletableHeapq.py.html
title: data_structure/DeletableHeapq.py
---
