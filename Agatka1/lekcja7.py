with open ("choinka.txt", 'w') as file:
#     file. write('*\n')
# with open("choinka.txt", 'a') as file:
#     file. write('**\n')
# with open("choinka.txt", 'a') as file:
#     file. write('***\n')
# with open("choinka.txt", 'a') as file:
#     file. write('****\n')
# with open("choinka.txt", 'a') as file:
#     file. write('*****\n')
# with open("choinka.txt", 'a') as file:
#     file. write('*****\n')
# with open("choinka.txt", 'a') as file:
#     file. write('******\n')
# with open("choinka.txt", 'a') as file:
#     file. write('*******\n')
# with open("choinka.txt", 'a') as file:
#     file. write('********\n')
    for i in range(15):
        file.write('*'*i+ '\n')
    # file.write('\n'.join('*'*i for i in range(4)))
    for i in range(15):
        file.write(' '*(15-i)+ 'o'*(i)+  'o'*(i)+ '\n')


