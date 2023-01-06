from typing import Any, Generic

from .core import ACLCommands, DataAccessCommands, ManagementCommands, PubSubCommands, _StrType

# TODO: Stubs for `AsyncRedisClusterCommands`
class AsyncRedisClusterCommands: ...

class ClusterMultiKeyCommands:
    def mget_nonatomic(self, keys, *args): ...
    def mset_nonatomic(self, mapping): ...
    def exists(self, *keys): ...
    def delete(self, *keys): ...
    def touch(self, *keys): ...
    def unlink(self, *keys): ...

class ClusterManagementCommands(ManagementCommands):
    def slaveof(self, *args, **kwargs) -> None: ...
    def replicaof(self, *args, **kwargs) -> None: ...
    def swapdb(self, *args, **kwargs) -> None: ...

class ClusterDataAccessCommands(DataAccessCommands[_StrType], Generic[_StrType]):
    def stralgo(
        self,
        algo,
        value1,
        value2,
        specific_argument: str = ...,
        len: bool = ...,
        idx: bool = ...,
        minmatchlen: Any | None = ...,
        withmatchlen: bool = ...,
        **kwargs,
    ): ...

class RedisClusterCommands(
    ClusterMultiKeyCommands,
    ClusterManagementCommands,
    ACLCommands[_StrType],
    PubSubCommands,
    ClusterDataAccessCommands[_StrType],
    Generic[_StrType],
):
    def cluster_addslots(self, target_node, *slots): ...
    def cluster_countkeysinslot(self, slot_id): ...
    def cluster_count_failure_report(self, node_id): ...
    def cluster_delslots(self, *slots): ...
    def cluster_failover(self, target_node, option: Any | None = ...): ...
    def cluster_info(self, target_nodes: Any | None = ...): ...
    def cluster_keyslot(self, key): ...
    def cluster_meet(self, host, port, target_nodes: Any | None = ...): ...
    def cluster_nodes(self): ...
    def cluster_replicate(self, target_nodes, node_id): ...
    def cluster_reset(self, soft: bool = ..., target_nodes: Any | None = ...): ...
    def cluster_save_config(self, target_nodes: Any | None = ...): ...
    def cluster_get_keys_in_slot(self, slot, num_keys): ...
    def cluster_set_config_epoch(self, epoch, target_nodes: Any | None = ...): ...
    def cluster_setslot(self, target_node, node_id, slot_id, state): ...
    def cluster_setslot_stable(self, slot_id): ...
    def cluster_replicas(self, node_id, target_nodes: Any | None = ...): ...
    def cluster_slots(self, target_nodes: Any | None = ...): ...
    read_from_replicas: bool
    def readonly(self, target_nodes: Any | None = ...): ...
    def readwrite(self, target_nodes: Any | None = ...): ...
