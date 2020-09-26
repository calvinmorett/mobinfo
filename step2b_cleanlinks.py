mwpages = ['#mw-pages']

with open('step2.txt') as step2, open('step2b_cleanup.txt', 'w') as step2_cleanup:
    for line in step2:
        if not any(mwpages in line for mwpages in mwpages):
            step2_cleanup.write(line)