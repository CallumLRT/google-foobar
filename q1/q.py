def solution(string):
    result = ""

    # ASCII values for a and z
    a_num = ord('a') 
    z_num = ord('z')
    for char in string:
        # The current character's ASCII value
        char_num = ord(char)

        # If the character is lowercase
        if a_num <= char_num and char_num <= z_num:
            # Convert back to the original character and add it to the result string
            original_char_num = a_num + z_num - char_num
            result += chr(original_char_num)
        # Otherwise, just add the character to the result string
        else:
            result += char
    return result



# driver
if __name__ == '__main__':
    ex1 = solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
    print(ex1)
    print(ex1 == "did you see last night's episode?")
    ex2 = solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
    print(ex2)
    print(ex2 == "Yeah! I can't believe Lance lost his job at the colony!!")
