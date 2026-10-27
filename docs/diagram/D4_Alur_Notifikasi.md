@startuml
autonumber

actor "Penyewa" as Tenant
actor "Pemilik Kos" as Owner
participant "Modul Tagihan" as Billing
participant "Modul Tiket Keluhan" as Ticket
participant "Modul Notifikasi" as Notif
database "Database" as DB

group 1. Pengingat Tenggat Waktu & Keterlambatan Tagihan (Automated / Trigger)
    Billing -> Notif: Trigger pengecekan status & jatuh tempo tagihan
    Notif -> DB: Ambil daftar tagihan (mendekati tenggat / terlambat)
    DB --> Notif: Data tagihan & kontak penyewa
    Notif -> Tenant: Kirim pengingat tagihan / peringatan keterlambatan
    Notif -> DB: Simpan riwayat pengiriman notifikasi
end

group 2. Pemberitahuan Pembaruan Status Tiket Keluhan
    Owner -> Ticket: Update status tiket (contoh: "Sedang Diperbaiki" / "Selesai")
    Ticket -> DB: Simpan pembaruan status tiket
    Ticket -> Notif: Trigger pemberitahuan perubahan status tiket
    Notif -> Tenant: Kirim notifikasi pembaruan status perbaikan ke penyewa
    Notif -> DB: Simpan riwayat pengiriman notifikasi
end
@enduml
