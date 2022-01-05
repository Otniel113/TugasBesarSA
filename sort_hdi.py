import time
import pandas as pd

# Melakukan import data dari Excel
def importData():
    data = pd.read_excel("rank_hdi.xlsx")
    country = data['Country'].to_list()
    region = data['Region'].to_list()
    score = data[2018].to_list()
    hdi_national = []
    hdi_subnational = []
    for i in range(0,len(country)):
        tampung = []
        if (str(score[i]) != "nan"):                        #Tidak memasukkan missing value
            if (region[i] == "Total"):                      #Memilih data untuk wilayah Nasional dan ditampung ke list hdi_national
                tampung.append(country[i])
                tampung.append("Total")
                tampung.append(score[i])
                hdi_national.append(tampung)
            else:                                           #Memilih data untuk wilayah Subnasional dan ditampung ke list hdi_subnational
                tampung.append(country[i])
                tampung.append(region[i])
                tampung.append(score[i])
                hdi_subnational.append(tampung)
    return hdi_national, hdi_subnational                    #Melakukan return list keduanya

# Algoritma Selection Sort sebagai implementasi Brute Force
def SelectionSort(arr):
    for i in range(0,len(arr)):
        maks = i
        for j in range(i+1,len(arr)):
            if (arr[j][2] > arr[maks][2]):
                maks = j
        arr[maks], arr[i] = arr[i], arr[maks]

# Algoritma Merge Sort sebagai implementasi Divide and Conquer
def MergeSort(arr, low, high):
    if low >= high:
        return

    mid = (low + high)//2                           # Divide
    MergeSort(arr, low, mid)                        # Conquer kiri
    MergeSort(arr, mid + 1, high)                   # Conquer kanan
    Merge(arr, low, high, mid)                      # Merge

# Algoritma untuk Merge dari hasil pembagian 
def Merge(arr, low, high, mid):
    low_copy = arr[low:mid + 1]
    high_copy = arr[mid+1:high+1]

    low_copy_idx = 0
    high_copy_idx = 0
    sorted_index = low

    while low_copy_idx < len(low_copy) and high_copy_idx < len(high_copy):
        if low_copy[low_copy_idx][2] >= high_copy[high_copy_idx][2]:
            arr[sorted_index] = low_copy[low_copy_idx]
            low_copy_idx = low_copy_idx + 1
        else:
            arr[sorted_index] = high_copy[high_copy_idx]
            high_copy_idx = high_copy_idx + 1

        sorted_index = sorted_index + 1

    while low_copy_idx < len(low_copy):
        arr[sorted_index] = low_copy[low_copy_idx]
        low_copy_idx = low_copy_idx + 1
        sorted_index = sorted_index + 1

    while high_copy_idx < len(high_copy):
        arr[sorted_index] = high_copy[high_copy_idx]
        high_copy_idx = high_copy_idx + 1
        sorted_index = sorted_index + 1

# Melakukan export data menjadi file excel
def exportData(hdi_national, hdi_subnational):
    national_country = []
    national_score = []

    #Untuk data Subnasional
    for i in range(0,len(hdi_national)):
        national_country.append(hdi_national[i][0])
        national_score.append(hdi_national[i][2])
    data_1 = {"Country" : national_country,
            "Score" : national_score
            }
    df = pd.DataFrame(data_1, columns = ["Country", "Score"])
    df.to_excel(r'hasil_national.xlsx', index=False, header=True)

    #Untuk data n\Nasional
    subnational_country = []
    subnational_region = []
    subnational_score = []
    for i in range(0,len(hdi_subnational)):
        subnational_country.append(hdi_subnational[i][0])
        subnational_region.append(hdi_subnational[i][1])
        subnational_score.append(hdi_subnational[i][2])
    data_2 = {"Country" : subnational_country,
            "Region" : subnational_region,
            "Score" : subnational_score
            }
    df = pd.DataFrame(data_2, columns = ["Country", "Region", "Score"])
    df.to_excel(r'hasil_subnational.xlsx', index=False, header=True)


#==================MAIN PROGRAM==================
hdi_national, hdi_subnational = importData()

# Eksekusi Merge Sort National
hdi_national_copy = hdi_national
print("Sort Negara , banyak data = ", len(hdi_national_copy))
start = time.time()
MergeSort(hdi_national_copy,0,len(hdi_national_copy)-1)
end = time.time()
print("Waktu Eksekusi MergeSort = ", (end-start), " detik")

# Eksekusi Selection Sort National
hdi_national_copy = hdi_national
start = time.time()
SelectionSort(hdi_national_copy)
end = time.time()
print("Waktu Eksekusi SelectionSort = ", (end-start), " detik")

# Eksekusi Merge Sort Subnational
hdi_subnational_copy = hdi_subnational
print("\n\nSort SubNegara (Setara Provinsi), banyak data = ", len(hdi_subnational_copy))
start = time.time()
MergeSort(hdi_subnational,0,len(hdi_subnational_copy)-1)
end = time.time()
print("Waktu Eksekusi MergeSort = ", (end-start), " detik")

# Eksekusi Selection Sort Subnational
hdi_national_copy = hdi_national
start = time.time()
SelectionSort(hdi_subnational_copy)
end = time.time()
print("Waktu Eksekusi SelectionSort = ", (end-start), " detik")

# Menampung hasil copy ke list asli dan melakukan export
hdi_national = hdi_national_copy
hdi_subnational = hdi_subnational_copy
exportData(hdi_national,hdi_subnational)