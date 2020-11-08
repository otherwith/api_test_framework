import pymysql
from config.config import *


# 获取连接方法
def get_db_conn():
    conn = pymysql.connect(host=db_host,  # 从配置文件中读取
                           port=db_port,
                           user=db_user,
                           passwd=db_passwd,  # passwd 不是 password
                           db=db,
                           charset='utf8')  # 如果查询有中文，需要指定测试集编码
    return conn


# 封装数据库查询操作
def query_db(sql):
    conn = get_db_conn()
    cur = conn.cursor()
    logging.debug(sql)  # 输出执行的sql
    cur.execute(sql)
    conn.commit()
    result = cur.fetchall()
    logging.debug(result)  # 输出查询结果
    cur.close()
    conn.close()
    return result


# 封装更改数据库操作
def change_db(sql):
    conn = get_db_conn()
    cur = conn.cursor()
    logging.debug(sql)  # 输出执行的sql
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        logging.error(str(e))  # 输出错误信息
    finally:
        cur.close()
        conn.close()


# 封装常用数据库操作
def check_user(name):
    # 注意sql中''号嵌套的问题
    sql = "select * from user where name = '{}'".format(name)
    result = query_db(sql)
    return True if result else False


def add_user(name, password):
    sql = "insert into user (name, passwd) values ('{}','{}')".format(name, password)
    change_db(sql)


def del_user(name):
    sql = "delete from user where name='{}'".format(name)
    change_db(sql)
