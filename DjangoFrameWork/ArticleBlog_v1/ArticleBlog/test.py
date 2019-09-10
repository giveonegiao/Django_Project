temp="""
尊敬的%s：
        我们将于%s在%s邀请你参加%s的宴会
                                        %s
"""
print(temp%("张三","五月八日","上海饭店","李四","尼古拉斯赵四"))

temp1="""
尊敬的%(yname)s：
        我们将于%(day)s在%(site)s邀请你参加%(name)s的宴会
                                        %(myname)s
"""
print(temp1%{'yname':'张三','day':'八月五日','site':'北京饭店','name':'李四','myname':'尼古拉斯赵四'})