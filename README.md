ReadMe File

Performance Analysis: VirtualBox VM vs GCP VM
This project compares the performance of two virtual environments:
1. VirtualBox VM: A local virtual machine running on VirtualBox.
2. GCP VM: A virtual machine hosted on Google Cloud Platform.

Test Environment Setup

 VirtualBox VM:
•	Host Machine: Your local computer (Windows).
•	VM Software: VirtualBox
•	Operating System: Ubuntu 20.04 (Linux).
•	Hardware Allocation: 
  -	CPU: 2 cores
  -	RAM: 4GB
  -	Disk: 20GB

 GCP VM:
•	Cloud Provider: Google Cloud Platform
•	Instance Type: e2-standard-2 (2 vCPUs, 4 GB memory)
•	Operating System: Ubuntu 20.04
  

The Application Details that we have run IN both VirtualBox VM and Cloud VM (GCP)
This project predicts customer churn for a telecommunications company using machine learning models. The goal is to build a predictive model that helps identify which customers are at risk of leaving the company. The project includes a web app built with Streamlit for live churn prediction and a Jupyter notebook detailing the model development process.
  
Initial Model Building:
•	ML_Project_IITJ.ipynb: This Jupyter notebook contains the machine learning workflow.
•	Imports necessary libraries for data manipulation and machine learning.
•	Loads and preprocesses the `telecommunications_churn.csv` dataset.
•	Trains several machine learning models, including Logistic Regression, Random Forest, and XGBoost.
•	Evaluates models using metrics such as accuracy, precision, recall, and AUC-ROC scores.
•	Provides visualizations and insights from the dataset.

Deployment:
•	ML_IIT.py: This Python script is the main file for deploying the churn prediction model as a web application using Streamlit.
•	Collects user inputs via a sidebar in the app.
•	Loads a pre-trained machine learning model to make predictions on customer churn.
•	Display results interactively in the app.
