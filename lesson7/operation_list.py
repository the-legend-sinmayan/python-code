lst = ['apple', 'banana', 'cherry','orange', 'kiwi', 'melon', 'mango', 'grape', 'strawberry', 'blueberry', 'raspberry', 'blackberry', 'pear', 'peach', 'plum', 'pineapple', 'coconut', 'avocado', 'papaya', 'fig', 'date', 'guava', 'lychee', 'passionfruit', 'dragonfruit', 'starfruit', 'watermelon', 'canteloupe', 'honeydew', 'grapefruit', 'lemon']

lst.append('tangerine')
print("updated list:", lst  )

lst.remove('banana')
print("updated list:", lst  )

lst.sort()
print("sorted list:", lst  )

lst.pop(1)
print("updated list:", lst  )
lst.reverse()
print("reversed list:", lst  )
print("multiiplication on list:", lst * 2  )

lst = lst[:4   ]
print("sliced list:", lst  )

lst.clear()
print("updated list:", lst  )