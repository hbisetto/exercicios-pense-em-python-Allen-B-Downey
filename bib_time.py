import time

# Obtém o tempo atual em segundos desde 1 de janeiro de 1970 (era Unix)
tempo_atual_segundos = time.time()

# Converte o tempo atual em uma estrutura legível de horas, minutos, segundos
tempo_atual_struct = time.localtime(tempo_atual_segundos)

# Calcula o número de dias desde 1970
segundos_por_dia = 24 * 60 * 60
dias_desde_epoca = int(tempo_atual_segundos // segundos_por_dia)

# Exibe as horas, minutos e segundos atuais
hora_atual = time.strftime("%H:%M:%S", tempo_atual_struct)

# Resultado final
print(f"Hora atual: {hora_atual}")
print(f"Número de dias desde 1 de janeiro de 1970: {dias_desde_epoca}")
