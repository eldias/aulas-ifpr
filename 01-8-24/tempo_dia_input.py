total_em_segundos = int(input("Insira o tempo em segundos:"))

dia = total_em_segundos // 86400

hora = total_em_segundos // 3600

resto_da_hora = total_em_segundos % 3600

minuto = resto_da_hora // 60

segundo = resto_da_hora % 60

print(dia, "dia" ,hora, "horas", minuto, "minutos", segundo, "segundos")

