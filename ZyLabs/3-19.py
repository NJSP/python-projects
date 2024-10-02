my_flower1 = input()
my_flower2 = input()
my_flower3 = input()

your_flower1 = input()
your_flower2 = input()



my_list = [my_flower1, my_flower2, my_flower3]
your_list = [your_flower1, your_flower2]
our_list = my_list + your_list
print(our_list)


their_flower = input()
our_list.append(their_flower)
print(our_list)


our_list[1] = their_flower
print(our_list)


our_list.remove(their_flower)
print(our_list)

del our_list[1]
print(our_list)
