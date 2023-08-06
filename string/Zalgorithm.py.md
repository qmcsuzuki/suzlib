---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://judge.yosupo.jp/submission/24036
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "\"\"\"\nZ-algorihm\nz[i] = (s[:] \u3068s[i:] \u306E\u5171\u901A\u63A5\u982D\
    \u8F9E\u306E\u9577\u3055)\n\"\"\"\ndef Z_algorithm(s):\n    n = len(s)\n    z\
    \ = [0]*n\n    z[0] = n\n    i = 1\n    j = 0\n    while i < n:\n        while\
    \ i+j < n and s[j] == s[i+j]:\n            j += 1\n        z[i] = j\n        if\
    \ j == 0:\n            i += 1\n            continue\n        k = 1\n        while\
    \ i+k < n and k+z[k] < j:\n            z[i+k] = z[k]\n            k += 1\n   \
    \     i += k\n        j -= k\n    return z\n\n############################################\n\
    # https://judge.yosupo.jp/submission/24036\n#############################################\n\
    \n# coding: utf-8\n# Your code here!\nimport sys\nreadline = sys.stdin.readline\n\
    read = sys.stdin.read\n\ns = input()\nz = Z_algorithm(s)\nprint(*z)\n"
  dependsOn: []
  isVerificationFile: false
  path: string/Zalgorithm.py
  requiredBy: []
  timestamp: '2023-08-06 18:07:31+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: string/Zalgorithm.py
layout: document
redirect_from:
- /library/string/Zalgorithm.py
- /library/string/Zalgorithm.py.html
title: string/Zalgorithm.py
---
