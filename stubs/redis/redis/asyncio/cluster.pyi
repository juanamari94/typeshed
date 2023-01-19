from _typeshed import Self
from collections.abc import Awaitable, Mapping
from typing import Any, Generic

from redis.asyncio.client import ResponseCallbackT
from redis.asyncio.connection import BaseParser, Connection, Encoder
from redis.client import AbstractRedis
from redis.cluster import AbstractRedisCluster

# TODO: add  AsyncRedisClusterCommands stubs
# from redis.commands import AsyncRedisClusterCommands
from redis.commands.core import _StrType
from redis.credentials import CredentialProvider
from redis.retry import Retry
from redis.typing import AnyKeyT, EncodableT, KeyT

# It uses `DefaultParser` in real life, but it is a dynamic base class.
class ClusterParser(BaseParser): ...

class RedisCluster(AbstractRedis, AbstractRedisCluster, Generic[_StrType]):  # TODO: AsyncRedisClusterCommands
    def __init__(
        self,
        host: str | None = ...,
        port: str | int = ...,
        # Cluster related kwargs
        startup_nodes: list[ClusterNode] | None = ...,
        require_full_coverage: bool = ...,
        read_from_replicas: bool = ...,
        reinitialize_steps: int = ...,
        cluster_error_retry_attempts: int = ...,
        connection_error_retry_attempts: int = ...,
        max_connections: int = ...,
        # Client related kwargs
        db: str | int = ...,
        path: str | None = ...,
        credential_provider: CredentialProvider | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        client_name: str | None = ...,
        # Encoding related kwargs
        encoding: str = ...,
        encoding_errors: str = ...,
        decode_responses: bool = ...,
        # Connection related kwargs
        health_check_interval: float = ...,
        socket_connect_timeout: float | None = ...,
        socket_keepalive: bool = ...,
        socket_keepalive_options: Mapping[int, int | bytes] | None = ...,
        socket_timeout: float | None = ...,
        retry: Retry | None = ...,
        retry_on_error: list[Exception] | None = ...,
        # SSL related kwargs
        ssl: bool = ...,
        ssl_ca_certs: str | None = ...,
        ssl_ca_data: str | None = ...,
        ssl_cert_reqs: str = ...,
        ssl_certfile: str | None = ...,
        ssl_check_hostname: bool = ...,
        ssl_keyfile: str | None = ...,
    ) -> None: ...
    async def initialize(self: Self) -> Self: ...
    async def close(self) -> None: ...
    async def __aenter__(self: Self) -> Self: ...
    async def __aexit__(self, exc_type: object, exc_value: object, traceback: object) -> None: ...
    def __await__(self: Self) -> Awaitable[Self]: ...
    def __del__(self) -> None: ...
    async def on_connect(self, connection: Connection) -> None: ...
    def get_nodes(self) -> list[ClusterNode]: ...
    def get_primaries(self) -> list[ClusterNode]: ...
    def get_replicas(self) -> list[ClusterNode]: ...
    def get_random_node(self) -> ClusterNode: ...
    def get_default_node(self) -> ClusterNode: ...
    def set_default_node(self, node: ClusterNode) -> None: ...
    def get_node(self, host: str | None = ..., port: int | None = ..., node_name: str | None = ...) -> ClusterNode | None: ...
    def get_node_from_key(self, key: str, replica: bool = ...) -> ClusterNode | None: ...
    def keyslot(self, key: EncodableT) -> int: ...
    def get_encoder(self) -> Encoder: ...
    def get_connection_kwargs(self) -> dict[str, Any | None]: ...
    def set_response_callback(self, command: str, callback: ResponseCallbackT) -> None: ...
    async def execute_command(self, *args: EncodableT, **kwargs: Any) -> Any: ...
    def pipeline(self, transaction: Any | None = ..., shard_hint: Any | None = ...) -> ClusterPipeline: ...
    @classmethod
    def from_url(cls: type[Self], url: str, **kwargs) -> Self: ...

class ClusterNode:
    def __init__(
        self,
        host: str,
        port: str | int,
        server_type: str | None = ...,
        *,
        max_connections: int = ...,
        connection_class: type[Connection] = ...,
        **connection_kwargs: Any,
    ) -> None: ...
    def __eq__(self, obj: object) -> bool: ...
    def __del__(self) -> None: ...
    async def disconnect(self) -> None: ...
    def acquire_connection(self) -> Connection: ...
    async def parse_response(self, connection: Connection, command: str, **kwargs: Any) -> Any: ...
    async def execute_command(self, *args: Any, **kwargs: Any) -> Any: ...
    async def execute_pipeline(self, commands: list[PipelineCommand]) -> bool: ...

class NodesManager:
    def __init__(
        self, startup_nodes: list[ClusterNode], require_full_coverage: bool, connection_kwargs: dict[str, Any]
    ) -> None: ...
    def get_node(self, host: str | None = ..., port: int | None = ..., node_name: str | None = ...) -> ClusterNode | None: ...
    def set_nodes(self, old: dict[str, ClusterNode], new: dict[str, ClusterNode], remove_old: bool = ...) -> None: ...
    def get_node_from_slot(self, slot: int, read_from_replicas: bool = ...) -> ClusterNode: ...
    def get_nodes_by_server_type(self, server_type: str) -> list[ClusterNode]: ...
    async def initialize(self) -> None: ...
    async def close(self, attr: str = ...) -> None: ...

class ClusterPipeline(AbstractRedis, AbstractRedisCluster, Generic[_StrType]):  # TODO: AsyncRedisClusterCommands
    def __init__(self, client: RedisCluster) -> None: ...
    async def initialize(self: Self) -> Self: ...
    async def __aenter__(self: Self) -> Self: ...
    async def __aexit__(self, exc_type: object, exc_value: object, traceback: object) -> None: ...
    def __await__(self: Self) -> Awaitable[Self]: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, exc_type: object, exc_value: object, traceback: object) -> None: ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...
    def execute_command(self: Self, *args: KeyT | EncodableT, **kwargs: Any) -> Self: ...
    async def execute(self, raise_on_error: bool = ..., allow_redirections: bool = ...) -> list[Any]: ...
    def mset_nonatomic(self: Self, mapping: Mapping[AnyKeyT, EncodableT]) -> Self: ...

class PipelineCommand:
    def __init__(self, position: int, *args: Any, **kwargs: Any) -> None: ...
