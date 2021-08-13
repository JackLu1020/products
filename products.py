
products = []
while True:
	name = input('please enter the product: ')
	if name == 'q':
		break

	price = input('pleae enter the price: ')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
    #     以上9~12可以寫成如下：
    #      1.
    #      p = [name,price]
    #      products.append(p)
    #      2.
    #      products.append([name,price])


print(products)