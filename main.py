from shapes import area, perimeter

if __name__ == "__main__":
    string1 = "food"
    string2 = "Leah"
    string3 = string1 + "loves" + string2
    print(string3)
    string4 = "{} loves {}".format(string1, string2)
    print(string4)
    string5 = f"{string1} loves {string2}"
    print(string5)
    result = area(4, 5)
    print(f"Result is {result}")
