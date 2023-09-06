from contextlib import contextmanager
from dataclasses import dataclass
from typing import Tuple, List, Dict, Hashable, Optional

import agate
import dbt.exceptions  # noqa
from dbt.adapters.base import Credentials
from dbt.adapters.base.query_headers import MacroQueryStringSetter
from dbt.adapters.sql import SQLConnectionManager
from dbt.contracts.connection import AdapterResponse, AdapterRequiredConfig, Connection


# from dbt.logger import GLOBAL_LOGGER as logger


@dataclass
class PipeRiderAdapterCredentials(Credentials):
    """
    Defines database specific credentials that get added to
    profiles.yml to connect to new adapter
    """

    # Add credentials members here, like:
    # host: str
    # port: int
    # username: str
    # password: str
    database: str = "main"
    schema: str = "main"
    host: str = "somewhere"

    _ALIASES = {"description": "host"}

    @property
    def type(self):
        """Return name of adapter."""
        return "piperider"

    @property
    def unique_field(self):
        """
        Hashed and included in anonymous telemetry to track adapter adoption.
        Pick a field that can uniquely identify one team/organization building with this adapter
        """
        return self.host

    def _connection_keys(self):
        """
        List of keys to display in the `dbt debug` output.
        """
        return ()


class FakeLock:
    def __enter__(self):
        """In __enter__()"""
        pass

    def __exit__(self, exception_type, exception_value, exception_traceback):
        """In __exit__()"""
        pass


class PipeRiderAdapterConnectionManager(SQLConnectionManager):
    def __init__(self, profile: AdapterRequiredConfig):
        self.profile = profile
        self.thread_connections: Dict[Hashable, Connection] = {}
        self.lock: FakeLock = FakeLock()  # type: ignore
        self.query_header: Optional[MacroQueryStringSetter] = None

    def cancel_open(self) -> List[str]:
        return super().cancel_open()

    def execute(
        self, sql: str, auto_begin: bool = False, fetch: bool = False, limit: Optional[int] = None
    ) -> Tuple[AdapterResponse, agate.Table]:
        return super().execute(sql, auto_begin, fetch)

    def begin(self):
        super().begin()

    def commit(self):
        super().commit()

    TYPE = "piperider"

    @contextmanager
    def exception_handler(self, sql: str):
        """
        Returns a context manager, that will handle exceptions raised
        from queries, catch, log, and raise dbt exceptions it knows how to handle.
        """
        # ## Example ##
        # try:
        #     yield
        # except myadapter_library.DatabaseError as exc:
        #     self.release(connection_name)

        #     logger.debug("myadapter error: {}".format(str(e)))
        #     raise dbt.exceptions.DatabaseException(str(exc))
        # except Exception as exc:
        #     logger.debug("Error running SQL: {}".format(sql))
        #     logger.debug("Rolling back transaction.")
        #     self.release(connection_name)
        #     raise dbt.exceptions.RuntimeException(str(exc))
        pass

    @classmethod
    def open(cls, connection):
        """
        Receives a connection object and a Credentials object
        and moves it to the "open" state.
        """
        # ## Example ##
        # if connection.state == "open":
        #     logger.debug("Connection is already open, skipping open.")
        #     return connection

        # credentials = connection.credentials

        # try:
        #     handle = myadapter_library.connect(
        #         host=credentials.host,
        #         port=credentials.port,
        #         username=credentials.username,
        #         password=credentials.password,
        #         catalog=credentials.database
        #     )
        #     connection.state = "open"
        #     connection.handle = handle
        # return connection
        pass

    @classmethod
    def get_response(cls, cursor):
        """
        Gets a cursor object and returns adapter-specific information
        about the last executed command generally a AdapterResponse ojbect
        that has items such as code, rows_affected,etc. can also just be a string ex. "OK"
        if your cursor does not offer rich metadata.
        """
        # ## Example ##
        # return cursor.status_message
        pass

    def cancel(self, connection):
        """
        Gets a connection object and attempts to cancel any ongoing queries.
        """
        # ## Example ##
        # tid = connection.handle.transaction_id()
        # sql = "select cancel_transaction({})".format(tid)
        # logger.debug("Cancelling query "{}" ({})".format(connection_name, pid))
        # _, cursor = self.add_query(sql, "master")
        # res = cursor.fetchone()
        # logger.debug("Canceled query "{}": {}".format(connection_name, res))
        pass
