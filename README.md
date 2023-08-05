<h1 align="center"> 📄✏ Wafer Fault Detection Project <h1>

# Brief Overview
In electronics, a **wafer** (also called a slice or substrate) is a thin slice of semiconductor, such as a crystalline silicon (c-Si), used for the fabrication of integrated circuits and, in photovoltaics, to manufacture solar cells. The wafer serves as the substrate(serves as foundation for contruction of other components) for microelectronic devices built in and upon the wafer. 

It undergoes many microfabrication processes, such as doping, ion implantation, etching, thin-film deposition of various materials, and photolithographic patterning. Finally, the individual microcircuits are separated by wafer dicing and packaged as an integrated circuit.

<h2 align="center">⛩ Architecture

 
 
![image](https://user-images.githubusercontent.com/85347886/137638160-1e2932af-e0ee-4dec-a00f-8552b06a96d0.png)
<h2>

##	Functional Architecture
<h2 align = "center">

![image](https://user-images.githubusercontent.com/85347886/137639174-37f387fb-6597-473b-877c-9261ff9522b6.png)

</h2>

 



💿 Installing
1. Environment setup.
```
conda create --prefix venv python==3.8 -y
```
## Why Do We Need ENV.
OS is a universal environment, one must not create project dependency in the universal environment as this idea may lead to overlap with other projects. We need to create isolated environment such no two projects share same resources. Such isolations are important because different projects will need different dependencies. Conda will help us in preserving os resources as an environment solely for the use of project in which that environment is active.

Anaconda on the other hand provides us with all necessary dependencies pre-installed in our environment helping in our data science projects.

```
conda activate venv/
````
2. Install Requirements and setup
```
pip install -r requirements.txt

```

## Need of setup.py File.
In any project our main logic (Code) folder can be seen as a package, which needs to be dumped in our local environment. For example, in this project src folder consists of all the logic, it can be seen as a package and to make my environment identify it as a package I need to create a setup.py file.

To execute the setup.py file use below command

```

python setup.py install
```
After executing the above command on executing pip list, we could see our src folder as a package.

3. EDA/Pipelines

My source folder src is going to contain whole lifecycle of machine learning project. Generally EDA is performed in notebook (Jupyter), but pipelines are needed when we want to deploy our application over a cloud.
Pipelines does the same Exploratory Data Analysis but in an automated fashion.

## Pipelines.
We will need to implement two types of pipelines.
1. Training Pipeline: It is composed of three components that are listed below.
    - Data Ingestion
    - Data Transformation
    - Model Trainer/Evaluator
    
2. Prediction Pipeline

## Data Ingestion
Data ingestion for machine learning refers to the process of collecting and preparing data for use in machine learning models. Ingesting data is a critical step in the machine learning pipeline, as the quality and quantity of data ingested can have a significant impact on the accuracy and effectiveness of the resulting models.
It involves steps like Data Collection and Data Cleaning.

In our project, we will store the dataset as a form of dataframe in mongodb database. Upload_data.py will do the task of uploading the wafers data into the mongodb cluster.

From there export_data_into_feature_store_file_path() method present in data_ingestion component will fetch it as a csv file, which will then be stored in the artifact folder.

The file_path of that stored csv file will be returned to the next component of our training pipeline which is Data Transformation.

## Data Transformation
Data transformation is the process of converting raw data into a a format or structure that would be more suitable for the model or algorithm and also data discovery in general. It is an essential step in the feature engineering that facilitates discovering insights.

When implementing supervised algorithms, training data and testing data need to be transformed in the same way. This is usually achieved by feeding the training dataset to building the data transformation algorithm and then apply that algorithm to the test set.

In this component first we will differentiate input and output feature and create train, test data. Since our aim is to perform automated EDA, we will create a preprocessor object applying simple imputer (constant strategy) for imputing missing values and Robust Scaler to scale the data.

Using the created preprocessor object, we will create scaled training and testing data.

Output of this component will be train_arr, test_arr and a preprocessor_path used by the next component named as Model Trainer. Also, this component will store a preprocessor pickle file in the artifacts folder for future transformation.

## Model Trainer
The ultimate goal of model training is to produce a model that predicts the value of some output feature y, given a set of input features X. Model training is the phase during which the model ‘learns’. The first step is to select an appropriate algorithm depending on the type of problem at hand.

Model training is an iterative process. It involves learning the model parameters and fine tuning the hyperparameters. Training data is used to learn the values for the model parameters while validation data is used to check the model’s performance and fine tune the hyperparameters. Since hyperparameters are set before the training, it’s best to tune them based on the performance of the model. Test data is used for evaluating the model in the evaluation phase.

Algorithms used in this components are XGBClassifier, GradientBoostingClassifier, SVC and RandomForestClassifier.

At the end of its execution, model.pkl file will be generated and stored in the artifacts that will be later used for predicting test data input by the user.

# Prediction Pipeline
Upon Completion of training pipeline, we will have model.pkl file stored in the artifacts folder and will be used for predicting the new data input by the user via /predict route.
After uploading a new test.csv file, it will be saved in prediction_artifacts folder for future reference, converted in the form of dataframe, preprocessor.pkl file will be used to transform the input features and make it ready for prediction. Finally we will use our model.pkl file to predict the output.
The predicted coloumn will be appended to the input dataframe, this final dataframe with the needed prediction will then be converted into csv file and will be given back to the user.
5. Run Application
```
python app.py
```

🔧 Built with
- flask (For Api Creation)
- Python 3.8 (Core Language)
- Machine learning 
- Scikit learn (ML Library)
- SQL (For Database)
- numpy
- Pandas
- 🏦 Industrial Use Cases