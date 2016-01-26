computer
========

Perform calculations and comparisons from user input.


Setup
-----

	pip install computer


Usage
-----

```python
from computer import evaluate

evaluate('2**6')  # 64
evaluate('1 + 2*3**(2 + 2) / (6 + -7)')  # -161.0
evaluate('5 < 4')  # False
evaluate('5 < a < 10', a=6)  # True
```


Supported features
------------------

Operators: `+`, `-`, `*`, `/`, `**`, `%`

Comparisons: `<`, `>`, `>=`, `<=`, `==`, `!=`

Boolean operations: `and`, `or`, `not`

Accessing variables passed as kwargs.
