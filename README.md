# fraud-detection
##### In this project, we're building a Machine Learning model that detects fraud transitions.
###### Dataset: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/data

## Key Words:
1. Imbalanced dataset
2. Fraud detection
3. Python
4. Scikit-learn
5. Pandas


## Instructions:
1. Set Up the Virtual Environment
- Create a virtual environment by running:
  
 `python -m venv venv `
 
2. Activate the virtual environment:

      For Windows:

        venv\Scripts\activate
        
      For MacOS/Linux:

        source venv/bin/activate

2. Install Dependencies
   
      Install all required packages from requirements.txt:
   
        pip install -r requirements.txt


4. Start the Uvicorn Server
   
        uvicorn main:app --reload

6. Send a POST Request
   
Send a POST request to the server using Postman or curl, with data from artifacts/sample.json as a template.

Example curl command:

    curl -X POST <localhost address> -H "Content-Type: application/json" -d "{
    \"Time\": 2.0,
    \"V1\": -1.158233093,
    \"V2\": 0.877736755,
    \"V3\": 1.548717847,
    \"V4\": 0.403033934,
    \"V5\": -0.407193377,
    \"V6\": 0.095921462,
    \"V7\": 0.592940745,
    \"V8\": -0.270532677,
    \"V9\": 0.817739308,
    \"V10\": 0.753074432,
    \"V11\": -0.822842878,
    \"V12\": 0.53819555,
    \"V13\": 1.345851593,
    \"V14\": -1.119669835,
    \"V15\": 0.17512113,
    \"V16\": -0.451449183,
    \"V17\": -0.237033239,
    \"V18\": -0.038194787,
    \"V19\": 0.803486925,
    \"V20\": 0.40854236,
    \"V21\": -0.009430697,
    \"V22\": 0.798278495,
    \"V23\": -0.13745808,
    \"V24\": 0.141266984,
    \"V25\": -0.206009588,
    \"V26\": 0.502292224,
    \"V27\": 0.21942223,
    \"V28\": 0.215153147,
    \"Amount\": 30.0
    }"

    
Note: Replace <localhost address> with http://127.0.0.1:8000 or your server's address if different.

## Model Performance (RandomForest Classifier)

 Recall: 0.89

Precision: 1.0

AUC: 0.94

