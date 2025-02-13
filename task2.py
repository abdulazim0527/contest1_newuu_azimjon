def typeBasedTransformer(information):
    yangilangan = {}
    
    for org_kalit, org_qiymat in information.items():
        
        if isinstance(org_qiymat, (int, float)):
            yangilangan[org_kalit] = org_qiymat ** 2
        elif isinstance(org_qiymat, bool):
            yangilangan[org_kalit] = not org_qiymat
        elif isinstance(org_qiymat, (list, tuple)):
            yangilangan[org_kalit] = org_qiymat[::-1]
        elif isinstance(org_qiymat, dict):
            yangilangan[org_kalit] = {s: t for t, s in org_qiymat.items()}
        elif isinstance(org_qiymat, str):
            yangilangan[org_kalit] = org_qiymat[::-1]
        
        else:
            yangilangan[org_kalit] = org_qiymat
            
    return yangilangan

# Example usage:
information = {
    'a': 13,
    'b': 4.5,
    'c': "Sekin",
    'd': False,
    'e': [6, 4, 3],
    'f': {"hw": 5, "ts": 6},
    'g': None,
    'h': (2, 8, 10)
}

output1 = typeBasedTransformer(information)
print(output1)