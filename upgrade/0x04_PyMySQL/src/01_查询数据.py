import pymysql

# 创建连接对象
conn = pymysql.connect(host='172.16.1.54', port=3306, user='root', password='mysql',database='python39', charset='utf8')

# 获取游标对象
cursor = conn.cursor()

# 查询 SQL 语句
sql = "select * from students;"
# 执行 SQL 语句 返回值就是 SQL 语句在执行过程中影响的行数
row_count = cursor.execute(sql)
print("SQL 语句执行影响的行数%d" % row_count)

# 取出结果集中一行数据,　例如:(1, '张三')
# print(cursor.fetchone())

# 取出结果集中的所有数据, 例如:((1, '张三'), (2, '李四'), (3, '王五'))
for line in cursor.fetchall():
    print(line)

# 关闭游标
cursor.close()

# 关闭连接
conn.close()