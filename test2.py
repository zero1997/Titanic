from pandas import DataFrame



df = DataFrame({'key1':['a','a','b','b','a','a'],
                'key2':['one','two','one','two','one','one'],
                'data1':[1,2,3,2,1,1],
                # 'data2':np.random.randn(5)
                })

print(df)

a=df.groupby(['key1','key2']).size().reset_index()
print(a)

dup=df[df.duplicated()].count()

print(dup)