def calculate_total_bill(rent, late_days):
    if not isinstance(rent, (int, float)) or not isinstance(late_days, int):
        raise TypeError("Input harus berupa angka")
    if rent < 0:
        raise ValueError("Harga sewa tidak boleh negatif")
    
    # Anggap denda keterlambatan adalah Rp50.000 per hari
    penalty_per_day = 50000
    actual_late_days = max(0, late_days) # Jika bayar awal (negatif), dihitung 0
    
    total_penalty = actual_late_days * penalty_per_day
    return rent + total_penalty
