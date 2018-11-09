import words
import random
def count_substring_v1(string, target):
    count = 0
    index = 0
    while index < len(string) - len(target) +1 :
        if string[index : index + len(target)] == target :
            count += 1
        index +=1
    return count

def count_substring_v2(string, target):
    count = 0
    index = 0
    while index < len(string) - len(target) +1:
        if string[index : index + len(target)] == target :
            count += 1
            index += len(target)
        else:
            index += 1
        return count


def locate_first(string, sub):
    matches = []
    index = 0
    while index < (len(string) - len(sub) + 1 ):
        if string[index : index + len(sub)] == sub :
            matches.append(index)
            index += 1
        else:
            index += 1
    return matches

# print(count_substring_v2('AAAA', 'AA'))
# print(locate_first('cookbook','ook'))

def silly_string(nouns, verbs, templates):
    position = 0
    template = random.choice(templates)
    output = []
    while position < len(template):
        if template[position : position+8] == "{{noun}}":
            output.append(random.choice(nouns))
            position += 8
        elif template[position: position + 8] =="{{verb}}":
            output.append(random.choice(verbs))
            position += 8
        else:
            output.append(template[position])
            position += 1

    return ''.join(output)
if __name__ == '__main__':
    print(silly_string(words.nouns, words.verbs, words.templates))
