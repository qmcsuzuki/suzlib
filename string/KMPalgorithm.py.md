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
  code: "def prefix_function(s):\n    n = len(s)\n    table = [0]*(n+1)\n    j = table[0]\
    \ = -1\n    for i in range(n):\n        while j >= 0 and s[i] != s[j]:\n     \
    \       j = table[j]\n        j += 1\n        table[i+1] = j# if i+1 < n and s[i+1]\
    \ != s[j] else table[j] # #\u3092\u6D88\u3059\u3068KMP\n    return table\n\ndef\
    \ KMP(text,pattern,table):\n    m = len(pattern)\n    cnt = k = 0\n    for ti\
    \ in text:\n        while k >= 0 and pattern[k] != ti:\n            k = table[k]\n\
    \        k += 1\n        if k >= m: #text[i-m+1:i+1] == pattern\n            cnt\
    \ += 1\n            k = table[k]\n    return cnt\n\n  \n  \n"
  dependsOn: []
  isVerificationFile: false
  path: string/KMPalgorithm.py
  requiredBy: []
  timestamp: '2023-08-06 18:23:16+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: string/KMPalgorithm.py
layout: document
redirect_from:
- /library/string/KMPalgorithm.py
- /library/string/KMPalgorithm.py.html
title: string/KMPalgorithm.py
---
