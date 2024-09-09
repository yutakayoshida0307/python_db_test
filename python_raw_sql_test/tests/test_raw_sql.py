from src.examples.raw_sql_example import (
    select_sql,
    insert_sql,
    select_parameterized_sql,
    insert_parameterized_sql,
    insert_complex_sql,
)
from src.db.mysql_db import DB


def test_raw_sql_select(cursor):
    """SELECT クエリのテスト"""

    db = DB()
    column_name = "new_value"
    query = f"INSERT INTO test_table (column_name) VALUES ('{column_name}')"
    db.exec_query(query)

    result = select_sql("new_value")
    assert result is not None
    assert result[0]["column_name"] == "new_value"


def test_raw_sql_insert(cursor):
    """INSERT クエリのテスト"""

    insert_sql(insert_value="new_value")

    select_query = "SELECT * FROM test_table WHERE (column_name) = 'new_value'"
    db = DB()
    result = db.select_query(str(select_query))

    assert result is not None
    assert result[0]["column_name"] == "new_value"


def test_raw_sql_sql_injection(cursor):
    """SQLインジェクションのテスト"""

    db = DB()
    column_name = "new_value1"
    query = f"INSERT INTO test_table (column_name) VALUES ('{column_name}')"
    db.exec_query(query)

    column_name = "new_value2"
    query = f"INSERT INTO test_table (column_name) VALUES ('{column_name}')"
    db.exec_query(query)

    # 全てのレコードを取得するSQLインジェクション
    result = select_sql("new_value' or '1' = '1")

    assert result is not None
    assert len(result) == 2
    assert result[0]["column_name"] == "new_value1"
    assert result[1]["column_name"] == "new_value2"


def test_raw_sql_injection_defense(cursor):
    """SQLインジェクションの対策テスト"""

    column_name = "new_value' or '1' = '1"
    insert_parameterized_sql(column_name)

    db = DB()
    column_name = "new_value2"
    query = f"INSERT INTO test_table (column_name) VALUES ('{column_name}')"
    db.exec_query(query)

    result = select_parameterized_sql("new_value' or '1' = '1")

    assert result is not None
    # SQLインジェクションの対策が効いているので、1レコードしか取得できない
    assert len(result) == 1
    assert result[0]["column_name"] == "new_value' or '1' = '1"


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

    select_query = "SELECT * FROM test_complex_table WHERE (id) = 1"
    db = DB()
    result = db.select_query(select_query)

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
