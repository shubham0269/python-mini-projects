# =========================== invertory system of complex or subway==============================


menu = {"mango":50,
     "apple":65,
     'dairymilk':20,
     "maggie":10,
     "biscuit":10,
     "tea":40,
     "faluda malai mar ke ":45,
     "iphone":150000,
     "mango sack":45,
     "musammi":50}

amount = int(input("enter your amount : "))

print(menu)
buying_products = int(input("how many product you want to buy : "))

selected_products = {}
for i in range(1,buying_products+1):
     item = input("enter your buying product : ").lower().strip()
     item_qun = int(input("enter your quantity : "))
     if item not in menu.keys():
          print("this item is not available ") 
          print("please place the  order from the above products ")  
          for j in range(i,buying_products+1):
               item = input("enter your buying product : ").lower().strip()
               item_qun = int(input("enter your quantity : "))   
                    
     else:
          selected_products[item] = item_qun

more = input("do you want to add more (y/n) : ").lower()

if more == "y":
     buying_p = int(input("how many products do you want to buy : "))
     for items in range(buying_p):
          item = input("item : ")
          item_qun = int(input("quentity : "))
          selected_products[item] = item_qun
       


sum = 0   
print("products you are buying : ",selected_products)
for k1,v1 in selected_products.items():
     total = 0 
     total = total + selected_products[k1]*v1
     print(k1,":",total)
     sum = sum + selected_products[k1]*v1
print("total amount is : ",sum)
print('rest amount in card : ',amount - sum)