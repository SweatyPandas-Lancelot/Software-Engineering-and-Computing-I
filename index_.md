- 可能是你写完函数之后还在源文件里调用了一次自己，比如
```python
def func():
    ...
# end
func()
```