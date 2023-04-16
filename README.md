# Quick Viz

"Quick Viz" offers quick vizualization for adhoc analysis.


# Note
Quick Viz uses the following libraries.
* [pandas](https://github.com/pandas-dev/pandas)>=1.3.0
* [pygwalker](https://github.com/Kanaries/pygwalker)==0.1.4.8

Please note that the version of the currently used libraries may change by installtion of Quick Viz.

# Usage

## Installation of Quick Viz

```bash
$ pip install git+https://github.com/Taichi-Ibi/quick-viz
```

## How to use it in Terminal
```bash
$ qviz
```
or
```bash
$ qviz "/Users/hoge/hoge.csv"
```

If you're using a terminal, you can get the file path by dragging and dropping a CSV or XLSX file onto the terminal.
  
  
## How to use it in Python
```python
from qviz import qviz

qviz("/Users/hoge/hoge.csv")
```

# Author

* *T.Ibi*
* *Y.Suzuki*
* *Y.Wada*

# License

"Quick Viz" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).

Let's get rid of boring jobs!

Thank you!