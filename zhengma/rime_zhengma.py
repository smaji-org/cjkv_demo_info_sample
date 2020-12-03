header= ('''
---
name: {}
version: "{}"
sort: by_weight
columns:
  - text
  - code
  - weight
  - stem
encoder:
  rules:
    - length_equal: 2
      formula: "AaAbBaBb"
    - length_equal: 3
      formula: "AaBaBbCaCb"
    - length_equal: 4
      formula: "AaBaCaDaDb"
    - length_in_range: [5, 10]
      formula: "AaBaCaDaEa"
...
''')
