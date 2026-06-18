class String:
    def __init__(self):
        self.upper=0
        self.lower=0
        self.vowel=0
        self.consonant=0
        self.space=0
        self.string=""
    def getstr(self):
        self.string=str(input("Enter a String : "))
    def count(self):
        for ch in self.string:
            if (ch.isupper()):
                self.upper+=1
            if (ch.islower()):
                self.lower+=1
            if (ch in ('AEIOUaeiou')):
                self.vowel+=1
            if (ch.isspace()):
                self.space+=1
                self.consonant=self.upper+self.lower-self.vowel
    def display(self):
        print("The given string contains...")
        print("%d Uppercase letters"%self.upper)
        print("%d Lowercase letters"%self.lower)
        print("%d Vowels"%self.vowel)
        print("%d Consonants"%self.consonant)
        print("%d Spaces"%self.space)
S=String()
S.getstr()
S.count()
S.display()
