# Data Science ML Boilerplate.
    

Starting a new Data Science / ML project from the scratch  .

#### Virtual environment creation [ using built-in venv ]

1. Run ```python -m venv --prompt <promt> .env``` 
2. Check project root directory, it should have ```.env``` directory
3. Activate virtual environment 
    - For Windows  ```.env\Scripts\activate.bat```
    - For Linux  ```source .env/bin/activate```
4. Check new python interpreter path    
    - For Windows  ```where python```
    - For Linux  ```which python```
    - It should point ```${Project_root}/.env/Scripts/python```
5. install dependency using ```pip install <package_name>```

#### Jupyter Installation [Optional]

Installation can be done ```pip install Jupyter```. However big list dependency og Jupyter can be avoided by installting ipython kernel module only.

1. ```pip install ipykernel```
2. ```python -m ipykernel install --user --name=<promt>```
3. You should now be able to see your kernel in the IPython notebook menu: Kernel -> Change kernel
    ![ipython-kernel](./ipythonkernel.png)

4. To Remove the kernel in case of uninstallation.
    - ```jupyter kernelspec list``` this list down all installed kernal.
    - ```jupyter kernelspec uninstall unwanted-kernel``` removes the kernal.  


#### Linting [ using pylint ]

1. Run linting for whole project  ```pylint src/* --report yes```
2. Disable linting for a specific line , example
    ```
    import config.logging_settings # pylint: disable=unused-import
    ```
    OR 
    ```
    global VAR # pylint: disable=global-statement
    ```
    OR 
    ```
    def test():
        # Disable all the no-member violations in this function
        # pylint: disable=no-member
        ...
    ```

#### Cleaning file cache files [__pycache__ ]

Run ``` pyclean . -v```

#### Code Formating

Run ```black . -v```

#### Run jupyter notebook from remote shell

1. First Run ```jupyter notebook``` from project directory of remote server.
2. Notedown the port number .
3. Finally run the following commands from local meachine
    ```ssh -L 8888:localhost:<remote_port> <remote_user_name>@<remote_ip>```
5. Point the browser at ```localhost:8888```    




 