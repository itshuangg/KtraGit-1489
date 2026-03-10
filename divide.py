#divide a,b
def divide(a,b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a/b
if __name__ == "__main__":
    a = 10
    b = 5
    print("The division of a by b is:", divide(a,b))