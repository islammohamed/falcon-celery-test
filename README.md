# falcon-celery-test
1. Install redis and run the server
2. create venv in any directory
  ```
  $ virtualenv myvenv
  $ source myvenv/bin/activate
  ```

3. Install the required libraries
  ```
  pip install -r requirements.txt
  ```

4. run  gunicorn workers
  ```
  gunicorn app:api --workers 4
  ```

if you want to do benchmarking, you can use boom or ab
  ``` 
  ab -c 10 -n 10000 http://127.0.0.1:8000
  ```

you could test the benchmarking while consuming the messages by running  the following commands
  ```
  celery -A resources.tasks worker --loglevel=info
  ```
