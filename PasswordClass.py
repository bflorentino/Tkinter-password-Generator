from random import randint as rd, sample, shuffle


class Password():
    # This class'aim is to generate a password according to the required length and strength

########## Password Possible chars ##############
    _upperCharString = "ABCDEFGHIJKLMNOPQRSTUVXWYZ"
    _lowerCharString = "abcdefghijklmnopqrstuvxwyz"
    _digits = "0123456789"
    _specialCharString = "@#$!%^&*()_+-={[}]/\"'?/,<.>`~¿¡:;"


    def __init__(self, Length: int, Strength: int):

        self._Length = Length
        self._Strength = Strength
        self._password = ""


########## This method will call the responsible function to generate the required password ##################
    def generatePassword(self):

        if self._Strength == 0:
            self._password = self._minimunStrengthPassword()
        
        elif self._Strength == 1:
            self._password = self._mediumStrengthPassword()
        
        elif self._Strength == 2:
            self._password = self._strongPassword()
        
        return self._password


################ This method will return the password when the user selects a minimun strength ########################
############ When it's a mininum strenght it generates a password with 1 upper case, 1 digit and left, lowers chars ##################
    def _minimunStrengthPassword(self):
        
        if self._Length > 9:
            self._Length = 9
        
        elif self._Length < 5:
            self._Length = 5

        password = self.__setPassword(1, 1, 0)
        
        return "".join(password)
        

############## This method will return the password when the user selects a medium strength #####################
#### When it's a medium strenght it generates a password with 2 upper case, 2 digits, 1 special char and left, lowers chars ####
    def _mediumStrengthPassword(self):
        if self._Length > 14:
            self._Length = 14
        
        elif self._Length < 10:
            self._Length = 10
        
        password = self.__setPassword(2, 2, 1)
        
        return "".join(password)
        

################# This method will return the password when the user selects a Strong password #######################
##### When it's a max strenght it generates a password with 3 or 4 upper cases, 3 or 4 digits, 2 or 3 special chars and left, lowers chars ###
    def _strongPassword(self):
        
        if self._Length > 25:
            self._Length = 25
        
        elif self._Length < 15:
            self._Length = 15
        
        uppers = 3 if self._Length <= 20 else 4
        digitsPassword = 3 if self._Length <= 20 else 4
        specialchar = 2 if self._Length <= 20 else 3
        
        password = self.__setPassword(uppers, digitsPassword, specialchar)
        
        return "".join(password)


################# Generates the password #######################
    def __setPassword(self, uppersCharsCant, digitsCant, specialCharsCant):

        upperChar = sample(list(self._upperCharString), uppersCharsCant)
        digits = sample(list(self._digits), digitsCant)
        specialChars = sample(list(self._specialCharString), specialCharsCant)

        lowerChar = sample(list(self._lowerCharString), self._Length - (uppersCharsCant + digitsCant +specialCharsCant))

        password = list("".join(upperChar) + "".join(digits) +
                        "".join(lowerChar) + "".join(specialChars))
                
        shuffle(password)

        return password


    def setLength(self, Length: int):
        self._Length = Length


    def setStrength(self, Strength: int):
        self._Strength = Strength