# Desafio 3 - Estatísticas com Tuplas e Desempacotamento

temperaturas = (29.4, 30.2, 28.9, 31.0, 30.2, 29.7, 28.9)

# Desempacotamento
t1, t2, t3, t4, t5, t6, t7 = temperaturas
print(f"Temperaturas desempacotadas: {t1}, {t2}, {t3}, {t4}, {t5}, {t6}, {t7}")

# Média
media = sum(temperaturas) / len(temperaturas)
print(f"Média das temperaturas: {media:.2f}")

# Temperaturas únicas
unicas = set(temperaturas)
print(f"Temperaturas únicas: {unicas}")

# Discussão sobre precisão float
print("Comparando 30.2 == 30.2000001:", 30.2 == 30.2000001)
print("Devido à representação binária dos floats, pequenas diferenças podem ocorrer. O Python considera iguais apenas se forem exatamente iguais na memória. Para comparar floats, use math.isclose() para tolerância de erro.")