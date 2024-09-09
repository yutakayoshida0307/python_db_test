from src.examples.orm_sql_example import insert_sql, select_sql, insert_complex_sql
from src.models.tables import TestTable, TestComplexTable
from sqlmodel import select


def test_orm_sql_select(test_session):
    """SELECT クエリのテスト"""
    test_session.add(TestTable(column_name="new_value"))
    test_session.commit()

    result = select_sql("new_value")
    assert result is not None
    assert result[0].column_name == "new_value"


def test_orm_sql_insert(test_session):
    """INSERT クエリのテスト"""

    insert_sql(insert_value="new_value")

    result = (
        test_session.query(TestTable).filter(TestTable.column_name == "new_value").all()
    )

    assert result is not None
    assert result[0].column_name == "new_value"


def test_orm_sql_injection():
    pass


def test_orm_sql_complex_insert(test_session):
    """複雑なテーブルへのINSERT クエリのテスト"""

    insert_complex_sql(
        id=1,
        param1_1="param1_1",
        param1_2="param1_2",
        param_1_3="param_1_3",
        param_1_4="param_1_4",
        param2_1="",
        param2_2="",
        param2_3="",
        param3_1="",
        param3_2="",
        param3_3="",
    )

    statement = select(TestComplexTable).where(TestComplexTable.id == 1)
    result = test_session.execute(statement).first()

    assert result is not None
    assert result[0].param1_1 == "param1_1"
    assert result[0].param1_2 == "param1_2"
    assert result[0].param_1_3 == "param_1_3"
    assert result[0].param_1_4 == "param_1_4"
    assert result[0].param2_1 == ""
    assert result[0].param2_2 == ""
    assert result[0].param2_3 == ""
    assert result[0].param3_1 == ""
    assert result[0].param3_2 == ""
    assert result[0].param3_3 == ""
