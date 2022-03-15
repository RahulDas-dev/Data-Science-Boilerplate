import os

__current_dir = os.path.dirname(os.path.abspath(__file__))

project_dir = os.path.abspath(os.path.join(__current_dir, os.pardir))

model_directory = os.path.join(project_dir, "model")

data_directory = os.path.join(project_dir, "data")
