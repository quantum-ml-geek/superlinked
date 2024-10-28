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

from __future__ import annotations

from beartype.typing import Sequence

from superlinked.framework.common.dag.number_embedding_node import NumberEmbeddingNode
from superlinked.framework.query.dag.query_embedding_orphan_node import (
    QueryEmbeddingOrphanNode,
)
from superlinked.framework.query.dag.query_node import QueryNode


class QueryNumberEmbeddingNode(QueryEmbeddingOrphanNode[float, float]):
    def __init__(self, node: NumberEmbeddingNode, parents: Sequence[QueryNode]) -> None:
        super().__init__(node, parents, float)
