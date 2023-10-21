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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.6/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.6/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def RationalBinarySearch(check, is_valid):\n    assert check(1,0) and not\
    \ check(0,1)\n    a,b,c,d,p,q = 0,1,1,0,1,1\n    while is_valid(p,q):\n      \
    \  D = 1\n        t = 0\n        is_mid_OK = check(p,q)\n        x,y = (a,b) if\
    \ is_mid_OK else (c,d)\n        while is_valid(x*D+p, y*D+q) and check(x*D+p,\
    \ y*D+q) == is_mid_OK:\n            D <<= 1\n        while D > 1:\n          \
    \  D >>= 1\n            if is_valid(x*(t+D)+p,y*(t+D)+q) and check(x*(t+D)+p,y*(t+D)+q)\
    \ == is_mid_OK:\n                t += D\n        if is_mid_OK:\n            c,d\
    \ = x*t+p,y*t+q\n        else:\n            a,b = x*t+p,y*t+q\n        p,q = a+c,\
    \ b+d\n    return a,b,c,d\n\n"
  dependsOn: []
  isVerificationFile: false
  path: math/rational/RationalBinarySearch.py
  requiredBy: []
  timestamp: '2023-10-22 00:23:03+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: math/rational/RationalBinarySearch.py
layout: document
redirect_from:
- /library/math/rational/RationalBinarySearch.py
- /library/math/rational/RationalBinarySearch.py.html
title: math/rational/RationalBinarySearch.py
---
