# MLSQL - Open Source Structured Query Language Machine Learning

License: BSD 3 

# Overall System Architecture

# Dependency requirements: (will be packaged together in future)
1. Tensorflow 1.2+
2. Python 3.6
3. Python Ply package
4. sci-kit learn package
5. Pandas package
6. Dill package

# Using the parser:
1. Navigate to root folder 
2. run "parser/parser.py" as a python application (You need to execute it from the root folder.)


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

Syntax: TRAIN **estimator_name** WITH **profile_name**;

Example: TRAIN **salaryPredictor** WITH **oneshotSalary**;

# Advanced Usage:
1. Reusing an estimator
2. Reusing a training profile
3. Cloning an estimator

# Available ML tools:
1. Linear Regresstion (LR)

# Flowcharts

## Initial Control Flow
![Initial Control Flow](https://raw.githubusercontent.com/adhocmaster/MLSQL/vishal/presentation/flow_chart_broad.png)

## Train Model Control Flow
![Creating a Training Profile](https://raw.githubusercontent.com/adhocmaster/MLSQL/vishal/presentation/SQL_train.png)

