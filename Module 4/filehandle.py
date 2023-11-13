try:
    file = open("myfile.txt",'w')
    try:
        lines = file.readlines()
    #if we cannot read from the file
    except:
        print("Error with read/write")
    finally:
         file.close()

#If the file does not open
except:
    print("Error opening file")


### To play in MA4 (division) your rating must be <= 850

class InvalidRatingException(Exception):
    pass
ma4 = 850
def register(rating,division):
    if rating > division:
        raise InvalidRatingException
    else:
        print(f"You are now registered for ma4 with rating {rating}")
try:
    user_rating = int(input("Enter your rating: "))
    register(user_rating,ma4)
except InvalidRatingException:
    print("Can not register for ma4")


import csv
with open("mycsv.csv","r") as file:
    data = csv.DictReader(file)
    for row in data:
        print(row)