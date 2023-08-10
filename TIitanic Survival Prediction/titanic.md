# Titanic Survival Prediction Project

This project involves predicting the survival status of passengers on the Titanic using machine learning techniques. The goal is to analyze various features of passengers and build a model that can predict whether a passenger survived or not based on those features.

## Dataset

The dataset used for this project is sourced from Kaggle and can be accessed here: [Titanic Dataset](https://www.kaggle.com/code/sabahattincag/beginner-friendly-titanic-data-preparation). It contains information about passengers on the Titanic, including features like age, gender, class, fare, and more.

### About the Titanic
The Titanic was a British passenger liner that sank on its maiden voyage from Southampton, England, to New York City, USA, on April 15, 1912. Here are some key details about the Titanic's journey:

- Departure: April 10, 1912, from Southampton, England.
- Specifications: One of the largest and most luxurious ships of its time.
- Passengers and Crew: Approximately 2,224 passengers and crew members.
- Sinking: Collided with an iceberg on April 14, 1912.
- Casualties: Over 1,500 people lost their lives in the disaster.

## Code for Data Analysis and Model Building
The provided Python code includes data analysis, preprocessing, and model building steps. It uses libraries like Pandas, Seaborn, Matplotlib, and scikit-learn to perform these tasks.

The code can be divided into the following sections:

1. **Importing Modules**: Importing necessary libraries for data analysis and model building.
2. **Importing Dataset**: Loading and exploring the Titanic dataset.
3. **Data Preprocessing**: Handling missing values, dropping unnecessary columns, and encoding categorical features.
4. **Data Analysis**: Exploring and visualizing the dataset to gain insights.
5. **Model Building**: Splitting the data into training and testing sets, building a Logistic Regression model, and evaluating its accuracy.

The code also includes a section for saving the trained model using the `joblib` library.

## Flask Deployment

Additionally, the code includes a Flask application for deploying the trained model. The Flask app allows users to input passenger information and receive a prediction about their survival status. The user interface is implemented using HTML templates.

The Flask app includes the following components:

1. **Home Page**: Displays a form for users to input passenger details.
2. **Prediction Page**: Processes the input data, preprocesses it, makes predictions using the trained model, and displays the prediction results.

## Instructions

1. Clone this repository to your local machine.
2. Download the Titanic dataset from the provided Kaggle link and place it in the same directory as the code.
3. Run the code snippets in the appropriate sequence to perform data analysis, model building, and deployment.
4. Access the Flask app by running the Flask application (`app.py`) and navigating to the provided URL (usually `http://127.0.0.1:5000/`).

For questions or further information, feel free to contact Sudipa Koner.

---

**Note:** Ensure that the Titanic dataset (`train.csv`) is placed in the same directory as the code for successful execution.
