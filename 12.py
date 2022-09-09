#12

import random
for i in range(1,11):
    name = random.randint(1,100)
    f = open( 'sample'+ str(name) +'.pdf'  ,'w')