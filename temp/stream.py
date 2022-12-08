from new_analyze import analyze

ana = analyze()

while True:
    cmd = input()
    ana.average(target=cmd)