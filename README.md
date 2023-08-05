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

4. Local Setup

# Local Project Setup

So, to set this project in local we have couple of steps needed. 

1. Environment creation
2. Mongodb Account setting
3. Environment variable settings
4. Aws configure 





## Environment creation

In this part, we will see how to create a conda environment. 

## Create a new Conda environment

Go to your project folder and open vscode/terminal there. To create a new Conda environment for this particular project, use the following command:

```bash
conda create --prefix ./env python=3.8
```

To activate the environment 
```bash
conda activate ./env 
```
if the environment activation code gives error, try this one 
```bash
source activate ./env
```
## MongoDb account setting

MongoDB is a popular NoSQL database that allows you to store and retrieve data in a flexible and scalable way. In this guide, we will go through the steps of creating a MongoDB account, database, and how to get the Python 3.8 client URL for MongoDB.

### Step 1: Create a MongoDB account

**To create a MongoDB account, follow these steps:**

1. Go to the MongoDB website and click on the "Sign Up" button.

2. Fill in the required details such as your name, email address, and password.

3. Verify your email address by clicking on the link sent to your email.

4. Once you have verified your email address, log in to your MongoDB account.

## Step 2: Create a MongoDB database

**To create a MongoDB database, follow these steps:**

1. Click on the "Create a Cluster" button on the MongoDB Atlas dashboard.

2. Choose the free plan by selecting the "Shared" option.

3. Choose your preferred cloud provider, region, and cluster name.

4. Click on the "Create Cluster" button.

5. Once the cluster is created, click on the "Collections" button to create a new collection in the database.

## Step 3: Get the Python 3.8 client URL

To get the Python 3.8 client URL for MongoDB, follow these steps:

1. Click on the "Connect" button on the MongoDB Atlas dashboard.

2. Select "Connect your Application".

3. Choose your preferred programming language ( for us python), version ( for us 3.6 or above), and driver.

4. Copy the Python 3.8 client URL provided.

5. Use the client URL to connect to your MongoDB database in Python.

## Step 4: Create s3 Bucket in AWS s3

1. Navigate to the S3 service in aws.
2. Click on the "Create bucket" button on the S3 dashboard.
3. In the "Create bucket" dialog, provide a unique name for your bucket. For our project, keep it `sensor-deployment` as we have mentioned this particular name for our project in our constant module. If you wanna give another name make sure you mention it inside the constant module.
4. Click on the "Create bucket" button to create your S3 bucket.


## Environment variable setting

**To set environment variables in Windows for AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and MONGO_DB_URL, you can follow these steps:**

- Open the Start menu and search for **Environment Variables**

- Click on **Edit the system environment variables**

Click on the **Environment Variables** button.

Under the **User variables** or **System variables** section, click **New**.

In the **Variable name** field, enter the name of the environment variable you want to set (e.g., AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, MONGO_DB_URL).

In the "Variable value" field, enter the corresponding value for the environment variable.

Click "OK" to save the environment variable.

**Note:**
- You will get *How to get the aws credentials* in the deployment documentation. 

**To set the environment variables in linux, use the following method to add any environment variable.

**AWS secret access key**
```bash
export AWS_ACCESS_KEY_ID=<your-access-key-id>
```

**AWS other credentials**
```bash
export AWS_SECRET_ACCESS_KEY=<your-secret-access-key>
```

**MongoDB URL**
```bash
export MONGO_DB_URL=<your-mongodb-client-url>
```
## Aws configure 

- [Install Aws Cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) Depending on your **Os**.

**Configure AWS cli**

Run the following command in your pc terminal
```bash
aws configure
```
This will prompt you the aws credentials. 

    # Enter your AWS Access Key ID and Secret Access Key
    # Enter your Default region name (set it as ap-south-1 or wherever your s3, ec2 and ecr are present)
    # Enter your Default output format (e.g. json)

## Final Project Run

Once you have successfully completed the steps above, 
- Install the **requirements.txt** by running the following command 

To activate the environment
```bash
source activate ./env 
```
To install the dependencies
```bash
pip install -r requirements.txt
```

Once you are done with the libraries installation, 
Run
```bash
python app.py
```

Open your browser and hit the url belor

- [https://localhost:5000](https://localhost:5000)

The project should run now in your local pc. 


5. Project Deployment

# Sensor Fault Detection Project Deployment

To deploy our project to Aws Ec2 we have some steps which are following:

- Create DockerFile and test by building docker image locally.
- Create Github Actions YAML config file
- Set up github repository secrets 
- Create an AWS EC2 ubuntu machine 
- Install docker and AWS cli in ec2 machine
- Set up self-hosted runner in EC2 
- Create an ECR repository in aws 



 
# ![Docker](https://skillicons.dev/icons?i=docker) Create DockerFile and test by building docker image locally.

- Let's check our DockerFile that we've created for our project.
```docker
FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD [ "python3","app.py" ]

```
So our base image is `python:3.8-slim-buster` and our work directory is `app.py` as this is the module where our FastApi app code is written. We are installing the requirements from the requirements.txt and atlast we are giving a command to run the app. That's all about the dockerfile that we have created for this particular project.

## Create Github Actions YAML config file

### Continuous Integration and Continuous Deployment Workflow

```YAMl

name: workflow

on:
  push:
    branches:
      - main
    paths-ignore:
      - 'README.md'

permissions:
  id-token: write
  contents: read

jobs:
  integration:
    name: Continuous Integration
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Lint code
        run: echo "Linting repository"

      - name: Run unit tests
        run: echo "Running unit tests"

  build-and-push-ecr-image:
    name: Continuous Delivery
    needs: integration
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Install Utilities
        run: |
          sudo apt-get update
          sudo apt-get install -y jq unzip
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ secrets.AWS_DEFAULT_REGION }}

      - name: Login to Amazon ECR
        id: login-ecr
        uses: aws-actions/amazon-ecr-login@v1

      - name: Build, tag, and push image to Amazon ECR
        id: build-image
        env:
          IMAGE_TAG: latest
        run: |
          # Build a docker container and
          # push it to ECR so that it can
          # be deployed to ECS.
          docker build -t ${{ secrets.AWS_ECR_REPO_URI }}:$IMAGE_TAG .
          docker push ${{ secrets.AWS_ECR_REPO_URI }}:$IMAGE_TAG
          
          
  Continuous-Deployment:
    needs: build-and-push-ecr-image
    runs-on: self-hosted
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ secrets.AWS_DEFAULT_REGION }}

      - name: Login to Amazon ECR
        id: login-ecr
        uses: aws-actions/amazon-ecr-login@v1
      
      
      - name: Pull latest images
        run: |
         docker pull ${{ secrets.AWS_ECR_REPO_URI }}:latest
         
                
      # - name: Stop and remove visibility container if running
      #   run: |
      #    docker ps -q --filter "name=visibility" | grep -q . && docker stop visibility && docker rm -fv visibility
      - name: Run Docker Image to serve users
        run: |
         docker run -d -p 8080:8080 --name=sensor -e 'MONGO_DB_URL=${{ secrets.MONGO_DB_URL }}' -e 'AWS_ACCESS_KEY_ID=${{ secrets.AWS_ACCESS_KEY_ID }}' -e 'AWS_SECRET_ACCESS_KEY=${{ secrets.AWS_SECRET_ACCESS_KEY }}' -e 'AWS_DEFAULT_REGION=${{ secrets.AWS_DEFAULT_REGION }}' ${{ secrets.AWS_ECR_REPO_URI }}:latest

      - name: Clean previous images and containers
        run: |
         docker system prune -f

```
This is a GitHub Actions workflow written in YAML for continuous integration (CI) and continuous deployment (CD) of a software project.

The workflow is triggered by a push to the main branch, and it consists of three jobs:

**The integration** job runs on an Ubuntu virtual machine and checks out the code from the repository. It then runs a linter on the code and executes unit tests.

**The build-and-push-ecr-image** job also runs on an Ubuntu virtual machine and depends on the integration job. It installs some utilities and configures AWS credentials to access Amazon Elastic Container Registry (ECR). It then logs in to ECR and builds a Docker image of the project using the latest tag. Finally, it pushes the image to ECR.

**The Continuous-Deployment** job runs on a self-hosted machine and depends on the build-and-push-ecr-image job. It checks out the code from the repository and configures AWS credentials to access ECR. It then pulls the latest Docker image from ECR and runs it as a container on the machine, passing some environment variables to it. Finally, it cleans up any previous images and containers.

To use this workflow, you can copy the YAML code to a .yml file in your repository's .github/workflows directory. You also need to configure some secrets in your repository settings to authenticate with AWS and ECR.

For more information on using GitHub Actions, refer to the [official documentation](https://docs.github.com/en/actions).


## ![github](https://skillicons.dev/icons?i=github) Set up github repository secrets 

### Adding Secrets in GitHub 

    1. Navigate to the repository where you want to add the secrets.
    2. Click on the "Settings" tab in the menu bar.
    3. Scroll down to the "Secrets" section and click on "New repository secret".
    4. Enter the name of the secret and its value.
    5. Click on "Add secret" to save the secret.
    6. To use the secret in your workflow, reference it using the syntax `secrets.<secret-name>`.


### Setting Up Secrets for this project

To use the GitHub Actions workflow in this repository, you need to set up several secrets in your GitHub repository. Here's how to set up the required secrets:

- `AWS_ACCESS_KEY_ID`: The access key for your AWS account.
  - To create an access key, go to your AWS Management Console and navigate to the "IAM" service.
  - Click on "Users" in the left-hand navigation menu, then click on your user.
  - Click on the "Security credentials" tab, then click on "Create access key".
  - Copy the access key ID and store it as a secret in your GitHub repository.
- `AWS_SECRET_ACCESS_KEY`: The secret access key for your AWS account.
  - To create a secret access key, follow the same steps as for the access key, but click on "Show" to reveal the secret access key.
  - Copy the secret access key and store it as a secret in your GitHub repository.
- `AWS_DEFAULT_REGION`: The default region for your AWS account.
  - This is typically set to the region closest to you.
  - You can find the region code in the AWS Management Console, in the upper-right corner of the page.
  - Store the region code as a secret in your GitHub repository.
- `AWS_ECR_REPO_URI`: The URI for your Amazon Elastic Container Registry (ECR) repository.
  - To get the URI, go to your AWS Management Console and navigate to the "ECR" service.
  - Click on your repository, then click on "View push commands" in the upper-right corner of the page.
  - Copy the "docker login" command and extract the repository URI from it.
  - Store the URI as a secret in your GitHub repository.
- `MONGO_DB_URL`: The URL for your MongoDB database.
  - This should be a connection string in the format `mongodb+srv://<username>:<password>@<cluster>/<database>`.
  - Store the URL as a secret in your GitHub repository.



## Create an AWS EC2 ubuntu machine


## Prerequisites

Before you begin, you'll need:

- An AWS account
- The AWS CLI installed on your local machine
- Docker installed on your local machine

## Creating an EC2 Instance

1. Log in to the [AWS Management Console](https://aws.amazon.com/console/).

2. Navigate to the EC2 dashboard.

3. Click on the "Launch Instance" button.

4. Choose an Amazon Machine Image (AMI) and instance type. For example, you have to choose the Ubuntu 22.04 AMI and t2.medium instance type for this project.

5. Configure the instance details, such as the number of instances, network settings, and storage.

6. Add any additional storage or tags, if necessary.

7. Configure the security group to allow incoming traffic. For example, you could allow HTTP and HTTPS traffic.

8. Launch the instance and save the private key for SSH access.

## Installing Docker in EC2 machine

1. SSH into the EC2 instance using the private key.

2. Update the package index and install the required dependencies:

```bash
sudo yum update -y
sudo yum install -y docker
```
3. Grant root access to docker
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```
4. Start the Docker service and enable it to start on boot:
```bash
sudo service docker start
sudo chkconfig docker on

```


## Installing AWS CLI in EC2 machine

1. SSH into the EC2 instance using the private key.

2. Download and install the AWS CLI:

```bash
sudo curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo unzip awscliv2.zip
sudo ./aws/install
```

3. Verify the installation by running the following command:
```bash
aws --version
```


You're now ready to use the EC2 instance with Docker and AWS CLI.

4. Configure AWS cli

```bash
aws configure
```
    # Enter your AWS Access Key ID and Secret Access Key
    # Enter your Default region name (e.g. ap-south-1)
    # Enter your Default output format (e.g. json)

Once you configure aws cli, setup the Ec2 as self-hosted runner on which our project is basically going to be deployed. 

### Here are the steps to get the code required to add a self-hosted runner to your GitHub repository:

- Go to your GitHub repository and click on the `Settings` tab.

- On the left-hand side, click on `Actions` and then click on `Runners`.

- Click on `New self-hosted runner` and choose a machine. For us we are going to use the **Linux** machine. Once you choose the linux machine, below that you will get a code snippet. That you have to copy and paste one by one in the EC2 machine console. Once you do that properly, you would see the name self-hosted available in your runners list in your github **repository > settings > Actions > Runners page**

Follow the prompts to configure the runner. You'll be asked to provide a name for the runner, and to download a token to authenticate the runner with your repository.

Once you've completed the configuration, you'll be presented with a code snippet that you need to run on your self-hosted runner instance. The code will look something like this. And now if you've reached till this part, you have successfully setup the EC2 machine. 


## Create a ECR repo in aws 

1. Open the `AWS Management Console` and navigate to the `Amazon ECR service`.
2. Click the `Create repository` button.
3. In the `Create repository` page, enter a name for your repository in the `Repository name` field.
4. (Optional) Add tags to your repository in the `Tags` section.
5. Click the `Create repository` button to create your ECR repository.

copy the ECR repo url and add into github secrets.


## Final deployment

Now when you have successfully completed the steps above, push your code to your github repository and click on the `Actions` in your github repository. You can see a `workflow` running there. If you have done the previous steps just the way it was demonstrated, the project will be deployed.

🔧 Built with
- flask (For Api Creation)
- Python 3.8 (Core Language)
- Machine learning 
- Scikit learn (ML Library)
- SQL (For Database)
- numpy
- Pandas

# ScreenShots


<h2 align="center">⛩ Training

 
 
![image](https://github.com/shafingit1234/Wafer-Fault-Detection-Project/blob/main/images/Training.png)
<h2>

<h2 align="center">⛩ Uploading Test.csv File

 
 
![image](https://github.com/shafingit1234/Wafer-Fault-Detection-Project/blob/main/images/Uploading.png)
<h2>


<h2 align="center">⛩ Result

 
 
![image](https://github.com/shafingit1234/Wafer-Fault-Detection-Project/blob/main/images/Result.png)
<h2>

