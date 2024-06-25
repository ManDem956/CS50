import contextlib
from types import NoneType
from typing import Sized
import pytest

from contextlib import nullcontext as does_not_raise


def pytest_make_parametrize_id(config: pytest.Config, val: object, argname: str) -> str | None:
    if isinstance(val, (int, float, bool)):
        return f"{argname}:{str(val)}"
    if isinstance(val, (dict,)):
        # note this wouldn't show any hours/minutes/seconds
        return "-".join(f"{key}:{value}" for key, value in val.items())
    elif isinstance(val, (tuple,)):
        return f"{argname}:{str(len(val))}"
    elif isinstance(val, (list,)):
        return f"{argname}:{str(len(val))}"
    elif isinstance(val, (does_not_raise,)):
        return f"{argname}:does_not_raise"
    elif isinstance(val, (NoneType,)):
        return f"{argname}:nothing"
    elif isinstance(val, (contextlib.AbstractContextManager,)):
        return f"{argname}:raises"
    else:
        val_len = f":{len(val)}" if isinstance(val, (Sized,)) else ""
        return f"{argname}:{val.__class__.__name__}{val_len}"
