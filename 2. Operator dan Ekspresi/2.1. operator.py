a = 2
a = a * 3
print(a)

'''
Berikut adalah ikhtisar singkat tentang operator yang tersedia:

+ (plus)
Menambahkan dua objek
3 + 5memberikan 8. 'a' + 'b'memberikan 'ab'.

- (dikurangi)
Memberikan pengurangan satu nomor dari yang lain; jika operan pertama tidak ada maka dianggap nol.
-5.2memberikan angka negatif dan 50 - 24 memberi 26.

* (multiply, berkembang biak)
Memberikan perkalian dua angka atau mengembalikan string yang berulang kali.
2 * 3memberikan 6. 'la' * 3 memberikan 'lalala'.

** (power, kekuatan)
Mengembalikan x ke pangkat y
3 ** 4 memberikan 81(yaitu 3 * 3 * 3 * 3)

/ (membagi)
Bagi x dengan y
13 / 3 memberi 4.333333333333333

// (divide and floor, bagi dan lantai)
Bagi x dengan y dan bulatkan jawabannya ke nilai bilangan bulat terdekat. Perhatikan bahwa jika salah satu nilainya adalah float, Anda akan mendapatkan kembali float.
13 // 3 memberi 4
-13 // 3 memberi -5
9//1.81 memberi 4.0

% (modul)
Mengembalikan sisa pembagian
13 % 3 memberikan 1. -25.5 % 2.25 memberikan 1.5.

<< (geser kiri)
Menggeser bit angka ke kiri dengan jumlah bit yang ditentukan. (Setiap nomor diwakili dalam memori dengan bit atau digit biner yaitu 0 dan 1)
2 << 2memberikan 8. 2diwakili oleh 10bit.
Pergeseran ke kiri dengan 2 bit memberikan 1000yang mewakili desimal 8.

>> (geser kanan)
Menggeser bit angka ke kanan dengan jumlah bit yang ditentukan.
11 >> 1memberikan 5.
11diwakili dalam bit 1011dimana ketika digeser kanan oleh 1 bit memberikan 101yang merupakan desimal 5.

& (bit-wise DAN)
Bit-bijaksana DAN angka: jika kedua bit 1, hasilnya adalah 1. Jika tidak, itu 0.
5 & 3memberi 1( 0101 & 0011 memberi 0001)

| (bit-wise ATAU)
Bitwise ATAU dari angka: jika kedua bit adalah 0, hasilnya adalah 0. Jika tidak, itu 1.
5 | 3 memberi 7( 0101 | 0011 memberi 0111)

^ (bit-wise XOR)
XOR bitwise dari angka: jika kedua bit ( 1 or 0) sama, hasilnya adalah 0. Jika tidak, itu 1.
5 ^ 3 memberi 6( O101 ^ 0011 memberi 0110)

~ (bit-wise, pembalikan)
Inversi bit-bijaksana dari x adalah -(x+1)
~5 memberikan -6. Lebih detail di http://stackoverflow.com/a/11810203

< (kurang dari)
Mengembalikan apakah x lebih kecil dari y. Semua operator perbandingan mengembalikan Trueatau False. Perhatikan kapitalisasi nama-nama ini.
5 < 3 memberi Falsedan 3 < 5 memberi True.
Perbandingan dapat dirantai secara sewenang-wenang: 3 < 5 < 7 memberi True.

> (lebih besar dari)
Mengembalikan apakah x lebih besar dari y
5 > 3 kembali True. Jika kedua operan adalah angka, mereka terlebih dahulu dikonversi ke tipe umum. Jika tidak, itu selalu kembali False.

<= (kurang dari atau sama dengan)
Mengembalikan apakah x lebih kecil atau sama dengan y
x = 3; y = 6; x <= y kembali True

>= (lebih dari atau sama dengan)
Mengembalikan apakah x lebih besar dari atau sama dengan y
x = 4; y = 3; x >= 3 kembali True

== (sama dengan)
Bandingkan jika objeknya sama
x = 2; y = 2; x == y kembali True
x = 'str'; y = 'stR'; x == y kembali False
x = 'str'; y = 'str'; x == y kembali True

!= (tidak sama dengan)
Bandingkan jika objeknya tidak sama
x = 2; y = 3; x != y kembali True

not (boolean TIDAK)
Jika x adalah True, ia kembali False. Jika x adalah False, ia kembali True.
x = True; not x kembali False.

and (boolean DAN)
x and y mengembalikan False jika x adalah False, jika tidak mengembalikan evaluasi y
x = False; y = True; x and y kembali Falsekarena x Salah. Dalam hal ini, Python tidak akan mengevaluasi y karena ia mengetahui bahwa sisi kiri dari ekspresi 'dan' adalah False yang menyiratkan bahwa seluruh ekspresi akan False terlepas dari nilai lainnya. Ini disebut evaluasi hubung singkat.

or (boolean ATAU)
Jika x adalah True, ia mengembalikan True, jika tidak ia mengembalikan evaluasi y
x = True; y = False; x or y kembali True. Evaluasi hubung singkat juga berlaku di sini.
'''