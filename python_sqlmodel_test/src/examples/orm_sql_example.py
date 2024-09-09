from src.models.tables import TestTable, TestComplexTable
from src.db.mysql_sql_model_db import SQLModelDB


def select_sql(select_value):
    db = SQLModelDB()
    return (
        db.session.query(TestTable).filter(TestTable.column_name == select_value).all()
    )


def insert_sql(insert_value):
    db = SQLModelDB()
    db.session.add(TestTable(column_name=insert_value))
    db.session.commit()


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
    db = SQLModelDB()
    db.session.add(
        TestComplexTable(
            id=id,
            param1_1=param1_1,
            param1_2=param1_2,
            param_1_3=param_1_3,
            param_1_4=param_1_4,
            param_unused_1="",
            param_unused_2="",
            param2_1=param2_1,
            param2_2=param2_2,
            param2_3=param2_3,
            param3_1=param3_1,
            param3_2=param3_2,
            param3_3=param3_3,
        )
    )
    db.session.commit()
