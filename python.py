def rev_sentence(sentence): 
    words = sentence.split(' ')  
      reverse_sentence = ' '.join(reversed(words))  
      return reverse_sentence   
if __name__ == "__main__": 
    input = 'AIET CHALLENGES IIT'
    print rev_sentence(input) 
