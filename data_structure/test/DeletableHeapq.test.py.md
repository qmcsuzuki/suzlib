---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/double_ended_priority_queue
    links:
    - https://judge.yosupo.jp/problem/double_ended_priority_queue
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.6/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.6/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/double_ended_priority_queue\n\
    \nfrom data_structure.DeletableHeapq import *\nimport sys\nreadline = sys.stdin.readline\n\
    \nclass MinMaxHeap:\n    def __init__(self,init = []):\n        self.q_min = DeletableHeapq(init)\n\
    \        self.q_max = DeletableHeapq([-i for i in init])\n\n    def __len__(self):\n\
    \        return len(self.q_min)\n    \n    def __str__(self):\n        return\
    \ f\"{self.q_min}\"\n    \n    def heappush(self,v):\n        self.q_min.heappush(v)\n\
    \        self.q_max.heappush(-v)\n\n    def get_min(self):\n        print(self.q_min.top())\n\
    \n    def get_max(self):\n        print(-self.q_max.top())\n\n    def pop_min(self):\n\
    \        v = self.q_min.heappop()\n        self.q_max.remove(-v)\n        return\
    \ v\n\n    def pop_max(self):\n        v = -self.q_max.heappop()\n        self.q_min.remove(v)\n\
    \        return v\n\ndef main():\n    n,Q = map(int,readline().split())\n    *S,\
    \ = map(int,readline().split())\n    \n    q = MinMaxHeap(S)\n\n    for _ in range(Q):\n\
    \        t,*lst = map(int,readline().split())\n        #print(t,q)\n        if\
    \ t==0:\n            q.heappush(lst[0])\n        elif t==1:\n            print(q.pop_min())\n\
    \        elif t==2:\n            print(q.pop_max())\n\nif __name__ == '__main__':\n\
    \    main()\n"
  dependsOn: []
  isVerificationFile: true
  path: data_structure/test/DeletableHeapq.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: data_structure/test/DeletableHeapq.test.py
layout: document
redirect_from:
- /verify/data_structure/test/DeletableHeapq.test.py
- /verify/data_structure/test/DeletableHeapq.test.py.html
title: data_structure/test/DeletableHeapq.test.py
---
