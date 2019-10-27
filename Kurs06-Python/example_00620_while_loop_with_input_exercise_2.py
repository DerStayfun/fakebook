# Schreibe eine while Schleife
# sie bricht nur dann ab, wenn der User "yes" oder "no" eingegeben hat


answer = None
while True:
    answer = input("Answer with yes or no: ")
    if answer == "yes" or answer == "no":
        break