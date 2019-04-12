from django.db import models

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey,Sequence,MetaData,Table

db_url = 'postgres://auditor:753f3abce5b2c049@10.175.121.214/pythondb?client_encoding=utf8'
# engine = create_engine(db_url,encoding='utf-8', echo=True)
engine = create_engine(db_url,encoding='utf-8')
Base=declarative_base()
md = MetaData(bind=engine) #引用MetaData

# Create your models here.
# class UserType(models.Model):
#     name = models.CharField(max_length=32)
#
# class UserInfo(models.Model):
#
#     username = models.CharField(max_length=30)
#     pwd = models.CharField(max_length=32)
#     email = models.CharField(max_length=32)
#     user_type = models.ForeignKey(UserType)

class UserTable(Base):
    __table__ = Table('django_test_userinfo', md, autoload=True)  # 自动加载表结构

class TableImaLog:
    def getTable(self,tablename):
        class TiamLog(Base):
            __table__ = Table(tablename, md, autoload=True)  # 自动加载表结构
        return TiamLog
def getUser():
    USER_LIST = []
    tableiamlog = TableImaLog()
    table = tableiamlog.getTable('django_test_userinfo')
    Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
    session = Session_class()  # 生成session实例
    ob1 = session.query(table)
    session.close()
    obj = ob1.all()
    for i in obj:
        temp = {'id': i.id, 'username': i.username, 'email': i.email, "gender": i.gender}
        USER_LIST.append(temp)
    return USER_LIST
def deleteUserById(id):
    tableiamlog = TableImaLog()
    table = tableiamlog.getTable('django_test_userinfo')
    Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
    session = Session_class()  # 生成session实例
    obj=session.query(table).filter(table.id == id).first()
    session.delete(obj)
    session.commit()
    session.close()





if __name__ == "__main__":
    tableiamlog = TableImaLog()
    table = tableiamlog.getTable('django_test_userinfo')
    Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
    session = Session_class()  # 生成session实例
    # session.query(table).filter(table.id == 1).update({"username": 'test'})
    obj=session.query(table).filter(table.id == 1).first()
    session.delete(obj)
    session.commit()
    # ob1 = session.query(table)
    # obj = ob1.all()
    #
    # for i in obj:
    #     print(i.email,i.id,i.username,i.gender)