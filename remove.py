import os 

# this function is to remove audio and json files that have been done  

def remove(wav_dir, json_dir, tuned_json_dir): 
    for file in os.listdir(tuned_json_dir):
        print(file)
        wav_file = file[6:-5] + ".wav"
        wav_path = os.path.join(wav_dir,wav_file)
        json_file = file[6:] 
        json_path = os.path.join(json_dir,json_file)
        if os.path.isfile(wav_path):
            os.remove(wav_path)
        if os.path.isfile(json_path):
            os.remove(json_path)

if __name__=="__main__":
    # example 
    wav_dir = '/home/trinhtuanvu/kws/mini_sub/wav'
    json_dir = '/home/trinhtuanvu/kws/mini_sub/json'
    tuned_json_dir = '/home/trinhtuanvu/Downloads/tuned'
    remove(wav_dir, 
           json_dir, 
           tuned_json_dir)