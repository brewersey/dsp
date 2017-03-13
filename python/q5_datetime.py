# Hint:  use Google to find python function
import pandas as pd
####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

Id = pd.Timestamp(date_start)
Sd = pd.Timestamp(date_stop)
print(Sd - Id)

####b)  
date_start = '12312013'  
date_stop = '05282015'  

Id = [l for l in date_start]
Id.insert(2, '-')
Id.insert(5, '-')
date_start = ''.join(Id)

Sd = [l for l in date_stop]
Sd.insert(2, '-')
Sd.insert(5, '-')
date_stop = ''.join(Sd)

Id = pd.Timestamp(date_start)
Sd = pd.Timestamp(date_stop)
print(Sd - Id)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

Id = pd.Timestamp(date_start)
Sd = pd.Timestamp(date_stop)
print(Sd - Id)
