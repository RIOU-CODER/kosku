import pytest
from billing import calculate_total_bill

def test_bayar_tepat_waktu():
    assert calculate_total_bill(1000000, 0) == 1000000

def test_telat_satu_hari():
    assert calculate_total_bill(1000000, 1) == 1050000

def test_telat_beberapa_hari():
    assert calculate_total_bill(2000000, 3) == 2150000

def test_bayar_lebih_awal():
    # Menguji TC-06: Hari negatif dianggap 0 hari telat
    assert calculate_total_bill(1000000, -5) == 1000000

def test_sewa_gratis_tetap_kena_denda():
    # Menguji TC-09
    assert calculate_total_bill(0, 3) == 150000

def test_sewa_negatif_error():
    # Menguji TC-07
    with pytest.raises(ValueError):
        calculate_total_bill(-500000, 2)

def test_input_tipe_string_error():
    # Menguji TC-08
    with pytest.raises(TypeError):
        calculate_total_bill(1000000, "dua")

def test_telat_sangat_lama():
    # Menguji TC-10
    assert calculate_total_bill(1000000, 100) == 6000000
