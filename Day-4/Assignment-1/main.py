# 7.Ivan Vukomanovic is the coach of ISL Club Kerala Blasters. Ask the coach of his biggest dream and note it down in a file named dream.txt

def dream_function(response):
    with open("dreams.txt","w") as f:
        f.write(response)
        print("Dream successfully added...")

response_from_ivan = input(" What's your biggest dream ?")
dream_function(response_from_ivan)