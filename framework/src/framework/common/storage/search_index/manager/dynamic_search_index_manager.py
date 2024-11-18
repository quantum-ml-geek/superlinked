# Copyright 2024 Superlinked, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import ABC, abstractmethod

from beartype.typing import Sequence
from typing_extensions import override

from superlinked.framework.common.storage.index_config import IndexConfig
from superlinked.framework.common.storage.search_index.manager.search_index_manager import (
    SearchIndexManager,
)


class DynamicSearchIndexManager(SearchIndexManager, ABC):
    @override
    def init_search_indices(
        self, index_configs: Sequence[IndexConfig], override_existing: bool = False
    ) -> None:
        self._index_configs.clear()
        existing_index_names = self._list_search_index_names_from_vdb()
        for index_config in index_configs:
            if index_config.index_name not in existing_index_names or override_existing:
                self._create_search_index_with_check(index_config)
            self._index_configs[index_config.index_name] = index_config

    def _create_search_index_with_check(self, index_config: IndexConfig) -> None:
        if index_config.index_name not in self._index_configs.keys():
            if (
                index_config.vector_field_descriptor.search_algorithm
                not in self.supported_vector_indexing
            ):
                raise NotImplementedError(
                    f"The specified vector search algorithm {index_config.vector_field_descriptor.search_algorithm}"
                    + f" is not yet supported. Currently supported algorithms: {self.supported_vector_indexing}"
                )
            self._create_search_index(index_config)

    @abstractmethod
    def _list_search_index_names_from_vdb(self) -> Sequence[str]:
        pass

    @abstractmethod
    def _create_search_index(self, index_config: IndexConfig) -> None:
        pass

    @abstractmethod
    def drop_search_index(self, index_name: str) -> None:
        pass
