# D6. Test Case Design (1 Scenario)

**Scenario:** Menghitung Total Tagihan Sewa dan Denda Keterlambatan

| ID | Title | Type | Preconditions | Input / Steps | Expected Result |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-01 | Bayar tepat waktu | Common | Sewa Rp1.000.000 | `rent=1000000`, `late_days=0` | Total Rp1.000.000 (tanpa denda) |
| TC-02 | Telat 1 hari | Common | Sewa Rp1.000.000, Denda Rp50.000/hari | `rent=1000000`, `late_days=1` | Total Rp1.050.000 |
| TC-03 | Telat 3 hari | Common | Sewa Rp2.000.000 | `rent=2000000`, `late_days=3` | Total Rp2.150.000 |
| TC-04 | Telat 5 hari | Common | Sewa Rp1.500.000 | `rent=1500000`, `late_days=5` | Total Rp1.750.000 |
| TC-05 | Telat 10 hari | Common | Sewa Rp1.000.000 | `rent=1000000`, `late_days=10` | Total Rp1.500.000 |
| TC-06 | Pembayaran lebih awal | Edge | Sistem menerima hari negatif | `rent=1000000`, `late_days=-5` | Total Rp1.000.000 (tidak ada denda/error) |
| TC-07 | Input uang sewa negatif | Edge | Salah ketik harga sewa | `rent=-500000`, `late_days=2` | *Error / Invalid Input* |
| TC-08 | Input hari format teks | Edge | Salah tipe data (String) | `rent=1000000`, `late_days="dua"`| *Error / Invalid Type* |
| TC-09 | Uang sewa Rp0 | Edge | Ruangan gratis/diskon penuh | `rent=0`, `late_days=3` | Total Rp150.000 (hanya denda) |
| TC-10 | Telat sangat lama | Edge | Telat 100 hari (batas sistem) | `rent=1000000`, `late_days=100` | Total Rp6.000.000 |

### Penjelasan Pemilihan Edge Cases
Pemilihan *edge case* berfokus pada menguji ketahanan sistem terhadap input yang tidak wajar atau batas ekstrim. Kasus input negatif (TC-07) atau format teks (TC-08) bertujuan memastikan fungsi menolak tipe data yang salah agar aplikasi tidak *crash*. Sementara itu, kasus pembayaran lebih awal di mana hari bernilai negatif (TC-06) dan biaya sewa Rp0 (TC-09) diuji untuk memastikan logika denda beroperasi dengan benar tanpa menghasilkan angka minus atau jumlah tagihan yang tidak masuk akal.
