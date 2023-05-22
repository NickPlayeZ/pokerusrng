from MT import MT

rng = MT(int(input("Initial Seed: 0x"),16))
initial_advances = 0
#initial_advances = int(input("Initial Advances: "))
max_advances = int(input("Max Advances: "))
rng.advance(initial_advances)
pokerus_UShorts = [16384, 32768, 49152] # 0x4000, 0x8000, 0xC000

print("----------------")

for cnt in range(max_advances):
    nextUShort = rng.nextUShort()
    if nextUShort in pokerus_UShorts:
        print("== Found ==")
        print(f"IV Frame {initial_advances+cnt} has Pokerus")