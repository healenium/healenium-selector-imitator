# Healenium selector imitator

Selector imitator tries to reconstruct a user selector, changing only fields that the user modified in HTML. It works with the original selector (and its type) and target node (so it should be applied after the best node is already found). It proposes possible healed selectors or raises an error.  
Proposed selectors are not guaranteed to find a unique web element. Uniqueness must be checked outside of the service with a selenium driver.  

1. [Example request and response](#example)
2. [Image and container resources consumption](#resources)
3. [Installation with Docker](#installation)
4. [Local testing](#testing)

### <a name="example">Example request and response</a>

Here is an example request. You can try out different requests with Swagger after the [installation](#installation).

![image](https://user-images.githubusercontent.com/40484210/123597816-7b949e80-d7fc-11eb-96b9-b7931ddee89b.png)  
![image](https://user-images.githubusercontent.com/40484210/123597848-83ecd980-d7fc-11eb-8a5b-4904939834b5.png)


### <a name="resources">Image and container resources consumption</a>
![image](https://user-images.githubusercontent.com/40484210/123598005-b7c7ff00-d7fc-11eb-9be6-fa20c181bb47.png)  
![image](https://user-images.githubusercontent.com/40484210/123598058-c3b3c100-d7fc-11eb-85d9-380bacd53d6a.png)


### <a name="installation">Installation with Docker</a>
Run these commands from the repository directory (you'll need docker and pyarmor installed):
```
pyarmor obfuscate --platform linux.x86_64.7 --recursive --output dist/src src/__init__.py
pyarmor obfuscate --platform linux.x86_64.7 --exact app.py
docker build -t hlm-selector-imitator:v1 .
docker run -d -p 8000:8000 hlm-selector-imitator:v1
```
Now you can access an API at http://localhost:8000/  
Check http://localhost:8000/docs for Swagger documentation.

### <a name="testing">Local testing</a>
To test or lint locally, create a virtual environment with Pyhton 3.7 and install packages from requirements_dev.txt  

Test with [pytest](https://docs.pytest.org/en/6.2.x/):
```
pytest
```

Get [coverage](https://coverage.readthedocs.io/en/coverage-5.5/#) report:
```
coverage run -m pytest
coverage report -m
coverage html
```

Lint with [flake8](https://flake8.pycqa.org/en/latest/):
```
flake8
```

Format code with [black](https://github.com/psf/black):
```
black .
```
