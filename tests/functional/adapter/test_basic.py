import pytest

from dbt.tests.adapter.basic.test_base import BaseSimpleMaterializations
from dbt.tests.adapter.basic.test_singular_tests import BaseSingularTests
from dbt.tests.adapter.basic.test_singular_tests_ephemeral import (
    BaseSingularTestsEphemeral
)
from dbt.tests.adapter.basic.test_empty import BaseEmpty
from dbt.tests.adapter.basic.test_ephemeral import BaseEphemeral
from dbt.tests.adapter.basic.test_incremental import BaseIncremental
from dbt.tests.adapter.basic.test_generic_tests import BaseGenericTests
from dbt.tests.adapter.basic.test_snapshot_check_cols import BaseSnapshotCheckCols
from dbt.tests.adapter.basic.test_snapshot_timestamp import BaseSnapshotTimestamp
from dbt.tests.adapter.basic.test_adapter_methods import BaseAdapterMethod


class TestSimpleMaterializationsPipeRiderAdapter(BaseSimpleMaterializations):
    pass


class TestSingularTestsPipeRiderAdapter(BaseSingularTests):
    pass


class TestSingularTestsEphemeralPipeRiderAdapter(BaseSingularTestsEphemeral):
    pass


class TestEmptyPipeRiderAdapter(BaseEmpty):
    pass


class TestEphemeralPipeRiderAdapter(BaseEphemeral):
    pass


class TestIncrementalPipeRiderAdapter(BaseIncremental):
    pass


class TestGenericTestsPipeRiderAdapter(BaseGenericTests):
    pass


class TestSnapshotCheckColsPipeRiderAdapter(BaseSnapshotCheckCols):
    pass


class TestSnapshotTimestampPipeRiderAdapter(BaseSnapshotTimestamp):
    pass


class TestBaseAdapterMethodPipeRiderAdapter(BaseAdapterMethod):
    pass
