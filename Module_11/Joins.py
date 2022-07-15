import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="winery_employee",
  password="Goomba99j#",
  database="winery"
)







def printTable(results,cursor):
    """Prints table in MySQL format"""
    #source: https://stackoverflow.com/a/20383011
    widths = []
    columns = []
    tavnit = '|'
    separator = '+' 

    for column,cd in enumerate(cursor.description):
        width = len(cd[0])
        for rowNumber in range(len(response)):
            if len(str(response[rowNumber][column])) > width:
                width = len(str(response[rowNumber][column]))
        widths.append(width)
        columns.append(cd[0])

    for w in widths:
        tavnit += " %-"+"%ss |" % (w,)
        separator += '-'*w + '--+'

    print(separator)
    print(tavnit % tuple(columns))
    print(separator)
    for row in results:
        print(tavnit % row)
    print(separator)
    print()


cursor = mydb.cursor()

cursor.execute("SELECT delivery_metrics.month, suppliers.supplier_name, delivery_metrics.expected_deliverytime, delivery_metrics.actual_deliverytime, delivery_metrics.delivery_gap  FROM delivery_metrics INNER JOIN suppliers ON suppliers.supplier_id = delivery_metrics.supplier_id ORDER BY month DESC;")

response = cursor.fetchall()
print("Delivery Gaps by Supplier")
printTable(response,cursor)