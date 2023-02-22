from datetime import datetime
from datetime import timedelta

def create_subscription(expiry_date,months_to_buy,monthly_cost):
    if(months_to_buy==1):
        new_date = datetime.strptime(expiry_date,"%d/%m/%Y")
        Enddate = new_date + timedelta(days=26)
        new_expiry = Enddate.strftime("%d/%m/%Y")
        cost = round((26)*(monthly_cost/30),2)
    else:
        new_date = datetime.strptime(expiry_date,"%d/%m/%Y")
        Enddate = new_date + timedelta(days=29+(months_to_buy-1)*30)
        new_expiry = Enddate.strftime("%d/%m/%Y")
        cost = round(((Enddate-new_date).days)*(monthly_cost/30),2)
    return(new_expiry,cost);
values = create_subscription("19/06/2022",1,1000)
print(values)
