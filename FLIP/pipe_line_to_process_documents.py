# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 17:58:36 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""
# list all functions in the project
# do we want to do a single dcoument at a time?
class document_vectorizer():
    def __init__(self):
        super().__init__()

        self.weights = {}
        self.biases = {}
        self.inputs = {}
        self.hidden_size = hidden_size
        self.input_size = input_size
        self.output_size = output_size
    
def decide_which_document_to_upload():
    """ Look thru which document we have in the embedding database and start on the list so we don't repeat"""
    import psycopg2
    conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
    cur = conn.cursor()
    ( f""" SELECT ID, case_name, links
                      FROM embeddings_of_cases 
                      ORDER BY ID DESC 
                      LIMIT 1 OFFSET ;""")
    cur_result= cur.fetchall()
    document_text=cur_result[0][2]
    return last_document_uploaded

    
    
def upload_text(last_document_uploaded):
    """ Bring the text from the sql database into the python program"""
    
    
    import psycopg2
    conn = psycopg2.connect(dbname="can_law_accessible", user="postgres", password="Meganiscute")
    cur = conn.cursor()
    
    document_asked_for=cur.execute( f""" SELECT ID, case_name, full_case_text
                      FROM full_cases 
                      ORDER BY ID DESC 
                      LIMIT 1 OFFSET {document_we_want};""") #OFFSET 20 is telling Postgres to skip the first 20 records.
    cur_result= cur.fetchall()
    document_text=cur_result[0][2]
    return document_text
    


def pre_process_text(document):
    # what do i want the text to look like before i put it into the network bascially
    import re
    import unicodedata
    """ remove extra spacing, names, tabs, and other unwanted values"""
    f= document.replace("\n"," ")
    f= f.replace("\t"," ")
    f= f.replace("\r"," ")
    f=re.sub(r" \\\s+", r" ", f)
    f = unicodedata.normalize("NFKD", f)
    return f
    #break corpus into sentences
    

def divide_doc_into_sentences(document):
    """ apply modified nltk sentence divider""" # need to find the sentence tokenizer, maybe can modify the code to make it go fast
    from nltk.tokenize import sent_tokenize
    from nltk.tokenize import word_tokenize
    sentences = sent_tokenize(document)
    
    return sentences
def generate_contexualized_sentences(sentences):
    """ need to keep context for when inputting text into the tokenizer"""
    import re
    contexualzed_sentennce_list = []
    find_word_pattern = re.compile(r"\w+")

    for i,  sentence_2 in enumerate(sentences):
        if i ==0:
            existing_sentences= " "

        words_remove_from_sentence = find_word_pattern.findall(existing_sentences)
        finding_words_to_remove_len =len(words_remove_from_sentence)
        #print(finding_words_to_remove_len)
        
        if finding_words_to_remove_len > 550:
            
            
            word_to_be_removed_for_next_iteration= words_remove_from_sentence[-550]
            
            #print(word_to_be_removed_for_next_iteration)
            
            pattern_to_find_word_to_be_kept = re.compile(f"{word_to_be_removed_for_next_iteration}")
            
            identifier_for_removing_from_string=re.search(pattern_to_find_word_to_be_kept, string=existing_sentences)
            
            end_of_word_needed_segment_sentence= identifier_for_removing_from_string.span()[1]
            existing_sentences=existing_sentences[end_of_word_needed_segment_sentence:]
            
        contexualzed_sentennce_list.append([existing_sentences,sentence_2])
        existing_sentences= existing_sentences + " " + f"{sentence_2}"
        

    return contexualzed_sentennce_list
        
    
  
def tokenize_document(contexualzed_sentennce_list):
    from transformers import DebertaTokenizerFast
    tokenizer = DebertaTokenizerFast.from_pretrained("microsoft/deberta-base")
    

    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    
    finding_start_of_second_sentence=re.compile(r"1")
    for sentence_3 in contexualzed_sentennce_list:
        inputs = tokenizer(existing_sentences, sentence_2, return_tensors="pt", truncation=True, return_token_type_ids=True).to("cuda")
        ids_of_tokens=inputs['input_ids'].tolist()
        [ids_of_tokens] = ids_of_tokens
        strwoo=(str((inputs['token_type_ids'])))


        
        tokens_in_current_sentence= re.findall(finding_start_of_second_sentence, string=strwoo)
        amount_of_tokens=len(tokens_in_current_sentence)-1  # for final token that will be labeled as 
        #print(amount_of_tokens)
        del inputs["token_type_ids"]
        
        
   
    return inputs

   
def embedding_postiion_saver():
    """ saving the position of the words(whether divided or not) to check pos and eventually apply cosine simialirty"""
    
    
    
   
def generate_embeddings(inputs):
    """ converting text to embeddings using a pre-trained deberta model"""
    from transformers import  DebertaModel
    print(inputs["input_ids"].is_cuda)
    model = DebertaModel.from_pretrained("microsoft/deberta-base").to("cuda")
    print((model.parameters()).is_cuda )

    output = model(**inputs)
    return output

   


def pos_tag_embeddings_in_sentence(embeddings):
    """ using pos tags from spacy feed embeddings of model and mark a sentences words with their coresponding pos, output the embeddings there part of speech and the corresponding word the embeddning represents"""
    sentence_list = []
    
    new_key =word + "====" + pos
    
    word_dic["word===pos"]=embedding
    sentence_list.append(word_dic)
    return sentence_list
    
def remove_unwanted_sentences():
    """ feed in all sentences in their embedding format and output only sentences that are cleaned and want to work with"""
    #shit that is not useful for deberta embeddings
    
    
    
def create_document_dictionary_of_embeddings():
    """ sentences words came from as a key, with keys and values insides this key of the words and associated embeddings in each sentences"""
    document_dictionary
    document_dictionary = {sentence_number:[{"word===pos":embedding},{"word===pos":embedding},{"word===pos":embedding}]}
    
    return document_dictionary
    

    
    
def storing_document_embedding_dic_of_pos():
    """ writing document information including pos, words, embeddings for words, sentence placement and other to an sql database"""
    import posgreql 
    #store dictonary in sql database
    #row for pos, word, sentence, document and embedding, court the document is from and so on.
    
    

    



    
def train_firac_model_verb():
    """  use verb embeddings in a sentence feed in FFn to produce model too train this model""" # need to figure out how to frame model for this task, verbs will go into one model 

    
def train_firac_model_noun():
    """  use noun embeddings in a sentence feed in FFn to produce model too train this model""" # need to figure out how to frame model for this task, verbs will go into one model and nouns will go into another, this way alikes are compared and model wil


            
            
    
def cosine_simairlity_pos_embeddings(doc1, doc2):
    """ check cosine simailirty of all sentences in two  documents comparing nouns against other nouns and verbs against verbs output list of cosine simialrities of each and also sentence level averages"""
    from torch.nn import CosineSimilarity


def store_sentence_cosine_simiarities():
    """ save to sql return a succcessul storage in a sql database of cosine comparasion, need to link this data to corepsonding document database"""
    
def doc_to_doc_network(input_judgement_sentence, label_factum_sentence):
    """ converting a judgement embeddings into a factum embeddings and if they retain a high cosine simialrity and are decided to be related based upon this cosine simialrity"""
def fact_pattern_input_for_pipeline():
    """ the fact pattern that we generate form the case we are working on"""

def find_case_fact_cluster():
    """ compare each fact sentence in a document to another fact sentence in a document on the basis of noun and verbs """

def find_case_by_fact():
    """ pick a single case from the case cluster based upon the closeest simialirity """
    
def find_issues():
    """ compare results of fact search choice among issue sentences"""

def find_argument():
    """ compare results of issue search against the true argument to determine a list of best arguments that might be used in a decision"""
    

def find_law_in_issue_or_argument():
    """ locate all mentions of law in the document by searching the cases and legislation that is used in the document"""
    
    
def find_similar_law():
    """find this law to make the argument relevent in the jurisdiction you are working in"""




