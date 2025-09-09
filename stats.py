def get_words(content):
    return len(content.split())

def get_stats(content):
    stats_dict = {}
    for chunk in content:
        chunk = chunk.lower()
        if chunk in stats_dict.keys():
            stats_dict[chunk] += 1
        else:
            stats_dict[chunk] = 1
    return stats_dict

def sort_stats(stats_dict):

    temp = []

    def sort_on(items):
        return items['num']
    
    for key, value in stats_dict.items():
        if key.isalpha():
            temp.append({'char':key, 'num':value})
    
    temp.sort(reverse=True, key=sort_on)

    return temp