# Sample taken from pyStrich GitHub repository
# https://github.com/mmulqueen/pyStrich
from pystrich.datamatrix import DataMatrixEncoder

x = input(" Please enter your name: ")

print( "Welcome",x)

encoder = DataMatrixEncoder(x)
encoder.save('./datamatrix_test.png')
print("This is your name as a DataMatrix: " + encoder.get_ascii())
