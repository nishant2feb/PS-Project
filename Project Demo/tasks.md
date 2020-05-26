# Setup

## Create Virtual Environment

In a terminal run the following commands from the root folder of the forked project.

```
python -m venv venv
```

Once that completes, also run this command from the same folder.

Windows

```
venv\Scripts\activate.bat
```

macOS & Linux

```
source venv/bin/activate
```

Now that you are working in the virtualenv, install the project dependencies with the following command.

```
pip install -r requirements.txt
```

## Verify Setup

In order to verify that everything is setup correctly, run the following command, which should show you the failing tests. This is good! We’ll be fixing this test once we jump into the build step.

```
pytest
```

Every time you want to check your work locally you can type that command, and it will report the status of every task in the project.

# Working on tasks

In this project you will work your way to import and merge two datasets into one.

## Task 1: Importing Pandas Library
**`@pytest.mark.test_task1`** In order to start working with the project, load the `pandas` library with an alias `pd` at the top of the `tasks/solution.py` file.

## Task 2: Importing the First CSV dataset
**`@pytest.mark.test_task2`** Next, in the same file load the dataset `Code.csv` from the `data` directory using the `pd.read_csv()` method and store the Pandas DataFrame in the `df1` variable.

## Task 3: Importing the Second CSV dataset
**`@pytest.mark.test_task3`** Next, in the same file load the dataset `ISOnum.csv` from the `data` directory using the `pd.read_csv()` method and store the Pandas DataFrame in the `df2` variable.

## Task 4: Merging the dataframe df1 and df2 on column country as a dataframe CountryCode
**`@pytest.mark.test_task4`** To merge the dataframe df1 and df2 on column country use `merge()` function and store the result to a dataframe `CountryCode`. 

