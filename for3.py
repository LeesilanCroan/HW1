phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]


def count_avg_lots(solded_lot):
    solded_items = 0
    for sold in solded_lot:
        solded_items += sold
    return (solded_items)
    

avg_phones_sold = 0
for one_model in phones:
    phones_sold = count_avg_lots(one_model['items_sold'])
    print(f'Всего продано {one_model["product"]}: {phones_sold}')
    print(f'В среднем продано {one_model["product"]} за партию: {round(phones_sold / len(one_model["items_sold"]), 2)}')
    avg_phones_sold += phones_sold
print(f'Всего продано телефонов: {avg_phones_sold}')
tottal_phones_sold = avg_phones_sold/len(phones)
print(f'в среднем продано телефонов: {tottal_phones_sold}')