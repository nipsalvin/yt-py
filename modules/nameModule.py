#__name__ is a special variale that shows the module name of the starting point of execution of code
def main():
    print("Default Hello ", __name__) #Here "__name__" prints out "__main__"
    print("Welcom to my page.")

if __name__ == "__main__": #This function is called and runs if the "__name__" variable is "__main__"
    main()

print("This '__name__' is imported from the module to :",__name__)