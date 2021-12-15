from tqdm import tqdm

def progress_bar(req, file_path):
    progress_bar = tqdm(total=int(req.headers.get('content-length', 0)), unit='iB', unit_scale=True)
    with open(file_path, 'wb') as file:
        for data in req.iter_content(1024): #block size 1Kibibyte
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()

    if int(req.headers.get('content-length', 0)) != 0 and progress_bar.n != int(req.headers.get('content-length', 0)):
           print("ERROR, something went wrong")