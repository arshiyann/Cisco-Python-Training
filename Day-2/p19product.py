
file = open('Product_Info.log','a')

product_info = {'prodID':[],'prodName':[],'salesCount':[]}

i =0 
while i<2:
    pr_id = input('Enter Product ID: ')
    pr_name = input('Enter Product Name: ')
    pr_sales = input('Enter Product Sales Count: ')
    
    file.write(pr_id+","+pr_name+","+pr_sales+"\n")
    i+=1
