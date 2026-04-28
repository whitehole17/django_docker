import pymysql

pymysql.version_info = (2, 2, 8, "final", 0) # Django가 요구하는 최신 버전인 것처럼 속이기 위해 버전 정보를 수동으로 설정합니다.
pymysql.install_as_MySQLdb()                   # Django야, MySQLdb 모듈을 찾을 때 대신 PyMySQL을 사용해줘