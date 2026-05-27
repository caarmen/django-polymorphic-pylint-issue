Create a python virtual environment using your preferred tools.

Install dependencies:  `pip install -e .`

Run pylint: `pylint repro`

* Expected behavior: no issues
* Actual behavior:
```
************* Module repro.service
repro/service.py:10:8: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)

------------------------------------------------------------------
Your code has been rated at 7.37/10 (previous run: 0.95/10, +6.42)
```
