larg = float(input("largura da parede: "))
alt = float(input("altura da parede: "))
área = larg * alt
print("Sua parede tem a dimensão de {}x{} e sua área ée de {}m².".format(larg, alt, área))
tinta = área / 2
print("para pintar essa parede, você precisará de {}l de tinta.".format(tinta))