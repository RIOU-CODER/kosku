@startuml
autonumber

actor "Pengguna (Penyewa / Pemilik)" as User
participant "Frontend / Interface" as UI
participant "Modul Autentikasi" as Auth
database "Database" as DB

group 1. Alur Login & Penentuan Peran
    User -> UI: Input username/email & password
    UI -> Auth: Kirim kredensial (POST /login)
    Auth -> DB: Cek data pengguna & hash password
    DB --> Auth: Data cocok (Return User ID & Peran: Penyewa / Pemilik)
    Auth -> Auth: Generate JWT / Session Token (menyimpan data Peran)
    Auth --> UI: Kirim Token & data Peran pengguna
    UI --> User: Redirect ke Dashboard (Penyewa / Pemilik)
end

group 2. Alur Logout & Invalidasi Sesi
    User -> UI: Klik tombol Logout
    UI -> Auth: Request Logout (Kirim Token)
    Auth -> Auth: Hapus / nonaktifkan Token Sesi
    Auth --> UI: Konfirmasi Logout berhasil
    UI --> User: Hapus Token dari local storage & redirect ke Halaman Login
end
@enduml
