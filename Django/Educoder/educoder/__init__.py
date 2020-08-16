import pymysql

pymysql.version_info = (1, 3, 13, "final", 0)  # 这主要是django 内部的一个版本限制在作怪
pymysql.install_as_MySQLdb()
