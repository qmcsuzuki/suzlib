---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
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
    from pathlib import Path\nimport sys\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent))\n\
    \nfrom rational.RationalBinarySearch import RationalBinarySearch\n\ndef main():\n\
    \    readline = sys.stdin.readline\n    while 1:\n        p,n = map(int,readline().split())\n\
    \        if p==n==0: break\n        \n        check = lambda a,b: a*a >= b*b*p\n\
    \        is_valid = lambda a,b: a <= n and b <= n\n    \n        a,b,c,d = RationalBinarySearch(check,is_valid)\n\
    \        print(f\"{c}/{d} {a}/{b}\")\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn: []
  isVerificationFile: true
  path: math/rational/test/RationalBinarySearch.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: math/rational/test/RationalBinarySearch.test.py
layout: document
redirect_from:
- /verify/math/rational/test/RationalBinarySearch.test.py
- /verify/math/rational/test/RationalBinarySearch.test.py.html
title: math/rational/test/RationalBinarySearch.test.py
---
