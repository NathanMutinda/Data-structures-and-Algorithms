def swap(a, b, arr):
    if a is not b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp


def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    start = pivot_index + 1
    end = len(elements) - 1

    while start < end:

        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end


def quick_sort(elements, start, end):
    if start < end:
        p1 = partition(elements, start, end)
        quick_sort(elements, start, p1 - 1)
        quick_sort(elements, p1 + 1, end)


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]

    quick_sort(elements, 0, len(elements) - 1)

    print(elements)

