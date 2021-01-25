import random 
import pickle

alphabet = "abcdefghijklmnopqrstuvwxyz"
 

# Create Rotor one 
r1 = list(alphabet)
random.shuffle(r1)
r1 = ''.join(r1)
print(r1)


#Create Rotor Tow
r2 = list(alphabet)
random.shuffle(r2)
r2 = ''.join(r2)
print(r2)

#Create Rotor Three
r3 = list(alphabet)
random.shuffle(r3)
r3 = ''.join(r3)
print(r3)

fs =  open('./today_rotor_state.enigma', 'wb')
pickle.dump((r1,r2,r3), fs)
fs.close