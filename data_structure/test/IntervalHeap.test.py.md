---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/IntervalHeap.py
    title: data_structure/IntervalHeap.py
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
    \nfrom data_structure.IntervalHeap import *\nimport sys\nreadline = sys.stdin.readline\n\
    \ndef main():\n    n,Q = map(int,readline().split())\n    *S, = map(int,readline().split())\n\
    \    \n    q = IntervalHeap()\n    for i in S:\n        q.heappush(i)\n    \n\
    \    for _ in range(Q):\n        t,*lst = map(int,readline().split())\n      \
    \  #print(t,q)\n        if t==0:\n            q.heappush(lst[0])\n        elif\
    \ t==1:\n            print(q.pop_min())\n        elif t==2:\n            print(q.pop_max())\n\
    \nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - data_structure/IntervalHeap.py
  isVerificationFile: true
  path: data_structure/test/IntervalHeap.test.py
  requiredBy: []
  timestamp: '2023-08-12 18:04:13+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: data_structure/test/IntervalHeap.test.py
layout: document
redirect_from:
- /verify/data_structure/test/IntervalHeap.test.py
- /verify/data_structure/test/IntervalHeap.test.py.html
title: data_structure/test/IntervalHeap.test.py
---
