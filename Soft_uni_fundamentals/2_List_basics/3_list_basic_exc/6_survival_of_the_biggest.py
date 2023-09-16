entry = input()

list_of_integers = list(map(int, entry.split(" ")))
number_n_remover = int(input())

sorted_list = sorted(list_of_integers)
remove_listing = sorted_list[0:number_n_remover]
for item in remove_listing:
    if item in list_of_integers:
        list_of_integers.remove(item)
final = map(str, list_of_integers)
print(", ".join(final))
