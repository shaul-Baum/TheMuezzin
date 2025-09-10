


class Calculations:
    def __init__(self,word_list_1:str,word_list_2:str):
        self.word_list_1 = self.split_text(word_list_1, ",")
        self.word_list_1 = self.split_list(self.word_list_1)
        self.word_list_2 = self.split_text(word_list_2, ",")
        self.word_list_2 = self.split_list(self.word_list_2)

    def word_search(self,text,word_list):
        found_sequences = []
        for i in range(len(text) - 1):
            current_two_words = [text[i],text[i + 1]]
            if current_two_words in word_list:
                found_sequences.append(" ".join(current_two_words))
            if text[i] in word_list:
                found_sequences.append(text[i])
        return len(found_sequences)

    def split_text(self,text,cutting_by):
        return text.lower().split(cutting_by)

    def split_list(self,word_list):
        search_sequences_words = []
        for seq in word_list:
            if " " in seq:
                search_sequences_words.append(seq.lower().split())
            else:
                search_sequences_words.append(seq.lower())
        return search_sequences_words

    def manager(self,text):
        text = self.split_text(text," ")
        list_writer1 = self.word_search(text,self.word_list_1)
        list_writer2 = self.word_search(text,self.word_list_2)
        bds_percent = self.risk_level(list_writer1,list_writer2,len(text))
        is_bds = list_writer1 > 1 or bds_percent > 40
        return bds_percent,is_bds

    def risk_level(self,hostile:int,less_hostile_writer:int,writer:int):
        extra = 0
        if hostile > len(self.word_list_1)/2:
            extra += 20
        if less_hostile_writer > len(self.word_list_2)/2 :
            extra += 10
        total_count = (hostile*2)+less_hostile_writer
        return  (total_count * (100/writer)) + extra



