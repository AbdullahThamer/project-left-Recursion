def process_file():
    try:
        def custom_split(string, delimiter):
            result = ['']
            word_index = 0
            for char in string:
                if char == delimiter:
                    result += ['']
                    word_index += 1
                else:
                    result[word_index] += char
            return result

        def custom_replace(string, old, new):
            result = ''
            i = 0
            while i < len(string):
                if string[i:i+len(old)] == old:
                    result += new
                    i += len(old)
                else:
                    result += string[i]
                    i += 1
            return result

        def rightP(stored):
            for i in stored.keys():
                j = stored[i]
                j = custom_replace(j, ' ', '')
                j = custom_replace(j, '\t', '')
                stored[i] = list(filter(None, custom_split(j, '|')))
            return stored

        def leftP(stored):
            nr = {}
            for A in stored.keys():
                direct_recursion = [alpha for alpha in stored[A] if alpha[0] == A]
                no_recursion = [alpha for alpha in stored[A] if alpha[0] != A]
                if direct_recursion:
                    A_prime = A + "'"
                    nr[A] = [alpha + A_prime for alpha in no_recursion] if no_recursion else ["e"]
                    nr[A_prime] = [alpha[1:] + A_prime for alpha in direct_recursion] + ["e"]
                else:
                    nr[A] = stored[A]
            return nr

        with open("in_project.txt") as f:
            stored1 = {}
            for c in f:
                c = custom_replace(c, '\n', '')
                x = custom_split(c, '>')
                x[0] = custom_replace(x[0], ' ', '')
                x[0] = custom_replace(x[0], '\t', '')
                stored1[x[0]] = x[1]

        r = rightP(stored1)
        e = leftP(r)

        with open("out_project.txt", "w") as f:
            for i in e.keys():
                j = e[i]
                f.write(i + ' > ')
                for a in j:
                    f.write(a)
                    if a != j[-1]:
                        f.write(' | ')
                f.write('\n')

        print("Successful code execution!")
    except Exception as e:
        print("An error occurred:", e)

process_file()
