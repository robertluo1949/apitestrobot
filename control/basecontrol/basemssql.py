#coding:utf-8
'''
title:数据库模块   control
author:Shiyunliang
date:20171204
email:shiyunliang@vcredut.com
'''

import pymssql
import time

class mssqlaction():
    def __init__(self, host, user, pwd, db):
        '''
        数据库初始化
        '''
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        '''
        数据库连接
        '''
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset="utf8", as_dict=True)
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    def ExecQuery(self, sql):
        '''
        select语句查询
        '''

        #数据库连接
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        # 查询完毕后必须关闭连接
        self.conn.close()
        return resList

    # def ExecNonQuery(self, sql):
    #     cur = self.__GetConnect()
    #     cur.execute(sql)
    #     self.conn.commit()
    #     self.conn.close()
    #     time.sleep(1)

    def ConnectNonQuery(self):
        cur = self.__GetConnect()
        return cur

    def ExecNonQuery(self, cur, sql):
        '''
        update，insert，delete语句执行
        '''
        cur.execute(sql)
        self.conn.commit()

    def CloseNonQuery(self):
        self.conn.close()