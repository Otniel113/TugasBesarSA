# TugasBesarSA
Membandingkan 2 strategi algoritma : Brute Force (implementasi SelectionSort) dan Divide and Conquer (implementasi MergeSort) yang dikerjakan secara berkelompok 3 orang dengan Winico Fazry dan Daffa Ulayya.

## Formulasi Masalah
HDI atau Human Development Index merupakan menjelaskan bagaimana penduduk dapat mengakses hasil pembangunan yang terdiri dari 3 bidang yaitu pendapatan, kesehatan, dan pendidikan, HDI bisa diukur dalam bentuk bilangan. Maka dari itu kita menggunakan algoritma pengurutan dengan metode Brute Force yaitu Selection Sort dan Divide and Conquer yaitu Merge Sort untuk mengurutkan data HDI dari terbesar hingga terkecil. Sebagai pembeda dari jumlah data, dilakukan pengurutan untuk 2 kasus yaitu mengurutkan HDI Subnational (setingkat provinsi, negara bagian, oblast, dsb.) dan mengurutkan HDI National.

## Dataset
Dataset diambil dari [GlobalDataLab](https://globaldatalab.org/shdi/) menjadi Ms. Excel <img src = 'https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white' /> dengan nama rank_hdi.xlsx

## Implementasi Algoritma
Brute Force - SelectionSort
```python
def SelectionSort(arr):
    for i in range(0,len(arr)):
        maks = i
        for j in range(i+1,len(arr)):
            if (arr[j][2] > arr[maks][2]):
                maks = j
        arr[maks], arr[i] = arr[i], arr[maks]

```
<br>
Divide and Conquer - MergeSort

```python
def MergeSort(arr, low, high):
    if low >= high:
        return

    mid = (low + high)//2                           
    MergeSort(arr, low, mid)                        
    MergeSort(arr, mid + 1, high)                   
    Merge(arr, low, high, mid)                      

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
```

## Analisis Hasil
Skenario pengujian dilakukan sebanyak 4 kondisi dengan masing-masing kondisi dilakukan 3 kali pengujian dengan mengambil nilai rata-ratanya. Kondisi tersebut adalah
1. Mengurutkan HDI National dengan MergeSort
2. Mengurutkan HDI National dengan SelectionSort
3. Mengurutkan HDI Subnational dengan MergeSort
4. Mengurutkan HDI Subnational dengan MergeSort

Hasil pengujian berupa waktu eksekusi dalam detik sebagai berikut
| Skenario | Waktu |
| -- | -- |
| 1 | 0.0011 |
| 2 | 0.1556 |
| 3 | 0.0689 |
| 4 | 0.8652 |
<br>

Dapat juga dilihat pada tabel banyaknya data (sumbu X) dengan waktu eksekusi (sumbu Y)
![image](https://user-images.githubusercontent.com/57952404/148204508-68c9025c-fb57-4816-9034-67933538bc44.png)

## Kompleksitas
Kompleksitas dari algoritma Brute Force - SelectionSort adalah O(n^2) sedangkan kompleksitas dari algoritma Divide and Conquer - MergeSort adalah O(n log n)

## Lebih Lengkap
Informasi lebih lengkap dapat dilihat di laporan [Kelompok 9 _ Laporan Tubes Strategi Algoritma.pdf](https://github.com/Otniel113/TugasBesarSA/files/7814261/Kelompok.9._.Laporan.Tubes.Strategi.Algoritma.pdf)
