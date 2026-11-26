# Simple word-lexicon sentiment classifier (NLP demonstration).
positive={'good','great','love','excellent','happy'}; negative={'bad','hate','poor','awful','sad'}
def predict(text):
 words=text.lower().split(); score=sum(w.strip('.,!?') in positive for w in words)-sum(w.strip('.,!?') in negative for w in words)
 return 'positive' if score>0 else 'negative' if score<0 else 'neutral'
text='I love this excellent product'; print(text,'=>',predict(text))
