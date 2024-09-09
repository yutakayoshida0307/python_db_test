from src.db.mysql_db import DB


def select_sql(select_value):
    with open("src/sql/select.sql", "r") as f:
        query = f.read().format(select_value=select_value)
    return DB().select_query(query)


def select_parameterized_sql(select_value):
    with open("src/sql/select_parameterized.sql", "r") as f:
        query = f.read()
    return DB().select_query(query, param=(select_value,))


def insert_sql(insert_value):
    with open("src/sql/insert.sql", "r") as f:
        query = f.read().format(column_name=insert_value)
    return DB().exec_query(query)


def insert_parameterized_sql(insert_value):
    with open("src/sql/insert_parameterized.sql", "r") as f:
        query = f.read()
    return DB().exec_query(query, param=(insert_value,))


def insert_complex_sql(
    id,
    param1_1,
    param1_2,
    param_1_3,
    param_1_4,
    param2_1,
    param2_2,
    param2_3,
    param3_1,
    param3_2,
    param3_3,
):
    with open("src/sql/insert_complex_parameterized_table.sql", "r") as f:
        query = f.read()

    return DB().exec_query(
        query,
        param=(
            id,
            param1_1,
            param1_2,
            param_1_3,
            param_1_4,
            "",
            "",
            param2_1,
            param2_2,
            param2_3,
            param3_1,
            param3_2,
            param3_3,
        ),
    )
