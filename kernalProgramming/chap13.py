# -*- coding: utf-8 -*-

class Foo(object):
    version = 0.1
    
    def __init__(self, nam):
        # self.f = nam
        self.name = nam
        # print self.__name

    def mk(self):
        print "lulei"
    
    def __showMe(self):
        # print(self.name)
        # print(self.__class__.__name__)
        self.mk()
    
    def showVersion(self):
        print(self.version)
        self.__showMe()

class QueryData(Foo):

    def __init__(self, nam, context):
      
        Foo.__init__(self, nam)
        self.__name = nam
        print self.name
        self.context = context
        print self.context
        # self.__other_name = nam

    # def __showMe(self):
    #     print("good")
    # def mk(self):
    #     print "psj"


    def get_sql(self):

        sql = "select %s from" % (self.context) 
        self.showVersion()
        # self.__showMe()

        return sql

    @staticmethod
    def read(va):
        print va

    def get_result(self):

        sql = self.get_sql()
        
        df_res = sql

        return df_res

z = QueryData("context", "lulei")
# z.get_sql()
# z.read("vas")
# z.showVersion()
# QueryData.read("vas")
# print QueryData.version
# print z.name, z.context, z.__other_name

        
# f = Foo("love")
# f._showMe()
# f.showVersion()

# z = QueryData("this")
# print z.__class__.__name__
# .get_result()