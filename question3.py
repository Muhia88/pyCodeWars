
def capital(sequence):
  sentences = []
  
  for entry in sequence:
      
    if 'state' in entry:
      location = entry['state']
    elif 'country' in entry:
      location = entry['country']
    else:
      continue  
    
    capital = entry['capital']
  
    sentences.append(f"The capital of {location} is {capital}")
    
    return sentences
