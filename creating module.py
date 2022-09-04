'''Create a module MassConversior.py that stores function for mass conversion e.g , 
· A kgtotonne( ) to convert kg to tonnes 
· A tonnetokg() to convert tonne to kg 
· A kgtopound( ) to convert kg to pound 
· A poundtokg()to convert pound to kg 
(Also store constants 1 kg - 0.001 tonne, 1 kg = 2.20462 pound) 
Help( ) function should give proper information about the module.'''
one_kg_in_tonnes = 0.001 
one_kg_in_pound = 2.20462 
def kgtotonne( x ): 
"Return value in tonne from kilogram" 
return x * one_kg_in_tonnes 
def tonnetokg( x ) : 
"Return value in kilogram from tonnes" 
return x / one_kg_in_tonnes 
def kgtopound ( x ): 
"Return value pound from kilogram" 
return x * one_kg_in_pound 
def poundtokg( x ) : 
"Return value kilogram from pound" 
return x / one_kg_in_pound