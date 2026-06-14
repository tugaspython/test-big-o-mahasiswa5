def cari_pasangan(arr, target):
    """
    Mencari apakah ada dua angka berbeda dalam list yang jumlahnya sama dengan target.
    
    Args:
        arr: List of integers
        target: Integer target yang ingin dicapai
    
    Returns:
        Boolean: True jika ada pasangan, False jika tidak
    """
    seen = set()
    for angka in arr:
        komplemen = target - angka
        if komplemen in seen:
            return True
        seen.add(angka)
    return False

