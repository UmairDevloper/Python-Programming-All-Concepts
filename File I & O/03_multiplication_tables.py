
def multiplication_tables(n):
     table = ""
     for i in range (1, 11):
          table += f"{n} x {i} = {n * i}\n"
     with open(f"tables/table{n}.txt", "w") as f:
          f.write(table)
       

def table_of():
     for i in range (1, 11):
          multiplication_tables(i)

table_of()