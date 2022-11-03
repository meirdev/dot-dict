# Dot dict

Use `.` notation to access nested dict properties.

## Example

```python
from dot_dict import DotDict

d = {
    "a": {
        "b": {
            "c": "d",
        },
        "e": "f",
        "g": [
            "h",
            "i",
        ],
    }
}

obj = DotDict(d)

print(obj.a.b.c)  # d
print(obj.a.e)  # f
print(obj.a.g[0])  # h
```
