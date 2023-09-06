from dbt.adapters.piperider.connections import PipeRiderAdapterConnectionManager  # noqa
from dbt.adapters.piperider.connections import PipeRiderAdapterCredentials
from dbt.adapters.piperider.impl import PipeRiderAdapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import piperider


Plugin = AdapterPlugin(
    adapter=PipeRiderAdapter,  # type: ignore
    credentials=PipeRiderAdapterCredentials,
    include_path=piperider.PACKAGE_PATH,
)
