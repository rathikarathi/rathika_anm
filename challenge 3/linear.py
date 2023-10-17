#Write a function called linear_search_product that takes the list of products 
def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)
  return indices
products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
target2 = 'apple'
result = linearSearchProduct(products, target)
print(result)
