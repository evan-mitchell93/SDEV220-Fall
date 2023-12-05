import pandas as pd

#series
s = [1,2,3]
myvar = pd.Series(s, index = ["a","b","c"])
print(myvar)
print(myvar["b"])

my_dict = {"name":"Evan","age":30,"color":"purple"}
myvar = pd.Series(my_dict, index=["name","color"])
print(myvar)

#Dataframe
my_dict = {
    "classes":["SDEV120","SDEV220","SDEV140"],
    "students":[15,10,12]
}

myvar = pd.DataFrame(my_dict,index = ["a","b","c"])
print(myvar)

#loc iloc
print(myvar.loc["a"])
print(myvar.iloc[0])

my_csv = pd.read_csv('discs.csv')
print(my_csv.head(10))
my_csv.loc[0,"In Bag"] = "N"
print(my_csv.head())
my_csv.to_csv("discs.csv",index=False)