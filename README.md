# Data Science ML Boilerplate.
    

Starting a new Data Science / ML project from the scratch  .


#### Linting 

1. Run linting for whole project  ```pylint src/* --report yes```
2. Disable linting for a specific line , example
    ```
    import config.logging_settings # pylint: disable=unused-import

    OR 

    global VAR # pylint: disable=global-statement

    OR 

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




