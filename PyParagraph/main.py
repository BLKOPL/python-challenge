import os
import string

#establish route and data paths
root_path = os.path.join(os.getcwd(), ".")
data_path = os.path.join(root_path,"raw_data")
output_path = os.path.join(root_path, "output")

#iterate through the .listdir results so that
#code can be applied to all new incoming files.
filepaths = []
for file in os.listdir(data_path):
    if file.endswith(".txt"):
        filepaths.append(os.path.join(data_path,file))
        
for file in filepaths:
    sentence_count = 0
    letter_count = 0
    punctuations = set(string.punctuation)
    #establish a function to read .txt files and return 
    #a list of words and punctuations
    with open(file, "r") as resume_file_handler:
        #.split() all whitespaces from each word in file
        word_list = resume_file_handler.read().lower().split()
        word_count = len(word_list)
        for word in word_list:
            if word[-1] in punctuations:
                 letter_count += len(word) - 1
            else:
                 letter_count += len(word)
            if word[-1] == "." or word[-1] == "?" or word[-1] == "!":
                 sentence_count += 1    
        avg_letter = float("{0:2f}".format(letter_count/word_count))
        avg_sentence = float("{0:2f}".format(word_count/sentence_count))

    # Grab the filename from the original path.
        # The _, gets rid of the path.
    _, filename = os.path.split(file)  
    filename, _ = filename.split(".txt")
  
        # Print the analysis to the terminal.
    print(
        f"Paragraph Analysis - {filename}\n"
        f"----------------------------\n"
        f"Approximate Word Count: {word_count}\n" 
        f"Approximate Sentence Count: {sentence_count}\n"
        f"Average Letter Count: {avg_letter}\n"
        f"Average Sentence Length: {avg_sentence}\n"
        )

    text_path = os.path.join(output_path, filename + ".txt")
    with open(text_path, "w") as text_file:
        text_file.write(
           f"Paragraph Analysis - {filename}\n"
        f"----------------------------\n"
        f"Approximate Word Count: {word_count}\n" 
        f"Approximate Sentence Count: {sentence_count}\n"
        f"Average Letter Count: {avg_letter}\n"
        f"Average Sentence Length: {avg_sentence}\n"
        )
