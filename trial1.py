import Algorithmia
input = {
"image": "data://Desktop//holi.jpeg " # Location of image
}
client = Algorithmia.client("#######") #insert your own API key
algo = client.algo('deeplearning/ColorfulImageColorization/1.0.1')
print(algo.pipe(input))
