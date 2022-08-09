This repo contains a Dockerfile, so you can execute my code though docker.

To build the Docker image, run the following command from the root of this repo:
```shell
docker build -t charniauskaya_test .
```

To check first task run the following command: 
```shell
docker run -ti charniauskaya_test python task_1.py
```

To check second task run the following command: 
```shell
docker run -ti charniauskaya_test python task_2.py
```

To check third task run the following command: 
```shell
docker run -ti charniauskaya_test python task_3.py
```

To check another version of third task run the following command: 
```shell
docker run -ti charniauskaya_test python task_3_second_version.py
```

Fourth task is .txt document
