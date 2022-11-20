from typing import Any, Callable


def default_is_value(obj: Any) -> bool:
    return obj is None or isinstance(obj, (int, float, str, bool))


class DotDict:
    def __init__(
        self, obj: Any, is_value_fn: Callable[[Any], bool] = default_is_value
    ) -> None:
        self._obj = obj
        self._is_value_fn = is_value_fn

    def __getattribute__(self, name: str) -> Any:
        return self[name]

    def __getitem__(self, name: Any) -> Any:
        obj = super().__getattribute__("_obj")
        is_value_fn = super().__getattribute__("_is_value_fn")

        obj = obj[name]
        if is_value_fn(obj):
            return obj

        return DotDict(obj, is_value_fn)

    def __call__(self) -> Any:
        return super().__getattribute__("_obj")
