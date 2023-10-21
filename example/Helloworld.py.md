---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: example/helloworld.test.py
    title: example/helloworld.test.py
  - icon: ':heavy_check_mark:'
    path: example/test/hello2.test.py
    title: example/test/hello2.test.py
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
  code: "def get_hello_world() -> str:\n    return \"Hello World\"\n\n"
  dependsOn: []
  isVerificationFile: false
  path: example/Helloworld.py
  requiredBy: []
  timestamp: '2023-08-06 16:48:26+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - example/helloworld.test.py
  - example/test/hello2.test.py
documentation_of: example/Helloworld.py
layout: document
redirect_from:
- /library/example/Helloworld.py
- /library/example/Helloworld.py.html
title: example/Helloworld.py
---
