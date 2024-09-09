import pytest
from pytest_mock import MockFixture

from src.db.mysql_db import DB
from tests.mysql_test_db import DB as TestDB


@pytest.fixture
def cursor(mocker: MockFixture):
    db = TestDB()
    
    mocker.patch.object(DB, "__new__", return_value=db)

    with db.connector as conn:
        with conn.cursor() as cur:
            print("\n" + "START TEST")
            yield cur
            print("\n" + "END TEST")
        conn.rollback()