from _typeshed import Incomplete
from typing import Any

class HDC:
    dc: Any
    def __init__(self, dc) -> None: ...
    def __int__(self) -> int: ...

class HWND:
    wnd: Any
    def __init__(self, wnd) -> None: ...
    def __int__(self) -> int: ...

class Dib:
    image: Any
    mode: Any
    size: Any
    def __init__(self, image, size: Incomplete | None = ...) -> None: ...
    def expose(self, handle): ...
    def draw(self, handle, dst, src: Incomplete | None = ...): ...
    def query_palette(self, handle): ...
    def paste(self, im, box: Incomplete | None = ...) -> None: ...
    def frombytes(self, buffer): ...
    def tobytes(self): ...

class Window:
    hwnd: Any
    def __init__(self, title: str = ..., width: Incomplete | None = ..., height: Incomplete | None = ...) -> None: ...
    def ui_handle_clear(self, dc, x0, y0, x1, y1) -> None: ...
    def ui_handle_damage(self, x0, y0, x1, y1) -> None: ...
    def ui_handle_destroy(self) -> None: ...
    def ui_handle_repair(self, dc, x0, y0, x1, y1) -> None: ...
    def ui_handle_resize(self, width, height) -> None: ...
    def mainloop(self) -> None: ...

class ImageWindow(Window):
    image: Any
    def __init__(self, image, title: str = ...) -> None: ...
    def ui_handle_repair(self, dc, x0, y0, x1, y1) -> None: ...
