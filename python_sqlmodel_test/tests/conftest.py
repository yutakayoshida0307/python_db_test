import pytest
from sqlmodel import Session
from tests.mysql_sql_model_test_db import TestDB as TestDB
import sqlalchemy as sa
from pytest_mock import MockFixture
from src.db.mysql_sql_model_db import SQLModelDB


@pytest.fixture
def test_session(mocker: MockFixture) -> Session:
    db = TestDB()
    transaction = db.connection.begin()
    session = db.init_session()

    nested = db.connection.begin_nested()

    @sa.event.listens_for(session, "after_transaction_end")
    def end_savepoint(session, transaction):
        nonlocal nested
        if not nested.is_active:
            nested = db.connection.begin_nested()

    mocker.patch.object(SQLModelDB, "__new__", return_value=db)

    yield db.session

    db.session.close()
    transaction.rollback()
    db.connection.close()
