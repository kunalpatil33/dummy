product = {
    101:{
        "productname":"car",
        "price":"10000",
        "color":"black",
    }
}
print(product[101]["color"])

#key
for v in product.values():
    for k,v in v.items():
        print(k,v)
