# T = "Hello my name's Alireza!."
#
# print(T)
#
# print(T.replace("Alireza", "Mohammad")) # For Change One Time.
#
# New_T = T.replace("Alireza", "Mohammad!") # For Change Forever.
# print(New_T)
from tabnanny import check

#         ******************************************************************************        #
                                        #  strip  #

# T = "   Alireza    "
#
# New_T = T.strip() # For Strip Any Space In (T).
# print(New_T)

#         ******************************************************************************        #
                                        #  split  #

# T = "Alireza, Mohammad, pouria"
# N = "2025=4=11"
#
# New_N = N.split("=")
# print(New_N)
#
# New_T = T.split(",") # For Use  Split String To List.
# print(New_T)

#         ******************************************************************************        #
                                        # Join  #

# T = ["Alireza", "Mohammad", "Pouria"]
#
# if T == list(T):
#     print("-".join(T)) # For List To String.
# else:
#     print(False)

#         ******************************************************************************        #
                                       # Lower And Upper And Capitalize And Title #

# T = "ALIREZA"
# T_2 = "alireza"
#
# print(T.lower()) # For Change Upper String To Lower Word.

# print(T_2.upper()) # For Change Lower String to Upper String.

# print(T.capitalize()) # For Upper First Word Of String.
#
# print(T.title()) # For Upper Only First word In Strings.

#         ******************************************************************************        #
                                       # StartWith And EndWith #

# T = "https.com"
#
# Check_Start_with = T.startswith("https") # For check Is It start with my target or not.
# print(Check_Start_with)
#
# check_end_with = T.endswith("com") # For check Is It End With My Target Or Not.
# print(check_end_with)

#         ******************************************************************************        #
                                            # Find #

# T = "Hello Alireza "
#
# Find_Alireza = T.find("Alireza") # For Find String. If It's Find Show(index).
# print(Find_Alireza)
#
# F = T.find("f") # For Find String. If It isn't Find Show(-1)
# print(F)

#         ******************************************************************************        #
                                            # Count #

# T = "alireza"
#
# print(T.count("a")) # For Search How Many A word Or Noun Repeat In String.

#         ******************************************************************************        #
                                        # Isalpha And Isdigit And Isalnum  #

# T = "Alireza"
# T_2 = "3"
# T_3 = ("1hd3")

# Check = T.isalpha() # For Check Is string Have word ?
# print(Check)
#
# Check_2 = T_2.isdigit() # For check Is String Have Num ?
# print(Check_2)

# Check_3 = T_3.isalnum() # For Check Is String Have word Or num ?
# print(Check_3)

#         ******************************************************************************        #
                                          # F-String #

# T = "ali"
# print(f"My name's {T}") # For Use String Data In Print.


                                          # and etc #
#         ******************************************************************************        #






