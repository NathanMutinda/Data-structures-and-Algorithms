
def bubble_sort(elements):

    size = len(elements)
    for k in range(size-1):
        swapped = False
        for i in range(size-1):
            if elements[i] > elements[i+1]:
                temp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = temp
                swapped = True

        if not swapped:
            break

if __name__ == '__main__':
    elements = [5, 9, 2, 1, 67, 34, 88, 34]

    # elements = [
    #     {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
    #     {'name': 'Dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
    #     {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
    #     {'name': 'aamir', 'transaction_amount': 800, 'device': 'i-phone 8'}
    # ]

    key = 'name'

    bubble_sort(elements)
    print(elements)
