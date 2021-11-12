import sys
import dz_4_2

command = sys.argv[1]
list = dz_4_2.currency_rates(command)
print(f"на {list[0]} 1 {list[1]} {list[2]} рублей")