from sqlmodel import SQLModel, Field
from datetime import datetime


class TestTable(SQLModel, table=True):
    __tablename__ = "test_table"

    id: int = Field(default=None, primary_key=True)
    column_name: str = Field(nullable=False, max_length=255)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class TestComplexTable(SQLModel, table=True):
    __tablename__ = "test_complex_table"

    id: int = Field(default=None, primary_key=True)
    param1_1: str = Field(nullable=False, max_length=255)
    param1_2: str = Field(nullable=False, max_length=255)
    param_1_3: str = Field(nullable=False, max_length=255)
    param_1_4: str = Field(nullable=False, max_length=255)
    param_unused_1: str = Field(nullable=False, max_length=255)
    param_unused_2: str = Field(nullable=False, max_length=255)
    param2_1: str = Field(nullable=False, max_length=255)
    param2_2: str = Field(nullable=False, max_length=255)
    param2_3: str = Field(nullable=False, max_length=255)
    param3_1: str = Field(nullable=False, max_length=255)
    param3_2: str = Field(nullable=False, max_length=255)
    param3_3: str = Field(nullable=False, max_length=255)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
