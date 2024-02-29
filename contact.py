contact = {
    'police': 112,
    'emergency': 101,
}

while True:
    name = input('Search any contacts:')
    if len(name) == 0:
        print("👋Bye!")
        break

    if name in contact:
        print(f"📞{name} is {contact[name]}")
    elif name == 'all':
        for name , number in contact.items():
            print(f"📞{name} is {number}")
        print('-'*20)
    else:
        print(f"👋{name} is not in the contact list")
        ch = input("🤔 Want to do contact? (y/n): ")
        if ch == 'y':
            number = input("📞 Enter number: ")
            contact[name] = number
            print(f"📞{name} is {number}")
            print('-'*20)