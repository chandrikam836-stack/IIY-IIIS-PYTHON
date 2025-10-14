Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Base Class - Animal 
... class Animal: 
... def  init (self, name): 
... self.name = name 
... def speak(self): 
... return "Some generic animal sound" 
... def move(self): 
... return "The animal moves around" 
... # Derived Class - cat 
... class cat(Animal): 
... def speak(self):return f"{self.name} says: Meow! Meow!" 
... def move(self): 
... return f"{self.name} runs quietly." 
... # Demonstration 
... cat = cat("cutie") 
... animals = [cat] 
... for animal in animals: 
... print(animal.speak()) 
