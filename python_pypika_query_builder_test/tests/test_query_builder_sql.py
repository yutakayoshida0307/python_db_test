from src.examples.query_builder_sql_example import (
    select_sql,
    insert_sql,
    select_parameterized_sql,
    insert_complex_sql,
)
from src.db.mysql_db import DB
from pypika import MySQLQuery as Query, Table


def test_query_builder_sql_select(cursor):
    """SELECT クエリのテスト"""

    db = DB()
    column_name = "new_value"
    query = Query.into("test_table").columns("column_name").insert(column_name)
    db.exec_query(str(query))

    result = select_sql("new_value")
    assert result is not None
    assert result[0]["column_name"] == "new_value"


def test_query_builder_sql_insert(cursor):
    """INSERT クエリのテスト"""

    insert_sql(insert_value="new_value")

    table = Table("test_table")
    select_query = (
        Query.from_("test_table").select("*").where(table["column_name"] == "new_value")
    )

    db = DB()
    result = db.select_query(str(select_query))

    assert result is not None
    assert result[0]["column_name"] == "new_value"


def test_query_builder_sql_injection(cursor):
    """SQLインジェクションのテスト"""

    db = DB()
    column_name = "new_value"
    query = Query.into("test_table").columns("column_name").insert(column_name)
    db.exec_query(str(query))

    result = select_sql(
        "new_value"
        # "new_value\\'; DROP TABLE test_table; --"  # SQL Injection
    )
    assert result is not None
    assert result[0]["column_name"] == "new_value"


def test_query_builder_sql_injection_defense(cursor):
    """SQLインジェクションの対策テスト"""

    db = DB()
    column_name = "new_value"
    query = Query.into("test_table").columns("column_name").insert(column_name)
    db.exec_query(str(query))

    select_parameterized_sql("new_value\\'; DROP TABLE test_table; --")

    # テーブルが削除されていないこと
    result = select_sql("new_value")
    assert result is not None
    assert result[0]["column_name"] == "new_value"


def test_raw_sql_complex_insert(cursor):
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

    table = Table("test_complex_table")
    select_query = Query.from_("test_complex_table").select("*").where(table["id"] == 1)
    db = DB()
    result = db.select_query(str(select_query))

    assert result is not None
    assert result[0]["param1_1"] == "param1_1"
    assert result[0]["param1_2"] == "param1_2"
    assert result[0]["param_1_3"] == "param_1_3"
    assert result[0]["param_1_4"] == "param_1_4"
    assert result[0]["param2_1"] == ""
    assert result[0]["param2_2"] == ""
    assert result[0]["param2_3"] == ""
    assert result[0]["param3_1"] == ""
    assert result[0]["param3_2"] == ""
    assert result[0]["param3_3"] == ""
