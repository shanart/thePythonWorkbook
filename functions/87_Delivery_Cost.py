# Интернет-магазин предоставляет услугу экспресс-доставки для части
# своих товаров по цене $10,95 за первый товар в заказе и $2,95 – за все
# последующие. Напишите функцию, принимающую в качестве единствен-
# ного параметра количество товаров в заказе и возвращающую общую
# сумму доставки. В основной программе должны производиться запрос
# количест­ва позиций в заказе у пользователя и отображаться на экране
# сумма доставки.

# Settings
FIRST_PROD = 10.95
PROD = 2.95


def delivery_cost(product_count: int) -> float:
    """
    Calculate delivery cost depends of number of products
    :param product_count: the number of products in delivery
    :return: Delivery coast
    """
    total_price = 0.0
    for p in range(product_count):
        total_price += FIRST_PROD if p == 0 else PROD

    return round(total_price, 2)


if __name__ == '__main__':
    count = int(input("Enter product count: "))
    print('Delivery price: $' + str(delivery_cost(count)))
