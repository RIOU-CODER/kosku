
@startuml
left to right direction
skinparam packageStyle rectangle
skinparam shadowing false
skinparam actorStyle hollow

' Aktor
actor "Penyewa" as Penyewa
actor "Pemilik Kos" as Pemilik

rectangle "Sistem Kosku" {
    ' Manajemen Akun & Kamar
    usecase "uc-01: login" as uc1
    usecase "uc-02: registrasi penyewa" as uc2
    usecase "uc-03: daftar kamar & ketersediaan" as uc3
    
    ' Pengelolaan Pemilik Kos
    usecase "uc-04: penugasan penghuni" as uc4
    usecase "uc-05: buat tagihan otomatis" as uc5
    usecase "uc-12: perbarui status perbaikan" as uc12
    
    ' Aktivitas & Keuangan Penyewa
    usecase "uc-06: lihat tagihan bulanan" as uc6
    usecase "uc-07: unggah bukti transfer" as uc7
    usecase "uc-08: kalkulasi denda" as uc8
    usecase "uc-10: batas waktu pembayaran" as uc10
    usecase "uc-11: buat tiket laporan" as uc11
    
    ' Use Case Notifikasi (Tambahan Baru)
    usecase "uc-13: kirim notifikasi tagihan / status" as uc13
    usecase "uc-14: kirim pengingat jatuh tempo" as uc14
}

' Relasi Aktor Penyewa
Penyewa --> uc1
Penyewa --> uc3
Penyewa --> uc6
Penyewa --> uc7
Penyewa --> uc11

' Relasi Aktor Pemilik Kos
Pemilik --> uc1
Pemilik --> uc2
Pemilik --> uc3
Pemilik --> uc4
Pemilik --> uc5
Pemilik --> uc12

' Relasi Antar Use Case (Include & Extend)
uc7 ..> uc8 : "<<include>>"
uc10 ..> uc6 : "<<extend>>"
uc5 ..> uc14 : "<<include>>"
uc12 ..> uc13 : "<<include>>"
@enduml
