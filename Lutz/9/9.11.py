with open('../myfile.txt', 'w') as txtfile:
    txtfile.write('Hello file world!\n')
with open('../myfile.txt', 'r') as txtfile:
    print(txtfile.read())