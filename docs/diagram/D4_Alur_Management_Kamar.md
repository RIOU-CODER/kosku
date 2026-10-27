@startuml
autonumber

actor "Pemilik Kos" as Pemilik
participant "Frontend / Interface" as UI
participant "Modul Autentikasi" as Auth
participant "Modul Manajemen Kamar" as Room
database "Database" as DB

group 1. Pencatatan Data & Kapasitas Kamar
    Pemilik -> UI: Input nomor & kapasitas kamar baru
    UI -> Auth: Validasi sesi & peranan (Pemilik)
    Auth --> UI: Sesi Valid
    UI -> Room: Tambah data kamar baru
    Room -> DB: Simpan data kamar (Status: Tersedia)
    DB --> Room: Data berhasil disimpan
    Room --> UI: Respon berhasil
    UI --> Pemilik: Konfirmasi data kamar tersimpan
end

group 2. Penempatan Penyewa & Pembaruan Status Kamar
    Pemilik -> UI: Pilih kamar & tempatkan penyewa
    UI -> Auth: Validasi akses Pemilik
    Auth --> UI: Sesi Valid
    UI -> Room: Alokasikan penyewa ke kamar X
    Room -> DB: Update alokasi penyewa & status (Terisi/Penuh)
    DB --> Room: Konfirmasi pembaruan status ketersediaan
    Room --> UI: Respon alokasi berhasil
    UI --> Pemilik: Tampilkan status ketersediaan kamar terbaru
end
@enduml
