red='\033[0;31m'
orange='\033[1;31m'
green='\033[0;32m'
cyan='\033[0;36m'
blue='\033[0;34m'
yellow='\033[0;33m'
magenta='\033[0;35m'
violet='\033[1;35m'

import random
def random_color():
    return random.choice([yellow, orange, red, magenta, violet, blue, cyan
    , green])
if __name__ == "__main__":
    print (random_color() 
