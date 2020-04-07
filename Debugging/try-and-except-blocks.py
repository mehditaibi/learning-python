try:
    foobar  # try this code
except NameError as err:
    print(err)  # if error, raise this


d = {"name": "Ricky"}
d["city"]


def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None

# try:
#     num = int(input("Please enter a number: "))
# except:
#     print("this is not a number!")
# else:
#     print("There was no error!")
# finally:
#     print("Runs no matter what..")


while True:
    try:
        num = int(input("Please enter a number: "))
    except ValueError:
        print("this is not a number!")
    else:
        print("There was no error!")
        break
    finally:
        print("Runs no matter what..")
