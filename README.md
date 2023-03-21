[![CircleCI](https://dl.circleci.com/status-badge/img/gh/jaysonmourier/EasyML/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/jaysonmourier/EasyML/tree/main)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# EasyML

EasyML is a machine learning framework designed to simplify the training of machine learning models. It is intended for non-expert users who want to leverage the power of these algorithms, but may not have a deep understanding of programming.

EasyML uses a Domain Specific Language (DSL) called TextX, which is written in Python. This allows users to access the power of machine learning algorithms in a more abstract and user-friendly way, without needing to be proficient in Python. The goal of EasyML is to provide a more accessible and user-friendly way of training machine learning models, making it possible for a wider range of users to take advantage of these powerful tools.

Whether you are a beginner or an experienced machine learning practitioner, EasyML provides a simple and intuitive way to train machine learning models and access the benefits of these algorithms.

## Usage

```
USE house_price_prediction.csv
FEATURES location, size, age, condition, n_bedrooms, n_bathrooms
TARGET price
MODEL svm
```

EasyML is designed to simplify the process of writing machine learning scripts, making it possible for even non-experts to train powerful models with ease.

Here's a simple use case to demonstrate how EasyML works:

- Load your data: The first step is to load your data into EasyML. In the example script, we use the "house_price_prediction.csv" file as our dataset.
- Specify features and target: Next, you need to specify which features you want to use for training, and what you want to predict (i.e., the target variable). In this example, the features are "location, size, age, condition, n_bedrooms, n_bathrooms", and the target is "price".
- Choose a model: Finally, you need to choose a model to train. In this example, we use the Support Vector Machine (SVM) algorithm.

With these three simple steps, you can train a machine learning model using EasyML. The framework will take care of all the heavy lifting, including preprocessing the data, selecting the right parameters, and training the model.

In the end, you'll get a pre-trained model that you can use to make predictions on new data. With EasyML, training machine learning models has never been easier!

