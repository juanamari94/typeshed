import time
from _typeshed import Incomplete
from typing import Any

from ...core import AWSXRayRecorder
from ..exceptions.exceptions import SegmentNotFoundException as SegmentNotFoundException
from .entity import Entity as Entity
from .segment import Segment

SUBSEGMENT_RECORDING_ATTRIBUTE: str

def set_as_recording(decorated_func, wrapped) -> None: ...
def is_already_recording(func): ...
def subsegment_decorator(wrapped, instance, args, kwargs): ...

class SubsegmentContextManager:
    name: str | None
    subsegment_kwargs: dict[str, Any] | None
    recorder: AWSXRayRecorder
    subsegment: Subsegment
    def __init__(self, recorder: AWSXRayRecorder, name: Incomplete | None = ..., **subsegment_kwargs) -> None: ...
    def __call__(self, wrapped, instance, args: list[Any], kwargs: dict[str, Any]): ...
    def __enter__(self) -> Subsegment: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

class Subsegment(Entity):
    parent_segment: Segment
    trace_id: str
    type: str
    namespace: str
    sql: dict[str, Any]
    def __init__(self, name: str, namespace: str, segment: Segment) -> None: ...
    def add_subsegment(self, subsegment: Subsegment) -> None: ...
    def remove_subsegment(self, subsegment: Subsegment) -> None: ...
    def close(self, end_time: time.struct_time | None = ...) -> None: ...
    def set_sql(self, sql: dict[str, Any]) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...
