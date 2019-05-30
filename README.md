# MLSQL - Open Source Structured Query Language Machine Learning

License: BSD 3 

# Overall System Architecture

# Using the parser:
1. Navigate to folder "parser"
2. run parser.py as a python application


## Creating an estimator
Syntax: CREATE ESTIMATOR **estimator_name** TYPE **type_name** FORMULA $**formula**$;

Example: CREATE ESTIMATOR **salaryPredictor** TYPE **LR FORMULA** $**salary~years**$;
### Formula

Formula fields must exactly be the same as the SQL resultset.

## Creating a training profile

Syntax: CREATE TRAINING PROFILE **profile_name** WITH [**sql**];

Example: CREATE TRAINING PROFILE **oneshotSalary** WITH [**SELECT * FROM salary**];

## Choose Database
USE '**data/salarydb.db**';

## Training an estimator with a training profile
Syntax: TRAIN **estimator_name** WITH TRAINING PROFILE **profile_name**;

Example: TRAIN **salaryPredictor** WITH TRAINING PROFILE **oneshotSalary**;

# Advanced Usage:
1. Reusing an estimator
2. Reusing a training profile
3. Cloning an estimator

# Available ML tools:
1. Linear Regresstion (LR)

# Flowcharts
![Creating a Training Profile](https://raw.githubusercontent.com/adhocmaster/MLSQL/vishal/presentation/SQL_train.png)

