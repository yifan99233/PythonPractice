from redis import StrictRedis

sr = StrictRedis(host='172.16.1.54',decode_responses=True)

_data = sr.lrange('mylist',0,-1)
print(_data)