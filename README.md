# 동아리 서비스
DGIST 동아리 활동 관리 서비스
## Before Installation

#### Docker로 MySQL을 설치해야 함

```
$ docker pull mysql
```

#### MySQL 세팅 방법

```
$ docker run -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=password mysql
$ docker exec -it mysql bash
bash-4.4# mysql -u root -p
Enter password:
mysql> CREATE DATABASE club;
```

#### docker로 MySQL가 컨테이너로 실행 중이어야 서버가 작동함

## Installation

1. Python 설치 (3.10.2)\
   https://www.python.org/downloads/ 에서 OS에 맞게 설치
2. Python 가상환경 설정\
   https://dojang.io/mod/page/view.php?id=2470 을 참고\
   python 3.10.2 을 사용하는 가상환경을 만들어야 함
3. 설정한 가상환경에 접속 후, 터미널에서 프로젝트 루트로 이동
4. pip로 requirements 설치
   ```
   $ pip install -r requirements.txt
   ```
5. 서버 실행
   ```
   $ python manage.py migrate
   $ python manage.py runserver
   ```
6. http://127.0.0.1:8000/ 에서 동아리 서비스 사용 가능
