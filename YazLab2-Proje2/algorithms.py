#seçmeli sıralama (selection)
def selection_sort(nums):
    for i in range(0,len(nums)-1):
        min=i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[min]:
                min=j


        tut=nums[i]
        nums[i]=nums[min]
        nums[min]=tut

    print(nums)


dizi=[3,2,1,6,7,5]
selection_sort(dizi)
#Kabarcık sıralaması(bubble sort)

def bubble_sortt(nums):
    for i in range(0, len(nums)):
       for j in range(0, len(nums) - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
        else:
            continue
    print(nums)


dizi=[3,2,1,6,7,5]
bubble_sortt(dizi)

#Ekleme sıralaması(insertion sort)
def insertion_sort(nums):
    for i in range(1, len(nums)):
        picked_item = nums[i]


        j = i - 1

        while j >= 0 and nums[j] > picked_item:
            nums[j + 1] = nums[j]
            j -= 1


        nums[j + 1] = picked_item
    print(nums)
dizi = [3, 2, 1, 6, 7, 5]
insertion_sort(dizi)

#Birleştirme sıralaması (Merge sort)
def merge(sol, sag):
	if not len(sol) or not len(sag):
		return sol or sag

	sonuc = []
	i, j = 0, 0
	while (len(sonuc) < len(sol) + len(sag)):
		if sol[i] < sag[j]:
			sonuc.append(sol[i])
			i+= 1
		else:
			sonuc.append(sag[j])
			j+= 1
		if i == len(sol) or j == len(sag):
			sonuc.extend(sol[i:] or sag[j:])
			break

	return sonuc

def merge_sort(arr):
	if len(arr) < 2:
		return arr

	orta = len(arr)//2
	sol = merge_sort(arr[:orta])
	sag = merge_sort(arr[orta:])

	return merge(sol, sag)

dizi=[3,2,1,6,7,5]
print(merge_sort(dizi))

#hızlı sıralama (quick sort)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

dizi=[3,2,1,6,7,5]
print(quick_sort(dizi))
