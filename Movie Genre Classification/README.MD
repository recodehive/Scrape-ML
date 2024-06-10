# Movie Genre Classification using Machine Learning

## Project Overview

Welcome to the Movie Genre Classification project! This project is part of the GirlScript Summer of Code program. The objective is to build a machine learning model to classify movies into genres based on various features such as plot summaries, cast, crew, and other metadata.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Dataset](#dataset)
- [Data Preprocessing](#data-preprocessing)
- [Model Training](#model-training)
- [Model Evaluation](#model-evaluation)
- [Usage](#usage)
- [License](#license)

## Introduction

Classifying movies into genres can enhance user experience by helping them find movies of their interest more easily. Machine learning can automate this classification process by analyzing various features of the movies.

In this project, we will:
1. Load and preprocess the movie dataset.
2. Train a machine learning model for genre classification.
3. Evaluate the performance of the model.
4. Provide usage instructions for making predictions on new data.

## Installation

To get started with this project, you'll need to have Python installed on your machine. You can install the necessary dependencies using pip:

```bash
pip install -r requirements.txt
```

## Dataset

The dataset used in this project consists of movie metadata, including plot summaries, cast, crew, and other relevant features. You can use publicly available datasets such as those from [IMDb](https://www.imdb.com/interfaces/) or [TMDb](https://www.themoviedb.org/documentation/api).

## Data Preprocessing

Data preprocessing steps include:
1. Loading the dataset.
2. Cleaning the data (handling missing values, removing duplicates, etc.).
3. Extracting relevant features (text processing for plot summaries, encoding categorical variables, etc.).
4. Splitting the dataset into training and testing sets.

## Model Training

We will use machine learning algorithms such as Logistic Regression, Random Forest, or a Neural Network for the classification task. The steps for training the model are as follows:
1. Choose the appropriate model.
2. Train the model on the training data.
3. Tune hyperparameters if necessary.

## Model Evaluation

To evaluate the performance of the model, we will use metrics such as:
- Accuracy
- Precision
- Recall
- F1-Score

Confusion matrix and ROC-AUC curve will also be plotted for a comprehensive evaluation.

## Usage

To use the trained model for making predictions on new data, follow these steps:

1. Load the pre-trained model from the saved file.
2. Prepare the input data in the same format as the training data.
3. Use the model to make predictions.

Example code:

```python
import pickle
import numpy as np

# Load the pre-trained model
with open('movie_genre_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Sample input data (replace with actual data)
input_data = np.array([[...]])

# Make predictions
predictions = model.predict(input_data)
print(predictions)
```


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
