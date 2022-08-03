from time import sleep, time
from random import uniform
from statistics import mean
from msvcrt import kbhit

def reflex_test(times = []):
    if len(times) == 0:
        print('A prompt will appear 1-5 seconds after you begin the test.')
        input('Press RETURN to begin the test, then RETURN again when the prompt appears.')
        print()
    sleep(uniform(1, 5))
    while kbhit():
        input()
    print('NOW!!!')
    start = time()
    input()
    res = time() - start
    times.append(res)
    print('You pressed RETURN in', res, 'seconds.')
    if input("To start the test again, just press RETURN. Otherwise, enter anything. ") == '':
        print()
        reflex_test(times)
    else:
        print('Your average time was', mean(times), 'seconds.')
    
reflex_test()

# If the script is run in the IDE (or outside of Windows),
#     kbhit won't work so input during sleep may cause problems.