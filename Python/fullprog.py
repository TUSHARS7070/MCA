#  to count the frequency of any specific word (in your domain) in the paragraph.

def count_symbols(paragraph):
    alphabet_count = 0
    numeric_count = 0
    special_count = 0

    for char in paragraph:
        if char.isalpha():
            alphabet_count += 1
        elif char.isdigit():
            numeric_count += 1
        else:
            special_count += 1

    return alphabet_count, numeric_count, special_count


if __name__ == "__main__":
    paragraph="I'm TUSHAR SAKHUJA, from Jamshedpur. My mobile no. is 8102673082. Roll no. 2347262. I am pursuing MCA from Christ University and had done BCA from SYMBIOSIS INTERNATIONAL UNIVERSITY. I also have an experice and knowledge in Mobile-Device-Managemengt ,digital marketing and poster making. It is a software that helps you edit /create your text, let’s you save your file after work and later you can open those files for re-editing. This software is designed to produce streamlined formatted documents.Scribble Pad has basic IDE features, Notepad is a text editor shipped with Windows since 95/98. Scribble Pad is designed to have the capability of a basic IDE while retaining the familiarity of Notepad. syntax highlighting in Scribble Pad. notepad is like a paper that can write anything Scribble Pad is notepad+=1 means better than notepad. Scribble Pad. The immediate difference is that it immediately shows you what is happening with your code."
    alphabet_count, numeric_count, special_count = count_symbols(paragraph)

    print(f"Number of alphabets: {alphabet_count}")
    print(f"Number of numeric characters: {numeric_count}")
    print(f"Number of special symbols: {special_count}")

# to display all the datatypes of selected specific elements in the paragraph.


paragraph="I'm TUSHAR SAKHUJA, from Jamshedpur. My mobile no. is 8102673082. Roll no. 2347262. I am pursuing MCA from Christ University and had done BCA from SYMBIOSIS INTERNATIONAL UNIVERSITY. I also have an experice and knowledge in Mobile-Device-Managemengt ,digital marketing and poster making. It is a software that helps you edit /create your text, let’s you save your file after work and later you can open those files for re-editing. This software is designed to produce streamlined formatted documents.Scribble Pad has basic IDE features, Notepad is a text editor shipped with Windows since 95/98. Scribble Pad is designed to have the capability of a basic IDE while retaining the familiarity of Notepad. syntax highlighting in Scribble Pad. notepad is like a paper that can write anything Scribble Pad is notepad+=1 means better than notepad. Scribble Pad. The immediate difference is that it immediately shows you what is happening with your code."

num=["0","1","2","3","4","5","6","7","8","9"]
spld_word=paragraph.split(" ")
for i in spld_word:
    for j in i:
        if j in num:
            if "." in i:
                print(i," is float")
                break
            else:
                print(i,"is int")
                break
        else:
            print(i," : is string")
            break

# to count the number of alphabets, numeric and other special symbols in the paragraph.


def count_word_frequency(paragraph, target_word):
    paragraph = paragraph.lower()
    words = paragraph.split()
    word_count = 0

    for word in words:
        word = word.strip('.,!?;:"()[]{}')
        if word == target_word.lower():
            word_count += 1

    return word_count

if __name__ == "__main__":
    paragraph = "I'm TUSHAR SAKHUJA, from Jamshedpur. My mobile no. is 8102673082. Roll no. 2347262. I am pursuing MCA from Christ University and had done BCA from SYMBIOSIS INTERNATIONAL UNIVERSITY. I also have an experice and knowledge in Mobile-Device-Managemengt ,digital marketing and poster making. It is a software that helps you edit /create your text, let’s you save your file after work and later you can open those files for re-editing. This software is designed to produce streamlined formatted documents.Scribble Pad has basic IDE features, Notepad is a text editor shipped with Windows since 95/98. Scribble Pad is designed to have the capability of a basic IDE while retaining the familiarity of Notepad. syntax highlighting in Scribble Pad. notepad is like a paper that can write anything Scribble Pad is notepad+=1 means better than notepad. Scribble Pad. The immediate difference is that it immediately shows you what is happening with your code."
    target_word = input("Enter the word to count its frequency in the paragraph: ")

    frequency = count_word_frequency(paragraph, target_word)

    print(f"The word '{target_word}' appears {frequency} times in the paragraph.")


# #sorting the set
def set_operations_example():
    string_set = {"Java","Python","Web-Satck","Database_tech"}
    print("Initial Set:", string_set)
    sorted_set = sorted(string_set, reverse=True)
    print("Sorted Set (Descending Order):", sorted_set)
set_operations_example()

#packing and unpacking of tuple
def slicing_and_negative_indexing(domain):
    print("\nOriginal Domain Name:", domain)
    print("\nPositive Slicing:")
    print("1. Slicing from index 3 to 9:", domain[3:10])
    print("2. Slicing from index 0 to 7:", domain[0:8])
    print("3. Slicing from index 5 to the end:", domain[5:])
    print("4. Slicing from index 2 to 11 with step 2:", domain[2:12:2])
    
    print("\nNegative Slicing:")
    print("1. Slicing from the end -8 to the end -3:", domain[-8:-2])
    
    
    print("\nNegative Indexing:")
    print("Last character:", domain[-1])
    print("Second to last character:", domain[-2])
    
domain = "Web-Hosting"
slicing_and_negative_indexing(domain)

#Word Count


dmn_name=("W","E","B","H","O","S","T","I","N","G")
count=0
for i in dmn_name:
    count=count+1
print("count of Names:",count)

#tuple slicing

def slicing_and_negative_indexing(domain):
    print("\nOriginal Domain Name:", domain)
    print("\nPositive Slicing:")
    print("1. Slicing from index 3 to 9:", domain[3:10])
    print("2. Slicing from index 0 to 7:", domain[:8])
    print("3. Slicing from index 5 to the end:", domain[5:])
    print("4. Slicing from index 2 to 11 with step 2:", domain[2:12:2])
    print("\nNegative Slicing:")
    print("1. Slicing from the end -8 to the end -3:", domain[-8:-2])
    print("2. Slicing from the end -11 to the end -1 with step 2:", domain[-11:-1:2])
    print("\nNegative Indexing:")
    print("Last character:", domain[-1])
    print("Second to last character:", domain[-2])
domain = "Web-Hosting"
slicing_and_negative_indexing(domain)


#Pop

def set_operations_example():
    mixed_set = {1, "Python", 2.263, True, (1, 2)}
    print("Initial Set:", mixed_set)
    popped_element = mixed_set.pop()
    print("\nElement popped:", popped_element)
    print("Updated Set after pop:", mixed_set)
    mixed_set.clear()
    print("\nSet after clear:", mixed_set)
    mixed_set.add(42)
    mixed_set.add("Python")
    mixed_set.add("World")
    mixed_set.add(False)
    mixed_set.add((3, 4))
    mixed_set.update(["Java","Python","C++","Mongodb"])  
    print("Set after adding elements:", mixed_set)
    mixed_set.discard("World")
    print("\nSet after discarding 'World':", mixed_set)
    del mixed_set
set_operations_example()
