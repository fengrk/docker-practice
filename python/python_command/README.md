# python 命令

本示例演示两种命令行执行 python 包指令的方法. 

## 目标

在自建 python 包`py_package` 中, 提供两种命令执行方式:

一种是

```
python -m py_package
python -m py_package.a
```

另一种是

``` 
py_pacakge_print 
py_pacakge_print_a
```

## 实现

### 指令一

对于第一种指令, 

命令 `python -m py_package` 实际上是运行 `py_package/__main__.py`.

命令 `python -m py_package.a` 实际上是运行 `py_package/a/__main__.py`.

所以, 提供相应的`__main__.py` 即可:

`./__main__.py`:

```python

from .cmd import cmd_demo

if __name__ == '__main__':
    cmd_demo(name="py_package")

```

`./a/__main__.py`: 

```python
from ..cmd import cmd_demo

if __name__ == '__main__':
    cmd_demo(name="py_package/a")

```

### 指令二

对于第二种指令, 其实是在 `setup.py` 中的 `entry_points` 提供命令映射.

本例中, 可以这样设置:

```
    entry_points={
        'console_scripts': [
            'py_package_print = py_package.info:print_package',
            'py_package_print_a = py_package:print_a'
        ]
    }
```

## 结果

使用 `docker-compose` 运行实例:

```docker-compose up ```

日志中可看到执行结果:

```
py-cmd    | exec:       python -m py_package xxxx
py-cmd    | [py_package] read input: /usr/local/lib/python3.7/site-packages/py_package/__main__.py xxxx
py-cmd    | 
py-cmd    | 
py-cmd    | exec:       python -m py_package.a yyyy
py-cmd    | [py_package/a] read input: /usr/local/lib/python3.7/site-packages/py_package/a/__main__.py yyyy
py-cmd    | 
py-cmd    | 
py-cmd    | exec:       py_package_print
py-cmd    | file in py_package/:
py-cmd    |     __main__.py
py-cmd    |     __pycache__
py-cmd    |     __init__.py
py-cmd    |     cmd
py-cmd    |     a
py-cmd    |     info.py
py-cmd    | 
py-cmd    | 
py-cmd    | 
py-cmd    | exec:       py_package_print_a
py-cmd    | file in py_package/a/:
py-cmd    |     __main__.py
py-cmd    |     __pycache__
py-cmd    |     __init__.py
py-cmd    | 

```









