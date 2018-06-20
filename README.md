# findreplace

Go through a directory recursively, find and replace specified values in file names and file data.

```python
pipenv install findreplace
```

example

```python
findreplace replace ~/git/findreplace/testdir '{{example}}' main

from findreplace.core import findreplace
base_dir='~/git/findreplace/testdir'
find_replace_dict = {'{{example}}': 'main', '{{dog}}': 'test'}
findreplace(base_dir=base_dir, find_replace_dict=find_replace_dict)
```
