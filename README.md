# **Lung Cancer Detection Model**

**Overview**

This repository contains code and resources for detecting lung cancer using machine learning models. The dataset used for this project is stored in a CSV file.

**Dataset**

The dataset used for training and testing the models is stored in `data.csv`. It includes the following columns:

- **GENDER**
- **AGE**
- **SMOKING**
- **YELLOW_FINGERS**
- **ANXIETY**
- **PEER_PRESSURE**
- **CHRONIC DISEASE**
- **FATIGUE**
- **ALLERGY**
- **WHEEZING**
- **ALCOHOL CONSUMING**
- **COUGHING**
- **SHORTNESS OF BREATH**
- **SWALLOWING DIFFICULTY**
- **CHEST PAIN**
- **LUNG_CANCER** (Target: Indicates the presence or absence of lung cancer)

**Machine Learning Models**

The following machine learning models have been implemented and evaluated:

- Linear Regression
- Logistic Regression
- Gradient Boosting
- k-Nearest Neighbors (KNN)
- Decision Tree Classifier
- Random Forest Classifier
- CATBoost Classifier
- XGBoost Classifier

**Usage**

**Environment Setup**
1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Ensure Python 3.x is used.

**Running the Models**
- `model.ipynb` contains the model training and testing process for all the models. 
- Execute the file to train and evaluate the model.

- NOTE: Use a separate conda environment for avoiding future errors with dependencies.

**Results**

The performance metrics and evaluation results for each model are documented in the respective model's notebook. 

**Future Improvements**

- Deploying the Model into a Web Application with a proper UI.
- Feature engineering techniques to enhance model performance.
- Hyperparameter tuning for optimizing model accuracy.
- Incorporating deep learning models for comparison.

**Contribution**

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

**License**

This project is licensed under the [Apache License](LICENSE).

**Acknowledgments**

- Dataset Credits : https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer
- Reference : https://www.kaggle.com/code/casper6290/lung-cancer-prediction-98

The above notebook was helpful in terms of understanding the preprocessing and model development process properly.
