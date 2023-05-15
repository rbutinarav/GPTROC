# GPTROC

GPTROC is a user-friendly app designed to generate datasets on any topic using OpenAI GPT models, suggest classes, train GPT-based classifier models, and evaluate their performance using ROC curve metrics. The app aims to help users find the most suitable GPT-based classification model for their data while understanding the trade-off between training sample size and model performance.

## Features

- Generate a dataset based on any topic using OpenAI GPT models
- Suggest classes for the classification task using clustering, topic modeling, or other unsupervised learning techniques
- Split the dataset into training and test sets using user-defined ratios or a fixed number of samples
- Train GPT-based classifier models for the selected classification task
- Specify the number of items used for training the classifiers
- Train and evaluate the selected GPT-based classifiers using confusion matrices, ROC curves, and AUC values
- Compare the performance of different classifiers and training sample sizes
- Interactive user interface powered by Streamlit

## Installation

1. Clone the repository:

git clone https://github.com/yourusername/GPTROC.git

2. Create a virtual environment and activate it:

python3 -m venv venv
source venv/bin/activate

3. Install required packages:

pip install -r requirements.txt


## Usage

1. Run the Streamlit app:

streamlit run main.py

2. Open the provided URL in your browser to access the interactive interface.

3. Input a topic, select classifiers, define training sample sizes, and view the performance metrics and plots.

## Dependencies

- Python 3.10
- OpenAI (for GPT models)
- Streamlit (for the user interface)



