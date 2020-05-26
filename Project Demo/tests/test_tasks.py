# Importing libraries
import pytest
from .utils import get_calls, get_assignments
from tasks import solution

# -------------------------------------------------
# Pytest for Task 1
# Importing the `pandas` library with an alias `pd`

@pytest.mark.test_task1
def test_task1():
    assert 'pd' in dir(solution), 'Have you imported the`pandas` library with an alias as `pd`?'
    
# -------------------------------------------------
# Pytest for Task 2
# Loading the Code.csv file in a variable `df1` using the `pd.read_csv()` method.

@pytest.mark.test_task2
def test_task2():
    assert get_calls(solution)[0] == 'pd:read_csv:data/Code.csv', 'Have you loaded the CSV file using the `pd.read_csv()` method with proper arguments?'
    assert get_assignments(solution)[0][:3] == 'df1', 'Has the `df1` DataFrame been created?'    

# -------------------------------------------------
# Pytest for Task 3
# Loading the ISOnum.csv file in a variable `df2` using the `pd.read_csv()` method.

@pytest.mark.test_task3
def test_task3():
    assert get_calls(solution)[1] == 'pd:read_csv:data/ISOnum.csv', 'Have you loaded the CSV file using the `pd.read_csv()` method with proper arguments?'
    assert get_assignments(solution)[1][:3] == 'df2', 'Has the `df2` DataFrame been created?'    

# -------------------------------------------------
# Pytest for Task 4
# Merging the dataframe df1 and df2 on column Country as a dataframe CountryCode

@pytest.mark.test_task4
def test_task4():    
    assert get_assignments(solution)[2][:11] == 'CountryCode', 'Has the `CountryCode` variable been created?'    
    assert get_calls(solution)[2] == 'CountryCode:pd:merge:df1:df2:on:country', 'You can use the `df.GRADE.median()` call to calculate the correct median.'
    get_assignments(solution)[2][32:] == 'country', 'Have you merged two dataframes on country column.'
