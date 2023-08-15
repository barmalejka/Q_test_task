# Objective

Given a dataset `train.csv` with 53 anonymized features and a target
column, build a model that predicts a target. Provide predictions for the `hidden_test.csv` file.

**Metric: RMSE.**

## Training

Exploratory data analysis showed, that `target` can be modeled as a simple $y = x^2 + b$ equation. Therefore there is no need for a `train.py` file.

## Prediction

Install requirements
```
pip install requirements.txt
```
Run the code
```
python3 predict.py --filename hidden_test.csv
```