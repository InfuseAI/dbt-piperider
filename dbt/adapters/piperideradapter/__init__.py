from dbt.adapters.piperideradapter.connections import PipeRiderAdapterConnectionManager  # noqa
from dbt.adapters.piperideradapter.connections import PipeRiderAdapterCredentials
from dbt.adapters.piperideradapter.impl import PipeRiderAdapterAdapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import piperideradapter


Plugin = AdapterPlugin(
    adapter=PipeRiderAdapterAdapter,
    credentials=PipeRiderAdapterCredentials,
    include_path=piperideradapter.PACKAGE_PATH,
)
