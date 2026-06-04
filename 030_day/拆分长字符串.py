import re

poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'

sentences_List = re.split(r'[，。]',poem)
sentences_List = [sentence for sentence in sentences_List if sentence]   # 列表推导式
for sentence in  sentences_List:
    print(sentence)
