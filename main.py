from caesar import caesar
from intro import get_instructions, title_card

def main():
    close = False
    title_card()
    while close != True:
        text, shift, encode_or_decode = get_instructions()
        output_text = caesar(text=text, shift=shift, encode_or_decode=encode_or_decode)
        print(f"\nHere is the {encode_or_decode}d text: {output_text}")

        close = input("\nType 'yes' if you want to go again. Otherwise, type 'no':\n> ").lower() == "no"
    print("\nAlright. Goodbye!")

if __name__ == "__main__":
    main()