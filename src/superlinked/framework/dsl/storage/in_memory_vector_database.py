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


from superlinked.framework.dsl.storage.vector_database import VectorDatabase
from superlinked.framework.storage.in_memory.in_memory_vdb import InMemoryVDB


class InMemoryVectorDatabase(VectorDatabase[InMemoryVDB]):
    """
    In-memory implementation of the VectorDatabase.

    This class provides an in-memory vector database connector, which is useful for testing
    and development purposes.
    """

    def __init__(self) -> None:
        """
        Initialize the InMemoryVectorDatabase.

        This constructor initializes the in-memory vector database connector.
        """
        super().__init__()
        self.__vdb_connector = InMemoryVDB()

    @property
    def _vdb_connector(self) -> InMemoryVDB:
        """
        Get the in-memory vector database connector.

        Returns:
            InMemoryVDB: The in-memory vector database connector instance.
        """
        return self.__vdb_connector
