
# Programavimo pritaikymas imones strukturai

# Gamybine duru imone, reikia projektuotojo, zaliavu, duru gamintojo ir administratoriaus

# Funkcijos

# Projektavimas 
# Cia galima aprasyti viena funkcija, taciau dvi idetos del logikos atskyrimo

def sukurti_projekta(projektuotojas, komponentai_projektavimui):
    projektas = f"Projektas suprojektuojamas ir sukomplektuojamas, tam reikalingi resursai: {projektuotojas}, {komponentai_projektavimui}"
    return projektas

def projektavimas(projektuotojas, komponentai_projektavimui):
    #atliekami projektavimo veiksmai
    projektas = sukurti_projekta(projektuotojas, komponentai_projektavimui)
    return projektas

# Projekto perdavimas duru gamintojui
def perduoti_projekta(gamintojas, projektas, projektuotojas):
    #perduodamas projektas gamintojui
    return gamintojas, projektas, projektuotojas

# Duru gamyba

def pagaminti_duris(gamintojas, projektas, komponentai_gamybai):
    durys = f'{gamintojas} pagal {projektas}, gamina duris su irankiais {komponentai_gamybai}'
    return durys

def gaminti_duris(gamintojas, projektas, komponentai_gamybai):
    # atliekami duru gamybos veiksmai
    durys = pagaminti_duris(gamintojas, projektas, komponentai_gamybai)
    return durys

# Pardavimas

def parduoti(administratorius, durys):
    pajamos = f'{administratorius} gauna preke {durys}, tada parduoda pirkejui ir gauna atlyginima'
    return pajamos


def parduoti_duris(administratorius, durys):
    # aliekami duru pardavimo veiksmai
    pajamos = parduoti(administratorius, durys)
    return pajamos

# Atlyginimu ismokejimas
def sumoketi_atlyginimus(administratorius, pajamos):
    atlyginimai = f'{administratorius} sumoka atlyginimus is {pajamos}'
    return atlyginimai

def ismoketi_atlyginimus(administratorius, pajamos):
    # atliekami altyginimu ismokejimo veiksmai
    atlyginimai = sumoketi_atlyginimus(administratorius, pajamos)
    return atlyginimai

# Procesu vykdymo seka -->>

# 1. Projektavimas

projektuotojas = "Projektuotojas"

komponentai_projektavimui = ['stalas', 'kede', 'kompiuteris', 'projektavimo programa', 'internetas']

projektas = projektavimas(projektuotojas, komponentai_projektavimui)

print("1. Projektavimas:", projektas)

# 2. Projekto perdavimas

gamintojas = 'Duru gamintojas'

gamintojas, projektas, projektuotojas = perduoti_projekta(gamintojas, projektas, projektuotojas)

print("2. Projekto perdavimas:", projektuotojas, "perduoda projekta gamintojui,", gamintojas, "pasiima", projektas)

# 3. Duru gamyba

komponentai_gamyba = ['stalas', 'irankiai', 'pjovimo_stakles', 'apranga']

durys = gaminti_duris(gamintojas, projektas, komponentai_gamyba)

print("3. Duru gamyba:", durys)

# 4. Duru pardavimas

administratorius = 'Administratorius'

pajamos = parduoti_duris(administratorius, durys)

print("4. Duru pardavimas:", pajamos)

# 5. Atlyginimu ismokejimas

atlyginimai = ismoketi_atlyginimus(administratorius, pajamos)

print("5. Atlyginimu ismokejimas:", atlyginimai)

# Funkciju perkelimas i kodo prieki
