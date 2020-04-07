from re import sub

if __name__ == '__main__':

    languages = {}
    with open('../../OriginalDataSet/db.txt', 'r') as reader:
        current_language = None
        for line in reader:
            new_line = sub('\r?\n$', '', line)
            if new_line:
                if '\t' not in new_line:
                    current_language = new_line
                    languages[current_language] = {}
                else:
                    new_line_list = new_line.split('\t')
                    languages[current_language][new_line_list[1]] = new_line_list[3]

    sum_total = {}
    for keys, language in languages.items():
        sum_total[keys] = sum([float(x) for x in language.values()])

    for keys, language in languages.items():
        for key in language.keys():
            language[key] = float(language[key]) / sum_total[keys]

    keep_going = True
    similarities = {}
    for key, dictionary in languages.items():
        for k, dictio in languages.items():
            if keep_going:
                if k == key:
                    keep_going = False
                continue

            if len(dictionary) < len(dictio):
                first = dictionary
                second = dictio
            else:
                first = dictio
                second = dictio

            similarity = 0.0

            for ke, ve in first.items():
                other_value = second.get(ke, 0)
                similarity += float(ve) * float(other_value)
            similarities[f'{key}\t{k}'] = '%.4f' % similarity
        keep_going = True


    similarities = dict(sorted(list(similarities.items()), key=lambda x: x[1], reverse=True))

    for k, v in similarities.items():
        print(k, v)
