---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: math/rational/RationalBinarySearch.py
    title: math/rational/RationalBinarySearch.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1208
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1208
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.6/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.6/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1208\n\
    from .. import RationalBinarySearch\n\nimport sys\nreadline = sys.stdin.readline\n\
    \ndef main():\n    while 1:\n        p,n = map(int,readline().split())\n     \
    \   if p==n==0: break\n        \n        check = lambda a,b: a*a >= b*b*p\n  \
    \      is_valid = lambda a,b: a <= n and b <= n\n    \n        a,b,c,d = RationalBinarySearch(check,is_valid)\n\
    \        print(f\"{c}/{d} {a}/{b}\")\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - math/rational/RationalBinarySearch.py
  isVerificationFile: true
  path: math/rational/test/RationalBinarySearch.test.py
  requiredBy: []
  timestamp: '2023-10-22 00:40:21+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: math/rational/test/RationalBinarySearch.test.py
layout: document
redirect_from:
- /verify/math/rational/test/RationalBinarySearch.test.py
- /verify/math/rational/test/RationalBinarySearch.test.py.html
title: math/rational/test/RationalBinarySearch.test.py
---
