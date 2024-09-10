from src.db.mysql_db import DB
from pypika import MySQLQuery as Query, Table, Parameter, Criterion


def select_sql(select_value):
    table = Table("test_table")
    query = Query.from_(table).select("*").where(table["column_name"] == select_value)
    return DB().select_query(str(query))


def insert_sql(insert_value):
    table = Table("test_table")
    query = Query.into(table).columns("column_name").insert(insert_value)
    return DB().exec_query(str(query))


def select_parameterized_sql(select_value):
    table = Table("test_table")

    query = (
        Query.from_(table).select("*").where(table["column_name"] == Parameter("%s"))
    )
    return DB().select_query(str(query), param=(select_value,))


def insert_complex_sql(
    id,
    param1_1,
    param1_2,
    param1_3,
    param1_4,
    param2_1,
    param2_2,
    param2_3,
    param3_1,
    param3_2,
    param3_3,
):
    query = (
        Query.into("test_complex_table")
        .columns(
            "id",
            "param1_1",
            "param1_2",
            "param1_3",
            "param1_4",
            "param_unused_1",
            "param_unused_2",
            "param2_1",
            "param2_2",
            "param2_3",
            "param3_1",
            "param3_2",
            "param3_3",
        )
        .insert(
            Parameter("%s"),
            Parameter("%s"),
            Parameter("%s"),
            Parameter("%s"),
            Parameter("%s"),
            Parameter("%s"),
            Parameter("%s"),
            Parameter("%s"),
            Parameter("%s"),
            Parameter("%s"),
            Parameter("%s"),
            Parameter("%s"),
            Parameter("%s"),
        )
    )

    return DB().exec_query(
        str(query),
        param=(
            id,
            param1_1,
            param1_2,
            param1_3,
            param1_4,
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


def select_complex_sql(select_value, param1=None, param2=None, param3=None):
    table = Table("test_complex_table2")
    query = Query.from_(table).select("*")
    where_terms = []
    params = ()

    if param1 is not None:
        where_terms.append(table["param1"] == Parameter("%s"))
        params += (param1,)
    if param2 is not None:
        where_terms.append(table["param2"] == Parameter("%s"))
        params += (param2,)
    if param3 is not None:
        where_terms.append(table["param3"] == Parameter("%s"))
        params += (param3,)

    if where_terms:
        query = query.where(Criterion.all(where_terms))

    return DB().select_query(str(query), param=params)
