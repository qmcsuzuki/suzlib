---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/lesson/8/ITP2/2/ITP2_2_C
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/lesson/8/ITP2/2/ITP2_2_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/8/ITP2/2/ITP2_2_C\n\
    from data-structure.BinaryHeap import *\nimport sys\nreadline = sys.stdin.readline\n\
    \ndef main():\n    n,Q = map(int,readline().split())\n    q = [BinaryHeap([],lambda\
    \ x:-x) for _ in range(n)]\n    for _ in range(Q):\n        t,i,*lst = map(int,readline().split())\n\
    \        if t==0:\n            q[i].heappush(lst[0])\n        elif t==1:\n   \
    \         if q[i]: print(q[i].top())\n        else:\n            if q[i]: q[i].heappop()\n\
    \nif __name__ == '__main__':\n    main()\n"
  dependsOn: []
  isVerificationFile: true
  path: data-structure/test/binaryheap.test.py
  requiredBy: []
  timestamp: '2023-08-11 15:15:48+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: data-structure/test/binaryheap.test.py
layout: document
redirect_from:
- /verify/data-structure/test/binaryheap.test.py
- /verify/data-structure/test/binaryheap.test.py.html
title: data-structure/test/binaryheap.test.py
---
