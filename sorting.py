# Muhammad waliyuddin
# F55121009
import time

# Fungsi untuk melakukan Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    end_time = time.time()
    return arr, end_time - start_time

# Fungsi untuk melakukan Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    end_time = time.time()
    return arr, end_time - start_time

# Fungsi untuk menampilkan hasil iterasi
def display_iterations(iterations):
    print("Iterasi Pertama:")
    print(iterations[:5])
    print("Iterasi Terakhir:")
    print(iterations[-5:])

# Fungsi untuk menampilkan waktu komputasi
def display_computation_time(time):
    print("Waktu Komputasi: %.6f detik" % time)

# Fungsi untuk menampilkan sebelum dan sesudah pengurutan
def display_before_after(arr):
    print("Sebelum Pengurutan:")
    print(arr)
    print("Sesudah Pengurutan:")
    print(arr)

# Fungsi untuk melakukan analisis algoritma
def analyze_algorithm():
    # Bubble Sort
    print("Bubble Sort:")
    sorted_arr, time_taken_bubble = bubble_sort(arr.copy())
    display_iterations(sorted_arr)
    display_computation_time(time_taken_bubble)
    display_before_after(sorted_arr)
    print()

    # Insertion Sort
    print("Insertion Sort:")
    sorted_arr, time_taken_insertion = insertion_sort(arr.copy())
    display_iterations(sorted_arr)
    display_computation_time(time_taken_insertion)
    display_before_after(sorted_arr)

# Main program
arr = [
    12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33,
    90, 90, 7, 26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84,
    32, 5, 3, 44, 21, 10, 21, 17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6,
    3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81
]

print("Pilihan Sort:")
print("1. Bubble Sort")
print("2. Insertion Sort")
choice = int(input("Masukkan pilihan (1/2): "))

if choice == 1:
    analyze_algorithm()
elif choice == 2:
    analyze_algorithm()
else:
    print("Pilihan tidak valid.")
