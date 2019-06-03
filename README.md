# Introduction 

The main goal of the Post Classification Service is to automatically classify the posts of different brands into pre-trained topics.  

# Getting Started
In these project we worked with [Anaconda Distribution](https://www.anaconda.com/distribution/) Python 3.7, these allow us to perform Python/R data science and machine learning on Linux, Windows, and Mac OS X. It is the industry standard for developing, testing, and training on a single machine, enabling  _individual data scientists_  to:

-   Quickly download 1,500+ Python/R data science packages
-   Manage libraries, dependencies, and environments with  Conda
-   Develop and train machine learning and deep learning models 
-   Analyze data with scalability and performance 
-   Visualize results 

[Installation Guide](https://docs.anaconda.com/anaconda/install/)

### Configuring the Development Environment

To set up the development environment first we need to open the **Anaconda Prompt**. Configure a virtual environment with the Azure ML SDK. Run the below commands to install the Python SDK, and launching a Jupyter Notebook. Start a new Python 3 kernel from Jupyter.

    conda create  -n  aml  -y  Python=3.6
    
    conda activate aml
    
    conda install nb_conda
    
    pip install azureml-sdk[notebooks]
    
    pip install sklearn
    
    jupyter notebook


# Description of the Notebooks

 1. **Extractor.ipynb**: This notebook extract the post from the MongoDB and convert to a CSV file.
 2. **MLmodel.ipynb**: This notebook works with the CSV file to create the machine learning models and save it as a Pickle files ".pkl".
 3. **Deployment.ipynb**: This notebook is used to deploy the models as a RESTful web service using Azure ML workpace.


# Build and Test


# Contribute
TODO: Explain how other users and developers can contribute to make your code better. 

If you want to learn more about creating good readme files then refer the following [guidelines](https://docs.microsoft.com/en-us/azure/devops/repos/git/create-a-readme?view=azure-devops). You can also seek inspiration from the below readme files:
- [ASP.NET Core](https://github.com/aspnet/Home)
- [Visual Studio Code](https://github.com/Microsoft/vscode)
- [Chakra Core](https://github.com/Microsoft/ChakraCore)