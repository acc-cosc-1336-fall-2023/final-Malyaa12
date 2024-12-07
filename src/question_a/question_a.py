#write functions here, don't add input('') statements here!
def test_config():
    return True

def create_multiplication_table():
    table = []
    for i in range(1, 11):
        row = [i * j for j in range(1, 11)]
        table.append(row)
    return table

def display_multiplication_table(table):
    for row in table:
        print("\t".join(map(str, row)))
