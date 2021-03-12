from sqlalchemy import *
import pandas as pd

class Medical_Rule:
    """This class is designed to allow one to examine a database to see whether
    physicians are pursuing cost-effective care that follow best practices or is one
    that might recommend more costly, expensive, and care that might have more side effects."""

    def __init__(self, database_name,diagnoses,procedures):
        self.database_name = database_name
        self.diagnoses = diagnoses
        self.procedures = procedures
        print('The inputs for the Medical Rule have been received')

    def denominator(self,database_name,interest_column,diagnoses,exceptions):
        stmt = select([database_name])
        for i in interest_column,diagnoses:
        stmt = stmt.where(or_(database_name.columns.interest_column[i] == diagnoses[i])
        results = connection.execute(stmt).fetchall()

