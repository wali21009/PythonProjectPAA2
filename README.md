# PythonProjectPAA2
Muhammad Waliyuddin F55121009

-Percobaan 1-

Dalam kode program di percobaan 1, terdapat fungsi `bubble_sort` untuk melakukan pengurutan menggunakan algoritma Bubble Sort, dan fungsi `insertion_sort` untuk melakukan pengurutan menggunakan algoritma Insertion Sort. Fungsi lainnya digunakan untuk menampilkan hasil iterasi, waktu komputasi, sebelum dan sesudah pengurutan, serta analisis algoritma.
Untuk menjalankan program ini, pengguna dapat memilih opsi antara Bubble Sort (pilihan 1) atau Insertion Sort (pilihan 2) dan program akan menampilkan hasil sesuai dengan ketentuan yang diberikan.

Analisis algoritma untuk Bubble Sort:
1. Worst case: Jika elemen-elemen dalam array sudah terurut dalam urutan terbalik, Bubble Sort akan memerlukan waktu yang paling lama karena setiap elemen akan dipindahkan ke posisi yang benar secara iteratif. Kompleksitas waktu worst case Bubble Sort adalah O(n^2).
2. Best case: Jika elemen-elemen dalam array sudah terurut dengan benar, Bubble Sort akan menyelesaikan pengurutan dalam satu iterasi. Namun, dalam implementasi di atas, terdapat optimisasi dengan menggunakan variabel `swapped` sehingga jika tidak ada pertukaran yang terjadi, iterasi akan dihentikan. Kompleksitas waktu best case Bubble Sort adalah O(n).
3. Average case: Rata-rata, Bubble Sort akan memerlukan waktu yang cukup lama karena kompleksitas waktu rata-rata adalah O(n^2).

Analisis algoritma untuk Insertion Sort:
1. Worst case: Jika elemen-elemen dalam array sudah terurut dalam urutan terbalik, Insertion Sort akan memerlukan waktu yang paling lama karena setiap elemen akan dipindahkan ke posisi yang benar secara iteratif. Kompleksitas waktu worst case Insertion Sort adalah O(n^2).
2. Best case: Jika elemen-elemen dalam array sudah terurut dengan benar, Insertion Sort tidak perlu melakukan perpindahan elemen dan hanya perlu memeriksa setiap elemen sekali. Kompleksitas waktu best case Insertion Sort adalah O(n).
3. Average case: Rata-rata, Insertion Sort akan memerlukan waktu yang cukup cepat karena kompleksitas waktu rata-rata adalah O(n^2), tetapi memiliki konstanta yang lebih rendah dibandingkan Bubble Sort.

-Percobaan 2-

Untuk melakukan analisis dari kode program tersebut, perlu diperhatikan beberapa faktor:

1. Worst Case:
   - Algoritma TSP: Dalam kasus terburuk, kompleksitas waktu algoritma TSP adalah O(n!), di mana n adalah jumlah simpul dalam grafik. Ini terjadi ketika semua kemungkinan permutasi rute dijelajahi untuk mencari rute terpendek. Namun, dengan menggunakan pendekatan aproksimasi seperti yang dilakukan dalam kode program, kompleksitas waktu dapat lebih rendah, tetapi masih cukup tinggi tergantung pada ukuran grafik.
   - Algoritma Dijkstra: Dalam kasus terburuk, kompleksitas waktu algoritma Dijkstra adalah O((V + E) log V), di mana V adalah jumlah simpul dan E adalah jumlah tepi dalam grafik. Hal ini terjadi ketika semua simpul harus dikunjungi dan jarak terpendek ke semua simpul harus dihitung.

2. Best Case:
   - Algoritma TSP: Dalam kasus terbaik, jika ada sedikit simpul atau jika grafik memiliki sifat khusus seperti simetri, kompleksitas waktu algoritma TSP dapat lebih rendah. Namun, tetap ada kompleksitas minimal yang tergantung pada jumlah simpul dan kompleksitas aproksimasi yang digunakan.
   - Algoritma Dijkstra: Dalam kasus terbaik, jika simpul awal adalah simpul tujuan atau memiliki jarak terpendek ke simpul tujuan, maka algoritma Dijkstra dapat berakhir lebih cepat. Hal ini terjadi ketika simpul tujuan ditemukan sejak awal atau berada dalam jarak minimum dari simpul awal.

3. Average Case:
   - Algoritma TSP: Untuk algoritma TSP dengan pendekatan aproksimasi, kompleksitas waktu rata-rata tergantung pada ukuran grafik dan kualitas aproksimasi yang digunakan. Dalam banyak kasus, pendekatan aproksimasi memberikan hasil yang cukup baik dengan kompleksitas waktu yang lebih rendah dibandingkan dengan TSP eksak.
   - Algoritma Dijkstra: Dalam kasus rata-rata, kompleksitas waktu algoritma Dijkstra juga tergantung pada ukuran grafik dan struktur jaringan. Jika grafik memiliki sifat khusus seperti struktur pohon atau terbatasnya jumlah tepi, kompleksitas waktu dapat lebih rendah.

Namun, penting untuk dicatat bahwa analisis ini bersifat umum dan kompleksitas sebenarnya dapat bervariasi tergantung pada implementasi kode program, struktur grafik, dan pendekatan yang digunakan.
