from dbt.adapters.base import BaseAdapter as adapter_cls

from dbt.adapters.piperider import PipeRiderAdapterConnectionManager


class PipeRiderAdapter(adapter_cls):
    """
    Controls actual implmentation of adapter, and ability to override certain methods.
    """

    ConnectionManager = PipeRiderAdapterConnectionManager

    @classmethod
    def date_function(cls):
        """
        Returns canonical date func
        """
        return "datenow()"

    @classmethod
    def is_cancelable(cls) -> bool:
        return False
