from datetime import datetime

def add_income(data):
    amount = float(input("Enter income amount: "))
    source = input("Enter source: ")
    data.append({
        "type": "Income",
        "amount": amount,
        "category": source,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

